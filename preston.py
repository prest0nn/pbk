#!/usr/bin/env python3
import requests 
import threading 
import argparse 
import time
import sys
import random
import os
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

def scan(target, links):
    for link in links:
        url = target + (link if link.startswith("/") else "/" + link)
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                if 'Page Not Found' in r.text or ('404' in r.text and len(r.text) > 1500):
                    sys.stdout.write(f"\033[K\033[1;30m[*] Analyzing: {link} (Filtered)\033[m\r")
                    sys.stdout.flush()
                else:
                    print(f"\n\033[1;32m[+]\033[m Identified: {url}")
            elif r.status_code in [301, 302]:
                print(f"\n\033[1;33m[!]\033[m Redirect Found: {url}")
            else:
                sys.stdout.write(f"\033[K\033[1;30m[*] Testing path: {link}\033[m\r")
                sys.stdout.flush()
        except:
            pass

def main():
    # 1. HELP BANNER - The Block Art (Shows when user types just 'pbk')
    help_banner = r'''
                                   ▏                                   
                                   ▏▍▏▍▅▁▋▏▏▏▏▋▆▅▋▏▏▏▏▌▃▅▎▏▍                      
                               ▌▉▋▊▃▂▅███▆▂▄▃▃▇██▇▄▅▆▇████▇█▅▊▊▉▎                  
                             ▏▏▉▅▄▇██▆▄▄▆▄▄▃▉▊▊▊▊▊▊▊▉▉▄▄▅▇███████▇▋▏▏▏             
                           ▌▃▄▄▄▅▇▆▅▂▂▍▍▎▎▎▎▎▏▏▎▎▎▎▏▎▎▎▎▎▍▌▌▂▄█████▇▇▇▍            
                         ▏▎▍▉██▇▆▅▁▌▏▏▏▏▏▏▏▏▏▎▏▏▏▎▎▏▎▎▎▎▏▎▎▍▍▎▍▎▊▃█████▋▍▎▏         
                        ▏▅▄▇█▆▇▄▌▏▏▏ ▏▏ ▏▏▏▏▏▏▏▏▏▏▏▏▎▎▎▎▎▎▎▍▎▎▎▎▍▎▍▌▄█████▂         
                        ▎▊▉▆▆▇█▆▌▏▎▏  ▏▏▏▏▏ ▏▏▏▏▏▎▎▎▎▏▎▎▎▎▎▍▍▍▍▎▍▎▍▍▍▍▎▋▆███▆▁▉▏         
                        ▎▋▅▇█▅▅▂▎▏▏▏▏▏  ▏▏▏▏▏▏▏▎▏▏▎▏▎▎▏▍▎▎▎▎▍▍▎▍▎▎▎▎▎▎▍▎▎▎▃█████▊▏         
                        ▎▃▄▅▅▆▇▁▎▎▎▏▎▏▏ ▏▏▏▏▏▏▏▏▎▏▏▎▎▎▎▎▎▍▎▍▎▍▍▍▍▍▍▎▍▍▍▍▎▍▍▍▂█████▃▏        
                       ▏▋▂▆█▇▄▁▎▎▎▎▏▎▎▎▎▎▎▍▎▎▎▍▍▍▍▎▍▍▍▍▎▍▌▍▍▎▌▍▍▍▍▍▍▍▍▍▍▎▌▌▍▍▁████▅▋▏      
                       ▏▉▅▆▃▆▂▎▏▎▎▎▏▎▎▎▍▊▂▉▎▎▍▍▎▎▎▏▎▎▎▍▏▎▎▎▍▎▍▍▍▍▋▃▊▊▌▌▎▍▍▍▎▎▍▅████▉▏      
                       ▊▄▅▅▄▆▎▍▎▍▎▍▎▌▊▃▂▊▍▋▌▍▎▍▎▍▎▍▎▍▎▎▎▍▍▎▎▍▌▍▍▎▍▍▌▌▋▋▊▂▄▃▋▌▌▍▍▍▌▍████▆▊      
                       ▎▉▄▃▃▂▎▎▎▍▎▎▏▎▎▎▎▎▎▎▎▎▍▍▎▎▎▂▆▆▎▎▄▅▄▍▎▎▍▍▍▍▍▍▍▍▍▌▋▌▌▍▍▍▍▍▄███▉▏      
                        ▏▄▂▄▋▎▎▎▍▍▍▎▍▍▍▎▍▍▍▍▎▍▍▍▍▍██▃▎▍▃██▋▍▍▍▍▌▌▍▌▍▍▍▌▊▉▊▌▍▍▌▌▊██▆▏       
                       ▍▂▆▆▅▋▎▍▎▍▍▎▋▂▌▎▎▍▍▍▎▍▍▍▍▎▍▁▃▍▍▍▍▂▉▋▎▎▍▍▍▍▍▌▍▍▍▋▂▋▌▉▋▌▋▌▊███▃▍      
                       ▊▃▅▇▅▌▎▎▎▍▎▎▇▂▍▎▎▍▍▍▎▍▍▍▎▎▎▎▎▎▍▍▎▎▍▍▎▎▍▍▍▍▎▍▌▍▍▍▂█▌▌▍▍▍▍▊███▆▊      
                        ▏▅▃▆▌▎▍▎▌▍▎▍▇█▃▍▍▍▍▎▍▎▍▍▍▎▎▍▍▍▍▎▍▍▍▍▎▍▌▌▌▍▌▍▌▃█▆▊▌▌▌▌▋▌▉██▇▏       
                        ▏▋▆▃▅▉▎▎▎▍▎▍▎▍▂██▆▉▊▍▍▎▍▍▎▎▎▎▍▍▍▎▎▍▍▍▎▎▍▍▍▉▁▇██▃▌▍▌▌▌▍▌▍▁██▇▋▏     
                       ▊▄▃▅▇▅▎▎▎▍▎▎▍▎▍▍▊▃█████▄▂▌▋▍▍▎▍▎▍▎▍▌▌▋▋▂▅█████▃▊▌▌▍▌▌▌▍▌▍████▇▊      
                        ▍▇█▆▅▁▍▎▍▍▎▎▍▍▍▎▌▁▅██████▇▅▅▅▅▆▅▆▅▇██████▅▂▋▌▋▊▌▌▊▋▋▌▋▃████▍       
                       ▎▂▄▃▆▆▅▊▎▎▎▎▎▎▎▍▎▍▍▌▌▉▃▇▇█████████████▇▃▉▋▍▍▍▍▍▍▍▌▌▌▌▍▁█████▃▏      
                        ▏▉█▇▅▆▄▊▍▍▍▎▍▍▍▎▍▍▌▍▌▍▌▍▊▁▄▄▄▅▅▅▄▅▁▉▍▌▋▋▋▌▋▌▌▋▋▊▌▋▊▌▁█████▉▏       
                        ▎▂▅▇▇██▇▉▎▎▎▍▍▍▎▍▎▍▎▍▍▍▍▎▍▍▌▍▍▌▍▍▌▍▌▍▍▋▌▌▌▌▍▌▋▋▌▋▌▍▁█████▆▂▏       
                          ▍███▅▅█▃▍▎▍▍▍▎▌▍▍▎▍▍▍▍▎▍▍▍▍▌▌▍▍▌▌▌▌▌▌▌▊▌▌▌▌▌▌▍▍▋▆██████▎        
                          ▏▋▊▇████▇▂▌▎▍▍▍▍▍▍▍▍▍▍▍▌▍▍▌▋▌▍▍▋▌▌▌▌▌▋▌▍▌▌▋▌▍▌▃▇████▆▉▋▏        
                            ▏▇███████▇▉▌▍▍▍▍▎▍▍▍▍▌▌▍▌▌▍▍▍▋▍▌▍▍▌▌▌▍▍▍▋▉▆███████▄            
                              ▋▁▁▃███████▇▁▁▍▎▍▍▍▌▌▌▍▋▌▌▍▌▌▌▋▌▌▌▍▌▁▃▆███████▂▂▁▍            
                                ▎▃▃▃▇████████▆▃▃▂▊▊▊▊▊▋▋▊▊▊▂▃▄▆████████▆▃▃▃▏                
                                    ▏▂▂▉▂▇████████▇███████▇▇██████▇▂▁▂▁▏                  
                                      ▎▋▏▌▆▁▎▏▏▏▎▁██▂▍▏ ▏▎▁▇▌▏▊▎                      
                                                  ▎▎        ▏                            
    '''

    # 2. SCAN BANNER - The Preston Breacher (Shows when starting a scan)
    scan_banner = r'''\033[1;32m
          o__ __o                                        o                             
     <|     v\\                                      <|>                            
     / \\     <\\                                     < >                            
     \\o/     o/  \\o__ __o     o__  __o       __o__   |        o__ __o    \\o__ __o  
      |__  _<|/   |     |>   /v      |>     />  \\    o__/_   /v     v\\    |     |> 
      |          / \\   < >  />      //      \\o       |      />       <\\  / \\   / \\ 
     <o>         \\o/        \\o    o/         v\\      |      \\         /  \\o/   \\o/ 
      |           |          v\\  /v __o       <\\     o       o       o    |     |  
     / \\         / \\          <\\/> __/>  _\\o__</     <\\__    <\\__ __/>   / \\   / \\ 

           =[ preston-breacher v2.0-dev           ]
           =[ Usage: pbk -u <url> [options]       ]\033[0m'''

    parser = argparse.ArgumentParser(
        description="Preston Breacher Framework - Admin Panel Finder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        add_help=True
    )
    parser.add_argument("-u", help="Target URL (e.g. http://example.com)", dest='target')
    parser.add_argument("--path", help="Custom path prefix", dest='prefix')
    parser.add_argument("--type", help="Set type (html, asp, php)", dest='type')
    parser.add_argument("--fast", help="Use multithreading", dest='fast', action="store_true")

    # Show help banner if no arguments are provided
    if len(sys.argv) == 1:
        print(help_banner)
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    if args.target:
        print(scan_banner)
        msf_boot()

        print ('''\n\033[1;33m[!] LEGAL WARNING: \033[37mOi, listen. I’m not responsible for your long day. 
        If this deads out or you’re catching errors, it’s because the 
        target’s moving peak or your own setup is clapped. Use it or lose it. Safe.\n''')

        # Target Cleaning
        target = args.target.replace('https://', '').replace('http://', '')
        if target.endswith('/'): target = target[:-1]
        target = 'http://' + target
        if args.prefix:
            target = target + ("/" + args.prefix if not args.prefix.startswith("/") else args.prefix)

        msf_log("*", f"Target configured: {target}")

        # Path discovery for wordlist
        base_path = os.path.dirname(os.path.abspath(__file__))
        wordlist_path = os.path.join(base_path, 'paths.txt')

        if not os.path.exists(wordlist_path):
            msf_log("-", "Critical: 'paths.txt' not found inside the package folder.")
            sys.exit(1)

        paths = []
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                for path in wordlist:
                    path = path.strip()
                    if path and (not args.type or args.type in path):
                        paths.append(path)
        except Exception as e:
            msf_log("-", f"Error reading wordlist: {e}")
            sys.exit(1)

        msf_log("*", f"Payload buffer: {len(paths)} paths loaded.")
        msf_log("*", "Initiating path discovery...")

        if args.fast:
            mid = len(paths) // 2
            t1 = threading.Thread(target=scan, args=(target, paths[:mid],))
            t2 = threading.Thread(target=scan, args=(target, paths[mid:],))
            t1.start(); t2.start()
            t1.join(); t2.join()
        else:
            scan(target, paths)

        print("\n")
        msf_log("+", "Scan completed successfully. Session closed.")

if __name__ == "__main__":
    main()
