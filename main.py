#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def banner():
    os.system("clear" if os.name == 'posix' else "cls")
    print(f"""{CYAN}
    ╔══════════════════════════════════════════════════╗
    ║          WOLFER WEB CLONER & EXTRACTOR           ║
    ║     [+] Target: All Code & 3D/Media Assets       ║
    ║     [+] Author: Algriom / Wolfer Tools             ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")

def clone_website(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc.replace(".", "_")
    output_dir = f"cloned_{domain_name}"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        os.makedirs(os.path.join(output_dir, "assets"))

    print(f"{YELLOW}[*] Connecting to target: {url}{RESET}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code != 200:
            print(f"{RED}[-] Failed to connect. Status Code: {response.status_code}{RESET}")
            return

        html_path = os.path.join(output_dir, "index.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"{GREEN}[+] Saved: index.html{RESET}")

        soup = BeautifulSoup(response.text, 'html.parser')
        
        resources = {
            'script': 'src',
            'link': 'href',
            'img': 'src',
            'source': 'src',
            'video': 'src',
            'audio': 'src'
        }

        downloaded_files = set()

        for tag_name, attr in resources.items():
            for elem in soup.find_all(tag_name):
                file_url = elem.get(attr)
                if file_url:
                    absolute_url = urljoin(url, file_url)
                    parsed_file_url = urlparse(absolute_url)
                    file_name = os.path.basename(parsed_file_url.path)
                    
                    if not file_name or file_name in downloaded_files:
                        continue
                        
                    downloaded_files.add(file_name)
                    
                    valid_extensions = ('.html', '.css', '.js', '.glb', '.gltf', '.fbx', '.xml', '.py', '.php', '.json', '.png', '.jpg', '.jpeg', '.svg')
                    
                    if file_name.lower().endswith(valid_extensions):
                        try:
                            file_data = requests.get(absolute_url, headers=headers, timeout=10).content
                            file_path = os.path.join(output_dir, "assets", file_name)
                            with open(file_path, "wb") as f:
                                f.write(file_data)
                            print(f"{GREEN}[+] Downloaded Asset: {file_name}{RESET}")
                        except Exception:
                            print(f"{RED}[-] Skipped (Failed): {file_name}{RESET}")

        print(f"\n{CYAN}[✔] Cloning Completed Successfully!{RESET}")
        print(f"{CYAN}[✔] All files saved inside directory: {output_dir}{RESET}")

    except Exception as e:
        print(f"{RED}[-] An error occurred: {e}{RESET}")

if __name__ == "__main__":
    banner()
    target = input(f"{YELLOW}[?] Enter Website URL (e.g. example.com): {RESET}")
    if target.strip():
        clone_website(target)
    else:
        print(f"{RED}[-] Please enter a valid URL!{RESET}")
