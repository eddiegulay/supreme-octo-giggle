# 🤪 Supreme Octo Giggle | Random MAC Address Changer 🤪

This is an experimental ethical hacking tool to randomize MAC address after a certain time interval. This tool can be used to improve your privacy and security when connected to public Wi-Fi networks.

⚠️ Please note that this tool is for ethical purposes only. Any weird attempts or malicious usage of this tool are strictly prohibited and may lead to legal consequences. ⚠️

## How it works

Giggle is a Python script that changes the MAC address of your Wi-Fi network adapter at regular intervals to make it difficult for anyone to track your online activities. The script uses the Windows WLAN API to get the current network interface and change the MAC address of the adapter. You can specify a target Wi-Fi network to apply the MAC address changes only when connected to that network.

## How to use

1. Install Python 3 on your Windows machine.
2. Download or clone the Giggle repository to your computer.
3. Open a command prompt or terminal and navigate to the Giggle folder.
4. Install the required Python modules by running `pip install -r requirements.txt`.
5. Open the `supreme.py` file in a text editor and modify the `target_ssid` variable to match the name of your Wi-Fi network.
```python
    target_ssid = "Your WiFi Network Name"
    giggle = Giggle(target_ssid)
    # Start to giggle 😁😆😂
    giggle.giggle()
```
6. Save the changes and run the `supreme.py` file using Python.

```bash
python supreme.py
```

The script will run in the background and change the MAC address of your Wi-Fi adapter after every specified interval.

## Disclaimer
This tool is provided for educational and ethical purposes only. Any malicious usage of this tool is strictly prohibited and may lead to legal consequences. The author will not be responsible for any damages or legal issues caused by the misuse of this tool. Use at your own risk.

## Author
Giggle is developed and maintained by [Eddie Gulay](https://github.com/eddygulled).

## License
This project is licensed under the MIT License. Feel free to use and modify the code as per your needs.
