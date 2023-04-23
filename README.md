# 🤪 Supreme Octo Giggle 
## 😂 Random MAC Address Changer

This is an experimental ethical hacking tool to randomize MAC address after a certain time interval. This tool can be used to improve your privacy and security when connected to public Wi-Fi networks.

⚠️ Please note that this tool is for ethical purposes only. Any weird attempts or malicious usage of this tool are strictly prohibited and may lead to legal consequences. 

## How it works

Giggle is a Python script that changes the MAC address of your Wi-Fi network adapter at regular intervals to make it difficult for anyone to track your online activities. The script uses the Windows cytpes & native network adapters to get the current network interface and change the MAC address of the adapter. You can specify a target Wi-Fi network to apply the MAC address changes only when connected to that network.

## How to use

### For Window Users

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
### When running the code, it might complain about not having admin privileges  so you have to accept the admin privileges  prompt or follow the following steps
To run the script with admin privileges, follow these steps:

1. Open the Command Prompt as an administrator.
   - Press the `Windows key` + `X` and select `Command Prompt (Admin)` from the menu.
2. Navigate to the directory where the script is located.
3. Type `python scriptname.py` and press `Enter`.
   - Replace `scriptname` with the name of your Python script.
4. If prompted, allow the script to make changes to your computer by clicking `Yes`.


```bash
python supreme.py
```

### For Linux Users
The script was primarily made for windows for any glitches and bugs... Sorry in advance
1. Changing to a specific mac address 
```bash
$ python3 giggle.py wlan0 -m 00:FA:CE:DE:AD:00
```
2. Changing to a random mac address
```bash
$ python3 giggle.py wlan0 --random
```

The script will run in the background and change the MAC address of your Wi-Fi adapter after every specified interval.

## Disclaimer
This tool is provided for educational and ethical purposes only. Any malicious usage of this tool is strictly prohibited and may lead to legal consequences. The author will not be responsible for any damages or legal issues caused by the misuse of this tool. Use at your own risk.

## Author
Giggle is developed and maintained by [Eddie Gulay](https://github.com/eddygulled).

## License
This project is licensed under the MIT License. Feel free to use and modify the code as per your needs.
