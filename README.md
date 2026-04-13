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

   <img width="1440" height="900" alt="Screenshot 2026-04-13 at 4 48 53 AM" src="https://github.com/user-attachments/assets/a2281052-4d69-4abc-b5ca-fd156285949a" />

   
<img width="1440" height="900" alt="Screenshot 2026-04-13 at 4 52 03 AM" src="https://github.com/user-attachments/assets/6c7af48b-02de-4a3a-9268-5feb200d478f" />



<img width="1440" height="900" alt="Screenshot 2026-04-13 at 4 49 42 AM" src="https://github.com/user-attachments/assets/dfc42343-c595-4cec-937e-347d1c76dd6a" />
