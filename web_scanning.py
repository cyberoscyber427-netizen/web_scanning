import os
import time
import sys
import subprocess
import re

# Colors
R, G, Y, C, M, W, RESET = '\033[91m', '\033[92m', '\033[93m', '\033[96m', '\033[95m', '\033[97m', '\033[0m'

# --- ABDUL MATEEN'S AI BRAIN ---
class CyberAI:
    def __init__(self):
        # Error patterns aur unke intelligent solutions
        self.error_db = {
            r"403 Forbidden|Access Denied": ("IP_BLOCKED", "Target ne aapka IP block kiya hai. IP rotate ho chuka hai, ab Stealth mode try karein."),
            r"406 Not Acceptable|WAF|Mod_Security|Cloudflare": ("WAF_DETECTED", "WAF Detection! Firewall ne packets drop kiye hain. Fragmentation (-f) ya Decoy (-D) use karein."),
            r"Connection timed out|0 hosts up": ("HOST_DOWN", "Target unreachable hai ya highly secured firewall use kar raha hai."),
            r"429 Too Many Requests": ("RATE_LIMITED", "Scanning speed bohot fast hai. Timing T2 ya T1 use karein."),
            r"401 Unauthorized": ("AUTH_REQUIRED", "Authentication bypass scripts ki zaroorat hai.")
        }

    def analyze_output(self, output):
        for pattern, (error_type, advice) in self.error_db.items():
            if re.search(pattern, output, re.IGNORECASE):
                return error_type, advice
        return None, None

mateen_ai = CyberAI()

def rotate_ip():
    print(f"{Y}[*] AI ACTION: Rotating IP via Tor for Anonymity...{RESET}")
    os.system("sudo service tor restart > /dev/null 2>&1")
    time.sleep(1)
    print(f"{G}[+] IP Changed. New identity established.{RESET}")

def animation():
    os.system('clear')
    name = "   A B D U L   M A T E E N   -   1 0 0   S C A N N I N G   C O M M A N D S   [AI EDITION]"
    for char in name:
        sys.stdout.write(f"{G}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.01)
    print(f"\n{M}" + "="*95 + f"{RESET}")

# --- 100 COMMANDS DATABASE (FULL RESTORED) ---
cmd_list = {
    "1": ("nmap -sS -Pn {t}", "Stealth SYN Scan: Disables ping discovery and uses half-open connections."),
    "2": ("nmap -sV --version-intensity 9 {t}", "Advanced Version Detection: High intensity service identification."),
    "3": ("nmap -O --osscan-guess {t}", "OS Fingerprinting: Aggressive OS stack analysis."),
    "4": ("nmap -f -mtu 8 {t}", "Packet Fragmentation: Splits headers to slip past firewalls/IDS."),
    "5": ("nmap -D RND:20 {t}", "Decoy Scanning: Masks your real IP with 20 random decoys."),
    "6": ("nmap --data-length 128 {t}", "Packet Padding: Adds random data to bypass size-based filters."),
    "7": ("nmap --source-port 53 {t}", "Source Port Spoofing: Mimics DNS traffic to bypass firewall rules."),
    "8": ("nmap --badsum {t}", "Checksum Manipulation: Identifies active IDS systems."),
    "9": ("nmap --script vuln {t}", "Vulnerability Engine: Checks for critical known vulnerabilities."),
    "10": ("nmap -p- -T4 {t}", "Full Port Coverage: Scans all 65,535 ports at high speed."),
    "11": ("nmap --script auth {t}", "Authentication Probe: Targets services with no/default passwords."),
    "12": ("nmap --script brute {t}", "Brute Force Discovery: Auto-guesses common credentials."),
    "13": ("nmap --script default,safe {t}", "Safe Reconnaissance: Gathers info without crashing services."),
    "14": ("nmap --spoof-mac Apple {t}", "MAC Address Spoofing: Appears as an Apple device."),
    "15": ("nmap -sU -p 53,67,123,161 {t}", "UDP Service Scan: Targets DNS, DHCP, SNMP."),
    "16": ("nmap --script http-enum {t}", "Web Directory Enumeration: Finds config and backup folders."),
    "17": ("nmap --script smb-vuln* {t}", "SMB Exploit Check: Checks for EternalBlue/SMBGhost."),
    "18": ("nmap --script ssl-enum-ciphers {t}", "SSL/TLS Audit: Finds weak encryption ciphers."),
    "19": ("nmap --script dns-brute {t}", "DNS Subdomain Discovery: Brute-forces hidden subdomains."),
    "20": ("nmap --script mysql-info {t}", "MySQL Recon: Extracts version and user info."),
    "21": ("nmap --script ftp-anon {t}", "FTP Anonymous Check: Checks for unauthorized logins."),
    "22": ("nmap --script rdp-enum-encryption {t}", "RDP Analysis: Audits Remote Desktop encryption."),
    "23": ("nmap -T1 -sS {t}", "Paranoid Mode: Extreme delays to stay undetected."),
    "24": ("nmap --script http-waf-detect {t}", "WAF Fingerprinting: Detects Cloudflare/Akamai protection."),
    "25": ("nmap --script http-robots.txt {t}", "Robots Scraper: Finds hidden paths from robots.txt."),
    "26": ("nmap --script snmp-brute {t}", "SNMP String Guessing: Finds public/private strings."),
    "27": ("nmap --script vnc-info {t}", "VNC Access Check: Scans for open remote desktops."),
    "28": ("nmap --script whois-domain {t}", "Whois Intelligence: Queries WHOIS for admin data."),
    "29": ("nmap --script http-methods {t}", "HTTP Verb Audit: Checks for PUT, DELETE, TRACE."),
    "30": ("nmap -sT -Pn {t}", "Full TCP Connect: Accurate but more visible port verification."),
    "31": ("nikto -h {t}", "Web Server Vulnerability Scan: Audits 6700+ dangerous files."),
    "32": ("nikto -h {t} -Tuning 4", "SQL Injection Tuning: Focuses specifically on SQLi."),
    "33": ("nikto -h {t} -evasion 1", "WAF Evasion: Random URI encoding."),
    "34": ("sqlmap -u {t} --batch --crawl=2", "Automated SQLi Discovery: Crawls and tests forms."),
    "35": ("sqlmap -u {t} --dbs", "Database Enumeration: Lists all databases."),
    "36": ("sqlmap -u {t} --level=5 --risk=3", "Maximum SQLi Aggression: All injection methods."),
    "37": ("ghauri -u {t} --batch --dbs", "Fast SQLi Recon: Advanced database detection."),
    "38": ("wafw00f {t} -a", "Aggressive WAF Detection: Identifies WAF type."),
    "39": ("whatweb -a 3 {t}", "Technology Profiling: Finds CMS and plugins."),
    "40": ("dirsearch -u {t} -e php,txt,zip,conf,sql,bak", "Hidden File Hunt: Searches for backups."),
    "41": ("ffuf -u {t}/FUZZ -w list.txt -mc 200", "High-Speed Fuzzing: Finds hidden directories."),
    "42": ("gobuster dir -u {t} -w list.txt -t 50", "Multi-Threaded Brute: Rapid folder scanning."),
    "43": ("arjun -u {t} -m GET", "Hidden Parameter Discovery: Finds undocumented params."),
    "44": ("paramspider -d {t} --level high", "Parameter Mining: Scrapes Wayback archives."),
    "45": ("xsstrike -u {t} --crawl", "XSS Warfare: Advanced XSS engine."),
    "46": ("wpscan --url {t} --enumerate vp,vt", "WordPress Audit: Plugin/Theme vulnerabilities."),
    "47": ("joomscan -u {t}", "Joomla Vulnerability Scan: Joomla-specific audit."),
    "48": ("droopescan scan drupal -u {t}", "Drupal Analysis: Scans for Drupalgeddon."),
    "49": ("commix --url {t} --batch", "Command Injection Scanner: RCE vulnerability check."),
    "50": ("subfinder -d {t} -silent", "Subdomain Recon: Uses multiple APIs."),
    "51": ("amass enum -d {t}", "Active Domain Mapping: Deep DNS enumeration."),
    "52": ("assetfinder --subs-only {t}", "Asset Extraction: Scrapes transparency logs."),
    "53": ("sublist3r -d {t} -e google,bing,yahoo", "Search Engine Recon: Scrapes subdomains."),
    "54": ("sslscan --show-certificate {t}", "SSL/TLS Security Audit: Cert expiration and POODLE."),
    "55": ("photon -u {t} -l 3", "Data Crawling: Extracts emails and profiles."),
    "56": ("theharvester -d {t} -b all", "OSINT Data Collection: Harvests emails and names."),
    "57": ("dnsrecon -d {t} -t axfr", "DNS Zone Transfer: Downloads entire DNS records."),
    "58": ("cloudflair -d {t}", "Cloudflare Bypass: Finds real origin IP."),
    "59": ("uniscan -u {t} -qw", "LFI/RFI/RCE Scanner: Web file inclusion audit."),
    "60": ("davtest -url {t}", "WebDAV Exploit Check: Tests unauthorized uploads."),
    "61": ("nmap -sS -f --mtu 16 --data-length 100 {t}", "Ultimate Stealth Suite: Maximum evasion."),
    "62": ("nmap --script http-shellshock {t}", "Shellshock Check: Probes for Bash vulnerability."),
    "63": ("nmap --script http-git {t}", "Exposed Git Repository: Finds leaked source code."),
    "64": ("nmap --script http-internal-ip-disclosure {t}", "Internal IP Disclosure: Forces IP leak."),
    "65": ("nmap --script http-backup-finder {t}", "Sensitive Backup Discovery: Auto-search."),
    "66": ("nmap --script http-wordpress-enum {t}", "WP User Discovery: Enumerate users."),
    "67": ("nmap --script snmp-sysdescr {t}", "SNMP Info Leak: Extract system info."),
    "68": ("nmap --script smtp-commands {t}", "SMTP Audit: Checks user enumeration commands."),
    "69": ("nmap --script rdp-vuln-ms12-020 {t}", "Legacy RDP Check: DoS vulnerability probe."),
    "70": ("nmap --script ftp-vsftpd-backdoor {t}", "Backdoor Detection: VSFTPD 2.3.4 root access."),
    "71": ("dirb {t} -X .php,.sql", "Classic Content Brute: Executables and dumps."),
    "72": ("uniscan -u {t} -d", "Directory Recon: Finds config files."),
    "73": ("clusterd -i {t}", "App Server Recon: Probes JBoss/WebLogic."),
    "74": ("cadaver {t}", "WebDAV Shell Access: Interactive file management."),
    "75": ("fierce --domain {t}", "Recursive DNS Discovery: Non-contiguous scanner."),
    "76": ("hping3 -S -p 80 -c 1 {t}", "Custom TCP Probe: Tests latency and FW."),
    "77": ("fping -g {t}", "Network Range Ping: Finds live hosts fast."),
    "78": ("netdiscover -r {t}", "ARP Discovery: Maps local network."),
    "79": ("masscan -p1-1000 {t} --rate=1000", "Hyper-Fast Port Scan: 1000 pps."),
    "80": ("webtech -u {t}", "Tech Stack Discovery: Lists libraries/frameworks."),
    "81": ("crlfsuite -u {t}", "CRLF Injection Scanner: Session hijacking audit."),
    "82": ("dalfox url {t}", "Modern XSS Fuzzer: DOM-based analysis."),
    "83": ("gau {t} | grep '.js'", "JS File Mining: Finds hidden endpoints/keys."),
    "84": ("waybackurls {t} | grep '.php'", "Wayback PHP Hunter: Recovers old PHP URLs."),
    "85": ("shodan host {t}", "Shodan Intelligence: Queries indexed vulnerabilities."),
    "86": ("recon-ng", "Full Recon Framework: Modular OSINT shell."),
    "87": ("sslscan --tlsall {t}", "Complete TLS Audit: Tests all versions."),
    "88": ("smbmap -H {t}", "SMB Share Permissions: Maps Read/Write access."),
    "89": ("enum4linux {t}", "Deep Windows Recon: Extract users/shares."),
    "90": ("nmap -sV -sC -p 445 {t}", "SMB Safe Scripting: Safe Windows info gathering."),
    "91": ("nmap --script broadcast-dns-service-discovery {t}", "mDNS Discovery: Apple/Linux devices."),
    "92": ("nmap --script http-svn-info {t}", "SVN Metadata Leak: Finds dev history."),
    "93": ("nmap --script http-headers {t}", "Security Header Audit: Checks HSTS/CSP."),
    "94": ("nmap --script banner {t}", "Service Banner Grab: Raw version extraction."),
    "95": ("nmap -Pn -sS -T4 --open {t}", "Fast Active Recon: Only open ports."),
    "96": ("nmap --script dns-brute --dns-brute.threads 10 {t}", "High-Thread DNS Brute."),
    "97": ("nmap --script http-vlc-streamer-info {t}", "VLC Recon: Finds open video feeds."),
    "98": ("nmap --script memcached-info {t}", "Memcached Leak: Checks for plain text data."),
    "99": ("nmap --script redis-info {t}", "Redis Recon: Checks for password-less access."),
    "100": ("nmap -p- --script vuln,safe,discovery {t}", "ABDUL MATEEN'S FINAL BOSS MODE: Deep Discovery."),
}

def run_with_ai(final_cmd, target, detail, choice):
    rotate_ip()
    print(f"\n{M}" + "-"*95)
    print(f"{G}RECON: {W}{detail}{RESET}")
    print(f"{Y}AI ENGINE: Monitoring for blocks and WAF...{RESET}")
    print(f"{M}" + "-"*95 + f"\n")

    # Command Execution with live monitoring
    process = subprocess.Popen(
        f"proxychains4 {final_cmd}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    full_output = ""
    for line in process.stdout:
        print(line, end="")
        full_output += line
    
    process.wait()

    # AI Brain analyzing the result
    err_type, advice = mateen_ai.analyze_output(full_output)
    
    if err_type:
        print(f"\n{R}[!!!] AI DETECTED {err_type}: {advice}{RESET}")
        if err_type == "IP_BLOCKED":
            print(f"{C}[REMEDY] Automated rotation successful. Re-run scan or use Command 004/005.{RESET}")
    else:
        print(f"\n{G}[+] Scan completed. No critical AI flags triggered.{RESET}")

def main():
    if os.geteuid() != 0:
        print(f"{R}[!] ERROR: ROOT privilege required! (sudo python3 filename.py){RESET}")
        sys.exit()

    animation()
    target = input(f"\n{W}ENTER TARGET (URL/IP): {RESET}").strip()
    if not target: return

    while True:
        animation()
        print(f"{C}TARGET: {target} | AI SECURITY: ACTIVE{RESET}")
        print(f"{Y}SELECT COMMAND (001-100) | '0' to Exit{RESET}\n")

        # Compact Grid
        for i in range(1, 101):
            key = str(i)
            print(f"[{G}{key.zfill(3)}{RESET}]", end="  ")
            if i % 10 == 0: print()

        choice = input(f"\n\n{M}[ABDUL-MATEEN@AI-RECON]# {RESET}").strip()

        if choice == '0' or choice == '000':
            print(f"{G}Exiting... Respect the Creed, Abdul Mateen!{RESET}")
            break
        
        if choice in cmd_list:
            cmd_template, detail = cmd_list[choice]
            final_cmd = cmd_template.replace("{t}", target)
            run_with_ai(final_cmd, target, detail, choice)
            input(f"\n{Y}Press Enter to return to Menu...{RESET}")
        else:
            print(f"{R}Error: 001-100 tak choose karein.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Aborted by user.{RESET}")
        # --- Web Vulnerability & Bug Hunting Module ---
def run_web_scanner(target):
    import subprocess
    import os

    print(f"\n[+] Abdul Mateen Web Scanner Starting on: {target}")
    
    # Commands ki list: [Tool Name, Command]
    web_commands = [
        ["Nikto", f"nikto -h {target} -Tuning 1234589 -o nikto_report.txt"],
        ["Nikto XSS/Subdomain", f"nikto -h {target} -Plugins 'apache_expect_xss,subdomain'"],
        ["Warp Scan", f"nmap --script http-enum,http-vhosts,http-methods {target}"],
        ["Dirb (Directory Search)", f"dirb http://{target} -f"]
    ]

    for tool_name, cmd in web_commands:
        print(f"\n[*] Running {tool_name}...")
        try:
            # Yeh command execute karega aur result terminal pe dikhayega
            subprocess.run(cmd, shell=True, check=True)
        except Exception as e:
            print(f"[!] Error running {tool_name}: {e}")

# Is line ko aap apne main menu ya loop ke andar call kar sakte hain
# Agar aap chahte hain ke script khatam hote hi yeh khud chal jaye, toh niche wali line ko uncomment (hata dein #) kar dein:
# run_web_scanner(target)
