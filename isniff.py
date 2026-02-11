#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iSniffNetwork - MAC Address Network Sniffer
Liest MAC-Adressen von direkt angeschlossenen Geräten aus
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import sys
import ctypes
from scapy.all import sniff, ARP, Ether, get_if_list, get_if_hwaddr, conf
import psutil
import time
import re


class NetworkSnifferGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("iSniffNetwork - MAC Address Sniffer")
        self.root.geometry("700x550")
        self.root.resizable(False, False)
        
        self.is_scanning = False
        self.sniffer_thread = None
        self.mac_packet_count = {}  # Zählt Pakete pro MAC
        self.primary_mac = None
        self.primary_ip = None
        self.interface_map = {}  # Map zwischen Display-Name und Scapy-Interface
        
        self.setup_ui()
        self.load_network_adapters()
        
    def setup_ui(self):
        """GUI-Elemente erstellen"""
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="iSniffNetwork", 
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Main Content Frame
        content_frame = tk.Frame(self.root, padx=20, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Adapter Selection
        adapter_frame = tk.LabelFrame(
            content_frame, 
            text="Netzwerkadapter auswählen",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=10
        )
        adapter_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.adapter_var = tk.StringVar()
        self.adapter_dropdown = ttk.Combobox(
            adapter_frame,
            textvariable=self.adapter_var,
            state="readonly",
            width=60,
            font=("Arial", 9)
        )
        self.adapter_dropdown.pack(fill=tk.X, pady=5)
        
        refresh_btn = tk.Button(
            adapter_frame,
            text="🔄 Adapter aktualisieren",
            command=self.load_network_adapters,
            bg="#3498db",
            fg="white",
            font=("Arial", 9),
            cursor="hand2",
            relief=tk.FLAT,
            padx=10,
            pady=5
        )
        refresh_btn.pack(pady=(5, 0))
        
        # Control Buttons
        button_frame = tk.Frame(content_frame)
        button_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.scan_btn = tk.Button(
            button_frame,
            text="▶ Scan starten",
            command=self.start_scan,
            bg="#27ae60",
            fg="white",
            font=("Arial", 12, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            width=20
        )
        self.scan_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.stop_btn = tk.Button(
            button_frame,
            text="⏹ Scan stoppen",
            command=self.stop_scan,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 12, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            width=20,
            state=tk.DISABLED
        )
        self.stop_btn.pack(side=tk.LEFT)
        
        # Results Frame
        results_frame = tk.LabelFrame(
            content_frame,
            text="Verbundenes Gerät am anderen Ende",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=15
        )
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # MAC Display
        mac_label = tk.Label(
            results_frame,
            text="MAC-Adresse:",
            font=("Arial", 11),
            anchor=tk.W
        )
        mac_label.pack(fill=tk.X, pady=(5, 0))
        
        self.mac_value = tk.Label(
            results_frame,
            text="--:--:--:--:--:--",
            font=("Consolas", 20, "bold"),
            fg="#27ae60",
            bg="#ecf0f1",
            anchor=tk.W,
            padx=10,
            pady=10
        )
        self.mac_value.pack(fill=tk.X, pady=(0, 15))
        
        # IP Display
        ip_label = tk.Label(
            results_frame,
            text="IP-Adresse:",
            font=("Arial", 11),
            anchor=tk.W
        )
        ip_label.pack(fill=tk.X, pady=(5, 0))
        
        self.ip_value = tk.Label(
            results_frame,
            text="---.---.---.---",
            font=("Consolas", 16, "bold"),
            fg="#3498db",
            anchor=tk.W,
            padx=10
        )
        self.ip_value.pack(fill=tk.X, pady=(0, 15))
        
        # Vendor/OUI Display
        vendor_label = tk.Label(
            results_frame,
            text="OUI (Vendor Prefix):",
            font=("Arial", 11),
            anchor=tk.W
        )
        vendor_label.pack(fill=tk.X, pady=(5, 0))
        
        self.vendor_value = tk.Label(
            results_frame,
            text="--:--:--",
            font=("Consolas", 14),
            anchor=tk.W,
            padx=10
        )
        self.vendor_value.pack(fill=tk.X, pady=(0, 10))
        
        # Packet Counter
        self.packet_counter = tk.Label(
            results_frame,
            text="Empfangene Pakete: 0",
            font=("Arial", 9),
            fg="#7f8c8d",
            anchor=tk.W
        )
        self.packet_counter.pack(fill=tk.X, pady=(10, 0))
        
        # Status Bar
        self.status_var = tk.StringVar()
        self.status_var.set("Bereit")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg="#ecf0f1",
            font=("Arial", 9)
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def load_network_adapters(self):
        """Alle verfügbaren Netzwerkadapter laden"""
        try:
            adapters = []
            self.interface_map = {}
            
            # Hole alle Scapy-Interfaces
            scapy_interfaces = get_if_list()
            
            # Hole alle Netzwerkinterfaces mit psutil
            if_addrs = psutil.net_if_addrs()
            if_stats = psutil.net_if_stats()
            
            # Erstelle eine Zuordnung zwischen psutil-Namen und Scapy-Interface-Namen
            for iface_name, addrs in if_addrs.items():
                # Finde MAC-Adresse
                mac = None
                ip = None
                is_up = iface_name in if_stats and if_stats[iface_name].isup
                
                for addr in addrs:
                    if addr.family == psutil.AF_LINK:  # MAC-Adresse
                        mac = addr.address
                    elif addr.family == 2:  # IPv4
                        ip = addr.address
                
                # Nur hinzufügen wenn MAC vorhanden und nicht leer
                # Zeige ALLE Adapter mit MAC, auch wenn kein Kabel angeschlossen ist
                if mac and mac != '00:00:00:00:00:00' and mac != '00-00-00-00-00-00':
                    # Finde das passende Scapy-Interface
                    scapy_iface = self.find_scapy_interface(iface_name, mac, scapy_interfaces)
                    
                    if scapy_iface:
                        display_name = f"{iface_name}"
                        
                        # Status-Indikatoren hinzufügen
                        if ip and not ip.startswith('169.254'):
                            display_name += f" (IP: {ip})"
                        elif ip:
                            display_name += f" (IP: {ip})"
                        
                        if not is_up:
                            display_name += " [INAKTIV]"
                        
                        adapters.append(display_name)
                        self.interface_map[display_name] = scapy_iface
            
            if not adapters:
                adapters = ["Keine Netzwerkadapter gefunden"]
            
            self.adapter_dropdown['values'] = adapters
            if adapters and adapters[0] != "Keine Netzwerkadapter gefunden":
                self.adapter_dropdown.current(0)
            
            self.status_var.set(f"Bereit - {len(adapters)} Adapter gefunden")
            
        except Exception as e:
            self.status_var.set(f"Fehler beim Laden der Adapter: {str(e)}")
    
    def find_scapy_interface(self, iface_name, mac, scapy_interfaces):
        """Findet das passende Scapy-Interface für einen psutil-Interface-Namen"""
        try:
            # Normalisiere MAC-Adresse (Windows verwendet manchmal '-' statt ':')
            mac_normalized = mac.replace('-', ':').lower()
            
            # 1. Versuch: Direkter Match des Namens
            if iface_name in scapy_interfaces:
                return iface_name
            
            # 2. Versuch: Interface-Name in Scapy-Namen enthalten
            for scapy_iface in scapy_interfaces:
                if iface_name.lower() in scapy_iface.lower():
                    return scapy_iface
            
            # 3. Versuch: Vergleiche MAC-Adressen
            for scapy_iface in scapy_interfaces:
                try:
                    scapy_mac = get_if_hwaddr(scapy_iface).lower()
                    if scapy_mac == mac_normalized:
                        return scapy_iface
                except:
                    continue
            
            # 4. Versuch: Nutze Windows GUID-Matching
            for scapy_iface in scapy_interfaces:
                # Extrahiere GUID aus Scapy-Interface-Namen
                if '{' in scapy_iface and '}' in scapy_iface:
                    guid_match = re.search(r'\{[0-9A-Fa-f-]+\}', scapy_iface)
                    if guid_match:
                        guid = guid_match.group(0)
                        # Prüfe ob die GUID in Windows-Registry mit dem Interface übereinstimmt
                        # Für diesen einfachen Fall akzeptieren wir es
                        return scapy_iface
            
            return None
            
        except Exception as e:
            return None
            
    def get_selected_interface(self):
        """Ausgewähltes Interface ermitteln"""
        selected = self.adapter_var.get()
        if not selected or selected == "Keine Netzwerkadapter gefunden":
            return None
        # Nutze die Interface-Map um den korrekten Scapy-Interface-Namen zu erhalten
        return self.interface_map.get(selected, None)
    
    def start_scan(self):
        """Scan-Prozess starten"""
        if self.is_scanning:
            return
            
        interface = self.get_selected_interface()
        if not interface:
            messagebox.showerror("Fehler", "Bitte wähle einen Netzwerkadapter aus!")
            return
        
        # Admin-Rechte prüfen
        if not self.is_admin():
            messagebox.showerror(
                "Admin-Rechte erforderlich",
                "Dieses Programm benötigt Administrator-Rechte zum Sniffing!\n"
                "Bitte starte das Programm als Administrator."
            )
            return
        
        self.is_scanning = True
        self.mac_packet_count.clear()
        self.primary_mac = None
        self.primary_ip = None
        
        # Reset display
        self.mac_value.config(text="Suche...", fg="#f39c12")
        self.ip_value.config(text="---")
        self.vendor_value.config(text="---")
        self.packet_counter.config(text="Empfangene Pakete: 0")
        
        self.scan_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.adapter_dropdown.config(state=tk.DISABLED)
        
        self.status_var.set(f"Scanne auf Interface: {interface}")
        
        # Sniffer-Thread starten
        self.sniffer_thread = threading.Thread(
            target=self.sniff_packets,
            args=(interface,),
            daemon=True
        )
        self.sniffer_thread.start()
    
    def stop_scan(self):
        """Scan-Prozess stoppen"""
        self.is_scanning = False
        self.scan_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.adapter_dropdown.config(state=tk.READONLY)
        
        if self.primary_mac:
            self.status_var.set("Scan gestoppt - Gerät gefunden")
        else:
            self.status_var.set("Scan gestoppt - Kein Gerät gefunden")
            self.mac_value.config(text="Kein Gerät gefunden", fg="#e74c3c")
    
    def sniff_packets(self, interface):
        """Pakete sniffen und die wichtigste MAC-Adresse identifizieren"""
        try:
            # Ermittle ALLE eigenen MAC-Adressen (von allen lokalen Interfaces)
            own_macs = set()
            try:
                # Eigene MAC des ausgewählten Interfaces
                own_mac = get_if_hwaddr(interface).lower()
                own_macs.add(own_mac)
                
                # Alle anderen lokalen Interface-MACs
                if_addrs = psutil.net_if_addrs()
                for iface_name, addrs in if_addrs.items():
                    for addr in addrs:
                        if addr.family == psutil.AF_LINK:
                            mac = addr.address.replace('-', ':').lower()
                            if mac and mac != '00:00:00:00:00:00':
                                own_macs.add(mac)
                
                self.status_var.set(f"Scanne auf Interface: {interface} (Filter: {len(own_macs)} eigene MACs)")
            except Exception as e:
                self.status_var.set(f"Scanne auf Interface: {interface}")
            
            total_packets = 0
            
            def packet_handler(packet):
                nonlocal total_packets
                if not self.is_scanning:
                    return True  # Stoppt das Sniffing
                
                try:
                    # Ethernet-Layer prüfen
                    if packet.haslayer(Ether):
                        src_mac = packet[Ether].src
                        src_mac_lower = src_mac.lower()
                        
                        # Eigene MACs, Broadcast und Multicast filtern
                        if src_mac_lower != 'ff:ff:ff:ff:ff:ff' and \
                           src_mac_lower not in own_macs and \
                           not src_mac.startswith('01:00:5e') and \
                           not src_mac.startswith('33:33'):  # IPv6 Multicast filtern
                            
                            # Pakete zählen
                            if src_mac not in self.mac_packet_count:
                                self.mac_packet_count[src_mac] = {'count': 0, 'ip': None}
                            
                            self.mac_packet_count[src_mac]['count'] += 1
                            total_packets += 1
                            
                            # IP-Adresse speichern falls vorhanden
                            if packet.haslayer(ARP):
                                self.mac_packet_count[src_mac]['ip'] = packet[ARP].psrc
                            
                            # Finde die MAC mit den meisten Paketen
                            primary = max(self.mac_packet_count.items(), 
                                        key=lambda x: x[1]['count'])
                            
                            self.primary_mac = primary[0]
                            self.primary_ip = primary[1]['ip']
                            
                            # Update GUI
                            self.update_display()
                            self.packet_counter.config(
                                text=f"Empfangene Pakete: {total_packets} | Von diesem Gerät: {primary[1]['count']}"
                            )
                            self.status_var.set(
                                f"Scanning... {total_packets} Pakete empfangen"
                            )
                
                except Exception as e:
                    pass  # Ignoriere Fehler bei einzelnen Paketen
            
            # Starte das Sniffing
            sniff(
                iface=interface,
                prn=packet_handler,
                store=0,
                stop_filter=lambda x: not self.is_scanning
            )
            
        except PermissionError:
            self.root.after(0, lambda: messagebox.showerror(
                "Fehler",
                "Keine Berechtigung zum Sniffing auf diesem Interface!\n"
                "Bitte als Administrator ausführen."
            ))
            self.root.after(0, self.stop_scan)
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                "Fehler",
                f"Fehler beim Sniffing:\n{str(e)}"
            ))
            self.root.after(0, self.stop_scan)
    
    def update_display(self):
        """Aktualisiert die Anzeige mit der primären MAC-Adresse"""
        if self.primary_mac:
            self.mac_value.config(
                text=self.primary_mac.upper(),
                fg="#27ae60"
            )
            
            if self.primary_ip:
                self.ip_value.config(text=self.primary_ip)
            else:
                self.ip_value.config(text="Keine IP ermittelt")
            
            # OUI anzeigen (erste 3 Oktette)
            oui = self.primary_mac[:8].upper()
            self.vendor_value.config(text=oui)
        
    def is_admin(self):
        """Prüfen ob das Programm mit Admin-Rechten läuft"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except Exception:
            return False


def main():
    """Hauptfunktion"""
    root = tk.Tk()
    app = NetworkSnifferGUI(root)
    
    # Programm-Icon setzen (optional)
    try:
        root.iconbitmap(default='icon.ico')
    except:
        pass
    
    root.mainloop()


if __name__ == "__main__":
    main()
