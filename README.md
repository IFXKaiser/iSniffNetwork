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
