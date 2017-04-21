# Network Scanner
`network_scanner` can be used to quickly find devices on your local network. It automatically detects your network subnet, and then retrieves ip and mac addresses on this network.
## Usage

Note: This program requires root privileges, so it needs to be run with `sudo`.

### From a Terminal
```
$ sudo python network_scanner.py
```

### From another program:

```
from network_scanner import NetworkScanner

ns = NetworkScanner()

ns.scan_devices()
```
The result is a list of dictionaries with ip and mac addresses.


## Setup
Make sure you have `nmap` installed:
```
sudo apt install nmap
```
Install the requirements:
```
pip install -r requirements.txt
```
