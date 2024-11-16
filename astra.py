import subprocess
import os
import pathlib
import argparse
import urllib.request
import sys
import platform


class Astra:
    """ A simulare astra object """
    def __init__(self):
        """ Initilize attributies """ 
        self.license = os.getenv("ASTRA_LICENCE") #Get license key from env var
        self.srv_name = "astra" #Service name

    def check_system(self):
        """ Check system """
        if platform.system() == "Linux":
            return True
        else:
            return False
    
    def astra_check(self):
        """ Checking astra installed """
        if self.check_system():
            path = pathlib.Path("/usr/bin/astra")
            #Check astra is installeda
            if path.exists():
                return True
            else:
                return False
        else:
            print("[+] Working only linux [+]")
            sys.exit(1) #Stop program if system not linux
    
    def check_license(self):
        """ Check license """ 
        if not self.license:
            print("[+] ASTRA_LICENCE envaurment variable is not set [+]")
        url = f"https://cesbo.com/astra-license/{self.license}"
        try:
            response = urllib.request.urlopen(url)
            if response.getcode() == 200:
                return True
            else:
                return False
        except urllib.error.HTTPError as e:
            print(f"[-] Licanse checking fail: {e} [-]")
            return False
    
    def astra_install(self):
        """ Installing astra """
        if not self.check_license():
            print("[+] License not valid [+]")
            sys.exit(1) #Stop program if license not valid

        if not self.astra_check():
            #Curl path
            curl_path = pathlib.Path("/usr/bin/curl")
            #Check curl if not exist installing
            if not curl_path.exists():
                #Install curl
                command = "sudo apt install curl -y"
                subprocess.run(command, shell=True, text=True, check=True)
                
            #Install astra
            command = "curl -Lo /usr/bin/astra https://cesbo.com/astra-latest"
            subprocess.run(command, shell=True, text=True, check=True)
            command = "chmod +x /usr/bin/astra"
            subprocess.run(command, shell=True, text=True, check=True)
            command = "astra init"
            subprocess.run(command, shell=True, text=True, check=True)
            command = "mkdir -p /etc/astra"
            subprocess.run(command, shell=True, text=True, check=True)
            command = f"curl -o /etc/astra/license.txt https://cesbo.com/astra-license/{self.license}"
            subprocess.run(command, shell=True, text=True, check=True)
            command = f"systemctl start {self.srv_name}"
            subprocess.run(command, shell=True, text=True, check=True)
            command = f"systemctl enable {self.srv_name}"
            subprocess.run(command, shell=True, text=True, check=True)
            print("[+] Installed astra [+]")
        else:
            print("[+] Astra alredy installed [+]")
            sys.exit(0)
    
    def tbs_driver_install(self):
        """ Installing TBS driver auto all version """
        if not self.check_system():
            print("[+] Working only linux [+]")
            sys.exit(1)
        command = "curl -sSf https://cdn.cesbo.com/astra/scripts/drv-tbs.sh | sh"
        subprocess.run(command, shell=True, text=True, check=True)
        print("[+] TBS driver installed [+]")
    
    def astra_update(self):
        """ Update astra """
        if self.astra_check():
            command = "rm -f /usr/bin/astra"
            subprocess.run(command, shell=True, text=True, check=True)
            command = "curl -Lo /usr/bin/astra https://cesbo.com/astra-latest"
            subprocess.run(command, shell=True, text=True, check=True)
            command = "chmod +x /usr/bin/astra"
            subprocess.run(command, shell=True, text=True, check=True)
            command = f"systemctl restart {self.srv_name}"
            subprocess.run(command, shell=True, text=True, check=True)
            print("[+] Astra updated [+]")
            
    
    def astra_remove(self):
        """ Remove astra  """
        if self.astra_check():
            command = f"systemctl stop {self.srv_name}"
            subprocess.run(command, shell=True, text=True, check=True)
            command = f"systemctl disable {self.srv_name}"
            subprocess.run(command, shell=True, text=True, check=True)
            command = "astra remove"
            subprocess.run(command, shell=True, text=True, check=True)
            command = "rm -rf /usr/bin/astra /etc/astra"
            subprocess.run(command, shell=True, text=True, check=True)
            print("[+] Astra removed [+]")


def main ():
    astra = Astra()

    parser = argparse.ArgumentParser(description="Astra control cli based tool")
    parser.add_argument("-up", "--update", action="store_true", help="Update astra")
    parser.add_argument("-i", "--install", action="store_true", help="Install astra")
    parser.add_argument("-r", "--remove", action="store_true", help="Remove astra")
    parser.add_argument("-tdi", "--tbs_driver_install", action="store_true", help="Installing TBS driver")

    # Check if user not give argument print help menu
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    args = parser.parse_args() # Parse argument

    if args.update:
        astra.astra_update()
    if args.install:
        astra.astra_install()
    if args.remove:
        astra.astra_remove()
    if args.tbs_driver_install:
        astra.tbs_driver_install()
    

if __name__ == "__main__":
    main()
