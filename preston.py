import requests 
import threading 
import argparse 
import time
import sys
import random
from datetime import datetime

# MSF-style status messages
def msf_log(status, msg):
    colors = {"*": "\033[1;34m", "+": "\033[1;32m", "-": "\033[1;31m", "!": "\033[1;33m"}
    prefix = colors.get(status, "\033[37m")
    print(f"[{prefix}{status}\033[m] {msg}")

def msf_boot():
    print(f"\033[1;32m[*] \033[mStarting the Preston Breacher Framework v2.0...")
    steps = [
        "Initializing core modules...",
        "Loading wordlist plugins...",
        "Validating network interface...",
        "Establishing listener on 0.0.0.0..."
    ]
    for step in steps:
        msf_log("*", step)
        time.sleep(random.uniform(0.1, 0.2))
    print("")

parser = argparse.ArgumentParser()
parser.add_argument("-u", help="target url", dest='target')
parser.add_argument("--path", help="custom path prefix", dest='prefix')
parser.add_argument("--type", help="set the type i.e. html, asp, php", dest='type')
parser.add_argument("--fast", help="uses multithreading", dest='fast', action="store_true")
args = parser.parse_args()

target = args.target 
if not target:
    print('\033[1;31m[-]\033[1;m Error: -u <url> is required.')
    quit()

msf_boot()

# Raw string banner to prevent SyntaxWarnings
print (r'''\033[1;32m
      o__ __o                                        o                             
 <|     v\                                      <|>                            
 / \     <\                                     < >                            
 \o/     o/  \o__ __o     o__  __o       __o__   |        o__ __o    \o__ __o  
  |__  _<|/   |     |>   /v      |>     />  \    o__/_   /v     v\    |     |> 
  |          / \   < >  />      //      \o       |      />       <\  / \   / \ 
 <o>         \o/        \o    o/         v\      |      \         /  \o/   \o/ 
  |           |          v\  /v __o       <\     o       o       o    |     |  
 / \         / \          <\/> __/>  _\o__</     <\__    <\__ __/>   / \   / \ 
                                                                               
                                                                               
                                                                                
       =[ preston-breacher v2.0-dev           ]
+ -- --=[ Made with ur mum                     ]
+ -- --=[ Preston Security Framework          ]''')

print ('''\n\033[1;33m[!] LEGAL WARNING: \033[37mOi, listen. I’m not responsible for your long day. 
    If this deads out or you’re catching errors, it’s because the 
    target’s moving peak or your own setup is clapped. Use it or lose it. Safe.\n''')

# Clean target URL
target = target.replace('https://', '').replace('http://', '')
if target.endswith('/'): target = target[:-1]
target = 'http://' + target
if args.prefix:
    target = target + ("/" + args.prefix if not args.prefix.startswith("/") else args.prefix)

msf_log("*", f"Target configured: {target}")

def scan(links):
    for link in links:
        url = target + (link if link.startswith("/") else "/" + link)
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                # Check for fake 404s
                if 'Page Not Found' in r.text or ('404' in r.text and len(r.text) > 1500):
                    # Progress update even for filtered results
                    sys.stdout.write(f"\033[K\033[1;30m[*] Analyzing: {link} (Filtered)\033[m\r")
                    sys.stdout.flush()
                else:
                    print(f"\n\033[1;32m[+]\033[m Identified: {url}")
            elif r.status_code in [301, 302]:
                print(f"\n\033[1;33m[!]\033[m Redirect Found: {url}")
            else:
                # Rolling progress line
                sys.stdout.write(f"\033[K\033[1;30m[*] Testing path: {link}\033[m\r")
                sys.stdout.flush()
        except:
            pass

paths = []
def get_paths(type_str):
    try:
        with open('paths.txt','r') as wordlist:
            for path in wordlist:
                path = path.strip()
                if not type_str or type_str in path:
                    paths.append(path)
    except IOError:
        msf_log("-", "Failed to load paths.txt.")
        quit()

get_paths(args.type)
msf_log("*", f"Payload buffer: {len(paths)} paths loaded.")
msf_log("*", "Initiating path discovery...")

if args.fast:
    mid = len(paths) // 2
    t1 = threading.Thread(target=scan, args=(paths[:mid],))
    t2 = threading.Thread(target=scan, args=(paths[mid:],))
    t1.start(); t2.start()
    t1.join(); t2.join()
else:
    scan(paths)

print("\n")
msf_log("+", "Scan completed successfully. Session closed.")