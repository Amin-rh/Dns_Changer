import subprocess


print('Hi, User\n')

_options = [
    '1) Set Dns (Static)',
    '2) Set Dns (DHCP)',
    '3) Set Dns (Shecan)'
]
for _ in _options:
    print(_)

_ = int(input(':'))

if _ == 1:
    def set_dns_windows(interface_name, dns_servers):
        try:
            subprocess.run(['netsh', 'interface', 'ipv4', 'set',
                            'dnsservers', interface_name, 'static', 'none'], check=True)
            for dns in dns_servers:
                subprocess.run(['netsh', 'interface', 'ipv4', 'add',
                                'dnsservers', interface_name, dns, 'index=1'], check=True)
            print('Dns Changed successfully.\n')
            print('-----------------------------')
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

    print('---------- S t a t i c ----------\n')
    interface = input("Enter the network interface name : ")
    dns_input = input("Enter the DNS servers separated by commas : ")

    dns_list = [dns.strip() for dns in dns_input.split(',')]

    set_dns_windows(interface, dns_list)

if _ == 2:
    def reset_dns(interface_name):
        try:
            subprocess.run(['netsh', 'interface', 'ipv4', 'set',
                            'dnsservers', interface_name, 'dhcp'], check=True)
            print('Dns Changed successfully.\n')
            print('-----------------------------')
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
    print('---------- D H C P ----------\n')
    interface = input("Enter the network interface name: ")
    reset_dns(interface)

if _ == 3:
    def set_dns_windows(interface_name, dns_servers):
        try:
            subprocess.run(['netsh', 'interface', 'ipv4', 'set',
                            'dnsservers', interface_name, 'static', 'none'], check=True)

            for dns in dns_servers:
                subprocess.run(['netsh', 'interface', 'ipv4', 'add',
                                'dnsservers', interface_name, dns, 'index=1'], check=True)
            print('Dns Changed successfully.\n')
            print('-----------------------------')
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
    print('---------- S h e c a n ----------\n')
    interface = input("Enter the network interface name : ")

    _dns_list = ['185.51.200.2', '178.22.122.100']  # free.Shecan.ir DNS

    set_dns_windows(interface, _dns_list)
