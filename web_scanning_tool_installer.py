import subprocess
import os
import sys

def install_tools():
    # Tools ki list jo humein website testing aur bug hunting ke liye chahiye
    # Format: {"Tool Name": "Package Name"}
    tools = {
        "Nmap": "nmap",
        "Nikto": "nikto",
        "SQLMap": "sqlmap",
        "Dirb": "dirb",
        "Wapiti": "wapiti",
        "theHarvester": "theharvester",
        "Dmitry": "dmitry"
    }

    print("--- [ Abdul Mateen Tool: Requirements Installer ] ---")
    
    # OS Check (Sirf Linux/Kali par kaam karega)
    if os.name == 'nt':
        print("[!] Error: Yeh installer sirf Linux/Kali par chalega.")
        return

    # Update system repositories pehle
    print("[*] Updating package list... Please wait.")
    subprocess.run("sudo apt update -y", shell=True)

    for tool_name, package in tools.items():
        # Check karna ke tool pehle se install hai ya nahi
        check_tool = subprocess.run(f"which {package}", shell=True, capture_output=True)
        
        if check_tool.returncode == 0:
            print(f"[✓] {tool_name} is already installed.")
        else:
            print(f"[*] {tool_name} not found. Installing...")
            try:
                # Tool install karne ki command
                subprocess.run(f"sudo apt install {package} -y", shell=True, check=True)
                print(f"[+] Successfully installed {tool_name}.")
            except subprocess.CalledProcessError:
                print(f"[X] Failed to install {tool_name}. Manual install may be needed.")

    print("\n[!] All tools are configured. You are ready to go, Abdul Mateen!")

# Installer ko run karne ke liye
if __name__ == "__main__":
    # Root check taake sudo baar baar na mangna pare
    if os.geteuid() != 0:
        print("[!] Please run this script with sudo: 'sudo python3 installer.py'")
    else:
        install_tools()