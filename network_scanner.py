import sys
import logging

import netifaces as ni
import nmap


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
log = logging.getLogger(__name__)


class NetworkScanner(object):
    """docstring for NetworkScanner."""
    def __init__(self):
        pass

    def scan_devices(self):
        subnet = self.get_subnet()
        log.info('Getting devices on subnet {}...'.format(subnet))
        nmap_args = '-sP'
        scanner = nmap.PortScanner()
        scanner.scan(hosts=subnet, arguments=nmap_args)

        devices = []
        for ip in scanner.all_hosts():
            if 'mac' in scanner[ip]['addresses']:
                mac = scanner[ip]['addresses']['mac'].upper()
                ip_address = scanner[ip]['addresses']['ipv4']
                device = {'ip': ip, 'mac':mac}
                log.info('Found device {}'.format(device))
                devices.append(device)
        log.info('Found {} devices'.format(len(devices)))
        return devices

    def get_interfaces(self):
        log.info('Getting local interfaces...')
        interfaces = []
        for interface in ni.interfaces():
            if not interface.startswith(('lo', 'vir')):
                log.info('Found local interface {}'.format(interface))
                interfaces.append(interface)
        return interfaces

    def get_local_ip(self):
        interfaces = self.get_interfaces()
        log.info('Getting local ip address...')
        for interface in interfaces:
            try:
                addr = ni.ifaddresses(interface)[2][0]['addr']
                log.info('Local ip address is {}'.format(addr))
                return addr
            except KeyError:
                log.debug('Error: No local ip addresses found.')

    def get_subnet(self):
        ip = self.get_local_ip()
        # log.info('Getting subnet for ip address {}...'.format(ip))
        subnet = '.'.join(ip.split('.')[:3]) + '.0/24'
        log.info('Subnet is {}'.format(subnet))
        return subnet
