## 🚀 Installation

The **pbk** framework is hosted on a Launchpad PPA. Choose the method below that best fits your system.

### **Option A: Automated (Recommended for Ubuntu/Linux Mint)**
If you are on a standard Ubuntu-based distribution, run these commands:

```bash
sudo add-apt-repository ppa:prest0nn/pbk
sudo apt update
sudo apt install python3-pbk
```

### **Option B: Manual Installation (Kali Linux / Debian)**

If `add-apt-repository` crashes or if you are using Kali/Debian, use these steps to manually add the PPA and its security key.

1. **Import the GPG Signing Key**
   This allows your system to verify the authenticity of the packages.
   ```bash
   curl -s "[https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x6B927541334175BF988C0836EB1A50B6A797B52B](https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x6B927541334175BF988C0836EB1A50B6A797B52B)" | sudo gpg --dearmor -o /usr/share/keyrings/pbk-ppa.gpg
   ```
 2.  Add the Repository & Link the Key
This creates a source file that points to the repository and uses the key downloaded above.
```bash
echo "deb [signed-by=/usr/share/keyrings/pbk-ppa.gpg] [https://ppa.launchpadcontent.net/prest0nn/pbk/ubuntu](https://ppa.launchpadcontent.net/prest0nn/pbk/ubuntu) noble main" | sudo tee /etc/apt/sources.list.d/pbk.list
```

3. Install the Framework
   ```bash
   sudo apt update && sudo apt install python3-pbk
   ```
