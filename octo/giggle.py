import random
import time
from ctypes import windll
wlanapi = windll.wlanapi

def get_interface_list():
    # Get the list of Wi-Fi network adapters
    interface_list = wlanapi.WlanEnumInterfaces()
    if not interface_list:
        raise Exception("No Wi-Fi network adapters found")
    return interface_list

def get_interface_guid():
    # Get the GUID of the first Wi-Fi network adapter
    interface_list = wlanapi.WlanEnumInterfaces()
    # print(interface_list) 🐛🐛🐛 
    if interface_list is None:
        raise Exception("No Wi-Fi network adapters found")
    return interface_list[0]['InterfaceGuid']


class Giggle:
    def __init__(self, target_ssid, interface_guid=None):
        self.target_ssid = target_ssid
        self.interface_guid = interface_guid or get_interface_guid()
        self.interval = 30 * 60 # Interval in seconds

    def get_random_mac_address(self):
        # Generate a random MAC address
        mac_bytes = [0x02, 0x00, 0x00,
                     random.randint(0x00, 0x7f),
                     random.randint(0x00, 0xff),
                     random.randint(0x00, 0xff)]
        return ':'.join(map(lambda x: "{0:02x}".format(x), mac_bytes))

    def change_mac_address(self):
        # Generate a random MAC address
        mac_address = self.get_random_mac_address()

        # Set the MAC address for the Wi-Fi network adapter
        wlanapi.WlanSetInterface(
            self.interface_guid,
            wlanapi.WLAN_INTF_OPCODE_CURRENT_MAC_ADDRESS,
            mac_address)

        print(f"MAC address changed to {mac_address} for {self.target_ssid}")

    def run(self):
        while True:
            # Get the current SSID
            current_network = wlanapi.WlanGetCurrentNetwork(self.interface_guid)
            current_ssid = current_network.get('ssid', '')

            # Check if the current SSID matches the target SSID
            if current_ssid.decode() == self.target_ssid:
                self.change_mac_address()

            # Wait for the specified interval
            time.sleep(self.interval)