# iSniffNetwork 🔍

A simple Windows tool for reading MAC addresses of directly connected network devices.

## 📋 Description

**iSniffNetwork** is a network sniffer with a graphical user interface, specifically developed to read MAC addresses of devices directly connected to your computer via LAN cable.

### Use Case

Do you have devices without a screen, mouse, or keyboard that need to be integrated into the network? Do you need their MAC address for a whitelist? Simply connect the device to your laptop via LAN cable, start **iSniffNetwork**, and read the MAC address!

## ✨ Features

- 🖥️ **Intuitive GUI** - Easy-to-use graphical interface with tkinter
- 🔌 **Intelligent Adapter Selection** - Shows all network adapters (even inactive ones)
- 🎯 **Smart Filtering** - Automatically filters out all your own MAC addresses
- 🔍 **Real-time Scanning** - Live detection of MAC addresses from connected devices
- 📊 **Clear Display** - Shows MAC address, IP address, and OUI (Vendor Prefix)
- 🔄 **Auto-Refresh** - Adapter list can be refreshed at any time
- ⚡ **Fast & Reliable** - Based on Scapy for professional packet sniffing
- 🌐 **Platform Independent** - Detects devices with any OS (Windows, Linux, Mac, IoT)

## 🚀 Installation

### Prerequisites

- **Windows 10/11**
- **Python 3.7 or higher**
- **Administrator rights** (required for packet sniffing)

### Step-by-Step Installation

1. **Clone or download repository:**
   ```bash
   git clone https://github.com/yourusername/iSniffNetwork.git
   cd iSniffNetwork
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or manually:
   ```bash
   pip install scapy psutil
   ```

## 🎯 Usage

### Start via Batch File (Recommended)

Double-click `start.bat` - the script:
- Checks if Python is installed
- Automatically installs missing dependencies
- Starts the program with admin rights

### Manual Start

```bash
python isniff.py
```

**Important:** The program must be run as administrator!

### How to Use

1. **Select Network Adapter**
   - Select the adapter from the dropdown menu where your device is connected
   - Inactive adapters (without cable) are also shown and marked with `[INAKTIV]`
   - Click "🔄 Adapter aktualisieren" to refresh the list

2. **Start Scan**
   - Click "▶ Scan starten"
   - The program now listens on the selected adapter
   - The status bar shows how many own MACs are being filtered

3. **Connect Device**
   - Connect your device via LAN cable (even after scan has started)
   - The MAC address is automatically detected and displayed
   - OUI (Vendor Prefix) and IP address (if available) are also shown

4. **Stop Scan**
   - Click "⏹ Scan stoppen" when finished

## 🛠️ Technical Details

- **GUI Framework:** tkinter (Python Standard Library)
- **Packet Sniffing:** Scapy
- **Network Interfaces:** psutil
- **Platform:** Windows (with admin rights)
- **Python Version:** 3.7+

### How Does It Work?

The tool uses **Scapy** to analyze network packets on the selected interface. It:

1. **Creates Interface Mapping** between Windows names and Scapy interface names
2. **Collects All Local MAC Addresses** from your own network adapters
3. **Automatically Filters** broadcast, multicast, and own MAC addresses
4. **Analyzes Ethernet Layer** of every received packet
5. **Identifies the Main Device** based on packet count

This way, only MAC addresses of **actually connected devices** are detected!

## ⚠️ Important Notes

- **Admin Rights Required:** Packet sniffing requires elevated privileges on Windows
- **Windows Firewall:** You may need to allow Python in the firewall
- **Npcap/WinPcap Required:** Scapy requires a packet capture driver
  - Download: https://npcap.com/
  - During installation: Enable "WinPcap API-compatible Mode"
- **Legal Use Only:** Use this tool only on your own devices and networks!

## 🐛 Troubleshooting

### "No Permission for Sniffing"
→ Start the program as administrator (via `start.bat` or right-click → Run as administrator)

### "Npcap Not Found"
→ Install Npcap from https://npcap.com/
→ Important: Enable "WinPcap API-compatible Mode" during installation

### "Interface Not Found" or Adapter Not Displayed
→ **Fixed in current version!** Automatic interface mapping implemented
→ Click "🔄 Adapter aktualisieren"
→ Inactive adapters (without cable) are now also displayed

### "No Adapters Found"
→ Check if your network adapters are enabled in Windows
→ Make sure Npcap is installed correctly

### No MAC Address Detected
→ Ensure the connected device is powered on
→ Some devices only send packets during network setup - try restarting the device
→ Wait a few seconds after plugging in

### Own MAC Address Displayed (USB Adapter etc.)
→ **Fixed in current version!** Automatic filtering of all local MAC addresses
→ The status bar shows how many own MACs are being filtered

### Does This Tool Only Work With Windows Devices?
→ **No!** The tool is independent of the connected device's operating system
→ It analyzes Layer-2 packets (Ethernet) that every network device sends
→ Works with: Windows, Linux, macOS, Raspberry Pi, IoT devices, routers, etc.

## 📝 License

This project is licensed under the MIT License. See `LICENSE` file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 🌍 Languages

- [🇩🇪 Deutsch](README.md)
- 🇬🇧 English (this file)

---

**Note:** This tool is intended for legal purposes only. Use it only on networks and devices you have permission to access.






_______________________________________________________________________________________________________________________________________________________

# iSniffNetwork 🔍

Ein einfaches Windows-Tool zum Auslesen von MAC-Adressen direkt angeschlossener Netzwerkgeräte.

## 📋 Beschreibung

**iSniffNetwork** ist ein Network Sniffer mit grafischer Benutzeroberfläche, der speziell dafür entwickelt wurde, MAC-Adressen von Geräten auszulesen, die direkt per LAN-Kabel an deinen Computer angeschlossen sind.

### Anwendungsfall

Du hast Geräte ohne Bildschirm, Maus oder Tastatur, die du ins Netzwerk integrieren musst? Du benötigst deren MAC-Adresse für eine Whitelist? Einfach das Gerät per LAN-Kabel an deinen Laptop anschließen, **iSniffNetwork** starten und die MAC-Adresse auslesen!

## ✨ Features

- 🖥️ **Intuitive GUI** - Einfach zu bedienende grafische Oberfläche mit tkinter
- 🔌 **Intelligente Adapter-Auswahl** - Zeigt alle Netzwerkadapter (auch inaktive)
- 🎯 **Smart Filtering** - Filtert automatisch alle eigenen MAC-Adressen heraus
- 🔍 **Echtzeit-Scanning** - Live-Erkennung von MAC-Adressen verbundener Geräte
- 📊 **Übersichtliche Ausgabe** - Zeigt MAC-Adresse, IP-Adresse und OUI (Vendor Prefix)
- 🔄 **Auto-Refresh** - Adapter-Liste kann jederzeit aktualisiert werden
- ⚡ **Schnell & Zuverlässig** - Basiert auf Scapy für professionelles Packet Sniffing
- 🌐 **Plattformunabhängig** - Erkennt Geräte mit jedem Betriebssystem (Windows, Linux, Mac, IoT)

## 🚀 Installation

### Voraussetzungen

- **Windows 10/11**
- **Python 3.7 oder höher**
- **Administrator-Rechte** (für Packet Sniffing erforderlich)

### Schritt-für-Schritt Installation

1. **Repository klonen oder herunterladen:**
   ```bash
   git clone https://github.com/yourusername/iSniffNetwork.git
   cd iSniffNetwork
   ```

2. **Dependencies installieren:**
   ```bash
   pip install -r requirements.txt
   ```

   Oder manuell:
   ```bash
   pip install scapy psutil
   ```

## 🎯 Verwendung

### Starten per Batch-Datei (Empfohlen)

Doppelklick auf `start.bat` - das Skript:
- Prüft ob Python installiert ist
- Installiert fehlende Dependencies automatisch
- Startet das Programm mit Admin-Rechten

### Manueller Start

```bash
python isniff.py
```

**Wichtig:** Das Programm muss als Administrator ausgeführt werden!

### Bedienung

1. **Netzwerkadapter auswählen**
   - Wähle aus dem Dropdown-Menü den Adapter aus, an dem dein Gerät angeschlossen ist
   - Auch inaktive Adapter (ohne Kabel) werden angezeigt und sind mit `[INAKTIV]` markiert
   - Klicke auf "🔄 Adapter aktualisieren" um die Liste zu erneuern

2. **Scan starten**
   - Klicke auf "▶ Scan starten"
   - Das Programm lauscht nun auf dem ausgewählten Adapter
   - In der Statusleiste siehst du wie viele eigene MACs gefiltert werden

3. **Gerät einstecken**
   - Schließe dein Gerät per LAN-Kabel an (auch nach dem Scan-Start möglich)
   - Die MAC-Adresse wird automatisch erkannt und angezeigt
   - OUI (Vendor Prefix) und IP-Adresse (falls verfügbar) werden ebenfalls angezeigt

4. **Scan stoppen**
   - Klicke auf "⏹ Scan stoppen" wenn du fertig bist

```

## 🛠️ Technische Details
psutil
- **Plattform:** Windows (mit Admin-Rechten)
- **Python-Version:** 3.7+

### Wie funktioniert es?

Das Tool verwendet **Scapy** um Netzwerkpakete auf dem ausgewählten Interface zu analysieren. Es:

1. **Erstellt Interface-Mapping** zwischen Windows-Namen und Scapy-Interface-Namen
2. **Sammelt alle lokalen MAC-Adressen** von deinen eigenen Netzwerkadaptern
3. **Filtert automatisch** Broadcast, Multicast und eigene MAC-Adressen
4. **Analysiert Ethernet-Layer** jedes empfangenen Pakets
5. **Identifiziert das Hauptgerät** anhand der Paketanzahl unter Windows
- **Windows Firewall:** Eventuell musst du Python in der Firewall erlauben
- **Npcap/WinPcap erforderlich:** Scapy benötigt einen Packet-Capture-Treiber
  - Download: https://npcap.com/
  - Während der Installation: "WinPcap API-compatible Mode" aktivieren
- **Nur für legale Zwecke:** Nutze das Tool nur auf eigenen Geräten und Netzwerken!
### Wie funktioniert es?

Das Tool verwendet **Scapy** um Netzwerkpakete auf dem ausgewählten Interface zu sniffing. Es analysiert den Ethernet-Layer jedes Pakets und extrahiert die Source-MAC-Adresse. Broadcast- und Multicast-Adressen werden automatisch gefiltert.

## ⚠️ Wichtige Hinweise

- **Admin-Rechte erforderlich:** Packet Sniffing benötigt erhöhte Rechte
- **Windows Firewall:** Eventuell musst du Python in der Firewall erlauben
- **Npcap/WinPcap:** Scapy benötigt einen Packet-Capture-Treiber. Falls noch nicht installiert, wird Scapy dich beim ersten Start darauf hinweisen. Download: https://npcap.com/

## 🐛 Troubleshooting (via `start.bat` oder Rechtsklick → Als Administrator ausführen)

### "Npcap nicht gefunden"
→ Installiere Npcap von https://npcap.com/
→ Wichtig: "WinPcap API-compatible Mode" während Installation aktivieren

### "Interface not found" oder Adapter wird nicht angezeigt
→ **Behoben in aktueller Version!** Automatisches Interface-Mapping implementiert
→ Klicke auf "🔄 Adapter aktualisieren"
→ Auch inaktive Adapter (ohne Kabel) werden jetzt angezeigt

### "Keine Adapter gefunden"
→ Prüfe ob deine Netzwerkadapter in Windows aktiviert sind
→ Stelle sicher, dass Npcap korrekt installiert ist

### Keine MAC-Adresse erkannt
→ Stelle sicher, dass das angeschlossene Gerät eingeschaltet ist
→ Manche Geräte senden erst Pakete beim Netzwerkaufbau - versuche das Gerät neu zu starten
→ Warte ein paar Sekunden nach dem Einstecken

### Eigene MAC-Adresse wird angezeigt (USB-Adapter etc.)
→ **Behoben in aktueller Version!** Automatische Filterung aller lokalen MAC-Adressen
→ In der Statusleiste siehst du wie viele eigene MACs gefiltert werden

### Funktioniert das Tool nur mit Windows-Geräten?
→ **Nein!** Das Tool ist unabhängig vom Betriebssystem des angeschlossenen Geräts
→ Es analysiert Layer-2-Pakete (Ethernet), die jedes Netzwerkgerät sendet
→ Funktioniert mit: Windows, Linux, macOS, Raspberry Pi, IoT-Geräten, Routern, etc.
### Funktioniert das Tool nur mit Windows-Geräten?
→ **Nein!** Das Tool funktioniert unabhängig vom Betriebssystem des angeschlossenen Geräts
Contributions are welcome! Feel free to open issues or submit pull requests.

## 🌍 Languages

- 🇩🇪 Deutsch (diese Datei)
- [🇬🇧 English](README_EN.md
Beiträge sind willkommen! Öffne gerne Issues oder Pull Requests.


## 📚 Weitere Ressourcen

- [Scapy Dokumentation](https://scapy.readthedocs.io/)
- [Python tkinter Tutorial](https://docs.python.org/3/library/tkinter.html)
- [MAC-Adresse Vendor Lookup](https://www.macvendorlookup.com/)

---

**Hinweis:** Dieses Tool ist nur für legale Zwecke gedacht. Nutze es nur auf Netzwerken und Geräten, für die du die Berechtigung hast.
