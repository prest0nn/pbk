## 🚀 Installation

The **pbk** framework is hosted on a Launchpad PPA. Choose the method below that best fits your system.

### **Option A: Automated (Recommended for Ubuntu/Linux Mint)**
If you are on a standard Ubuntu-based distribution, run these commands:

```bash
sudo add-apt-repository ppa:prest0nn/pbk
sudo apt update
sudo apt install python3-pbk

### **Manual Installation (Kali Linux / Debian / Power Users)**

Use this method if `add-apt-repository` is unavailable or returns an error. This manually imports the security key and adds the repository source.

**1. Import the GPG Signing Key**
This allows your system to verify the authenticity of the packages.
```bash
curl -s "[https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x6B927541334175BF988C0836EB1A50B6A797B52B](https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x6B927541334175BF988C0836EB1A50B6A797B52B)" | sudo gpg --dearmor -o /usr/share/keyrings/pbk-ppa.gpg
