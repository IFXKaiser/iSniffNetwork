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
