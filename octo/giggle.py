import subprocess
import regex as re
import string
import random
import time
import ctypes
import sys



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # your code that requires admin privileges goes here
    print("Running with admin privileges")
else:
    # Re-run the script with admin privileges
    if sys.argv[-1] != "asadmin":
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        print("Please run the script as an administrator")




class Giggle:
   def __init__(self, wifi_name,  platform = "windows"):
      self.platform = platform
      self.ssid = str(wifi_name).lower().replace(" ", "").strip()

      

      # the registry path of network interfaces
      self.network_interface_reg_path = r"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}"
      # the transport name regular expression, looks like {AF1B45DB-B5D4-46D0-B4EA-3E18FA49BF5F}
      self.transport_name_regex = re.compile("{.+}")
      # the MAC address regular expression
      self.mac_address_regex = re.compile(r"([A-Z0-9]{2}[:-]){5}([A-Z0-9]{2})")

      # check if the wifi name exists
      if self.approve_mac_update(self.get_connected_adapters_mac_address()) == None:
         print("Wifi name does not Exist")


   def get_random_mac_address(self):
      """Generate and return a MAC address in the format of WINDOWS"""
      # get the hexdigits uppercased
      uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
      # 2nd character must be 2, 4, A, or E
      return random.choice(uppercased_hexdigits) + random.choice("24AE") + "".join(random.sample(uppercased_hexdigits, k=10))
      

   def clean_mac(self):
      """Simple function to clean non hexadecimal characters from a MAC address
      mostly used to remove '-' and ':' from MAC addresses and also uppercase it"""
      return "".join(c for c in mac if c in string.hexdigits).upper()  


   def get_connected_adapters_mac_address(self):
    # make a list to collect connected adapter's MAC addresses, transport name, and SSID
    connected_adapters_mac = []
    # use the getmac command to extract 
    for potential_mac in subprocess.check_output("getmac").decode().splitlines():
        # parse the MAC address from the line
        mac_address = self.mac_address_regex.search(potential_mac)
        # parse the transport name from the line
        transport_name = self.transport_name_regex.search(potential_mac)
        # get the network SSID associated with the adapter using the netsh command
        ssid = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode()
        ssid = re.search("SSID\s+:\s(.*)", ssid)
        if mac_address and transport_name and ssid:
            # if a MAC, transport name, and SSID are found, add them to our list
            connected_adapters_mac.append((mac_address.group(), transport_name.group(), ssid.group(1)))
    return connected_adapters_mac

   def approve_mac_update(self, connected_adapters_mac):
      adapter_transport_name = None, None, None
      for adapter in connected_adapters_mac:
         mac, t_name, ssid = adapter
         ssid = str(ssid).lower().replace(" ", "").strip()

         if self.ssid == ssid:
            print("Approved for update.....")
            return adapter
         
      print(f"Failed to approve for network {self.ssid}")

   def change_mac_address(self, adapter_transport_name, new_mac_address):
      # use reg QUERY command to get available adapters from the registry
      output = subprocess.check_output(f"reg QUERY " +  self.network_interface_reg_path.replace("\\\\", "\\")).decode()
      for interface in re.findall(rf"{self.network_interface_reg_path}\\\d+", output):
         # get the adapter index
         adapter_index = int(interface.split("\\")[-1])
         interface_content = subprocess.check_output(f"reg QUERY {interface.strip()}").decode()
         if adapter_transport_name in interface_content:
               # if the transport name of the adapter is found on the output of the reg QUERY command
               # then this is the adapter we're looking for
               # change the MAC address using reg ADD command
               changing_mac_output = subprocess.check_output(f"reg add {interface} /v NetworkAddress /d {new_mac_address} /f").decode()
               # print the command output
               print(changing_mac_output)
               # break out of the loop as we're done
               break
      # return the index of the changed adapter's MAC address
      return adapter_index


   def disable_adapter(self, adapter_index):
      # use wmic command to disable our adapter so the MAC address change is reflected
      disable_output = subprocess.check_output(f"wmic path win32_networkadapter where index={adapter_index} call disable").decode()
      return disable_output


   def enable_adapter(self, adapter_index):
      # use wmic command to enable our adapter so the MAC address change is reflected
      enable_output = subprocess.check_output(f"wmic path win32_networkadapter where index={adapter_index} call enable").decode()
      return enable_output

   def giggle(self, interval):
      interval *= 60
      while True:
         new_mac_address = self.get_random_mac_address()
    
         connected_adapters_mac = self.get_connected_adapters_mac_address()
         
         old_mac_address, target_transport_name, ssid = self.approve_mac_update(connected_adapters_mac)

         print(f"[*] Old MAC address for {ssid}: ", old_mac_address)
         adapter_index = self.change_mac_address(target_transport_name, new_mac_address)
         print("[+] Changed to: ", new_mac_address)
         self.disable_adapter(adapter_index)
         print("[+] Adapter is disabled")
         self.enable_adapter(adapter_index)
         print("[+] Adapter is enabled again")
         print("..................................................")
         time.sleep(interval)

