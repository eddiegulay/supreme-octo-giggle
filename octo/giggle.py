import wlanapi
import random
import time

class Giggle:
    def __init__(self, target_ssid, interval=30*60, interface_guid=None):
        self.target_ssid = target_ssid
        self.interval = interval
        self.interface_guid = interface_guid or self.get_interface_guid()

    def get_interface_guid(self):
        """
            giggler.get_interface_guid() -> str
            # Get the GUID of the first Wi-Fi network adapter
        """
        interface_list = wlanapi.WlanEnumInterfaces()
        if not interface_list:
            raise Exception("No Wi-Fi network adapters found")
        return interface_list[0]['InterfaceGuid']

    def get_random_mac_address(self):
        """
            giggler.get_random_mac_address() -> str
            # Generate a random MAC address
        """

        mac_bytes = [0x02, 0x00, 0x00,
                    random.randint(0x00, 0x7f),
                    random.randint(0x00, 0xff),
                    random.randint(0x00, 0xff)]
        return ':'.join(map(lambda x: "{0:02x}".format(x), mac_bytes))

    def giggle(self):
        """
            giggler.giggle()
            # Change the MAC address of the Wi-Fi network adapter
            # when the target SSID is connected
        """
        interface_guid = self.interface_guid
        interval = self.interval
        target_ssid = self.target_ssid

        while True:
            # Get the current SSID
            current_network = wlanapi.WlanGetCurrentNetwork(interface_guid)
            current_ssid = current_network.get('ssid', '')

            # Check if the current SSID matches the target SSID
            if current_ssid.decode() == target_ssid:
                # Generate a random MAC address
                mac_address = self.get_random_mac_address()

                # Set the MAC address for the Wi-Fi network adapter
                wlanapi.WlanSetInterface(
                    interface_guid,
                    wlanapi.WLAN_INTF_OPCODE_CURRENT_MAC_ADDRESS,
                    mac_address)

                print(f"MAC address changed to {mac_address} for {target_ssid}")

            # Wait for the specified interval
            time.sleep(interval)
