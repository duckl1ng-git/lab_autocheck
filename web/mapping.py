mapping = {
    '01': {
        'name': 'Windows',
        'vars': {
            'fw1_lan_ip': '10.10.10.254',
            'pfsense_user': 'admin',
            'pfsense_pass': 'pfsense',
            'winsrv_ip': '10.10.10.1',
            'winsrv_user': 'Administrator',
            'winsrv_pass': 'eve@1234',
            'win7_ip': '10.10.10.11',
            'win10_ip': '10.10.10.12',
            'win_user': 'Admin',
            'win_pass': 'eve@123',
            'user1': 'UserSales',
            'pass1': 'eve@123',
            'user2': 'UserIT',
            'pass2': 'eve@123',
        }
    },
    '03': {
        'name': 'Базовая схема PfSense',
        'vars': {
            'fw1_dmz_ip': '10.10.10.254',
            'fw2_dmz_ip': '10.10.10.1',
            'fw2_lan_ip': '10.10.20.254',
            'pfsense_user': 'admin',
            'pfsense_pass': 'pfsense',
            'lan_win7_ip': '10.10.20.10',
            'windows_user': 'Admin',
            'windows_password': 'eve@123',
        }
    },
    '04': {
        'name': 'ICMP туннелирование',
        'vars': {
            'fw1_dmz_ip': '10.10.10.254',
            'fw2_dmz_ip': '10.10.10.1',
            'fw2_lan_ip': '10.10.20.254',
            'pfsense_user': 'admin',
            'pfsense_pass': 'pfsense',
            'lan_kali_ip': '10.10.20.11',
            'linux_user': 'root',
            'linux_password': 'eve@123',
            'lan_win7_ip': '10.10.20.10',
            'windows_user': 'Admin',
            'windows_password': 'eve@123',
        }
    },
    '05': {
        'name': 'DNS туннелирование',
        'vars': {
            'fw1_dmz_ip': '10.10.10.254',
            'fw2_dmz_ip': '10.10.10.1',
            'fw2_lan_ip': '10.10.20.254',
            'pfsense_user': 'admin',
            'pfsense_pass': 'pfsense',
            'lan_kali_ip': '10.10.20.12',
            'linux_user': 'root',
            'linux_password': 'eve@123',
            'lan_win7_ip': '10.10.20.10',
            'windows_user': 'Admin',
            'windows_password': 'eve@123',
            'lan_win_dns_ip': '10.10.20.1',
            'wan_win_dns_ip': '',
            'windows_server_user': 'Administrator',
            'windows_server_password': 'eve@123',
        }
    },
    '06': {
        'name': 'VPN на PfSense',
        'vars': {
            'fw1_lan_ip': '10.10.10.254',
            'pfsense_user': 'admin',
            'pfsense_pass': 'pfsense',
            'wan_win7_ip': '10.10.20.0',
            'wan_win10_ip': '10.10.20.1',
            'windows_user': 'Admin',
            'windows_password': 'eve@123',
            'winserver_ip': '10.10.10.1',
            'windows_server_user': 'Administrator',
            'windows_server_password': 'eve@1234',
        }
    },
    '07': {
        'name': 'Proxy',
        'vars': {
            'fw1_dmz_ip': '10.10.10.254',
            'fw2_dmz_ip': '10.10.10.1',
            'fw2_lan_ip': '10.10.20.254',
            'pfsense_user': 'admin',
            'pfsense_pass': 'pfsense',
            'lan_win7_ip': '10.10.20.10',
            'windows_user': 'Admin',
            'windows_password': 'eve@123',
        }
    },
    '08': {
        'name': 'Reverse Proxy',
        'vars': {
            'fw1_lan_ip': '10.10.10.1',
            'fw1_wan_ip': '',
            'pfsense_user': 'admin',
            'pfsense_pass': 'pfsense',
            'lan_win7_ip': '10.10.10.104',
            'windows_user': 'Admin',
            'windows_password': 'eve@123',
            'web1_ip': '10.10.10.101',
            'web2_ip': '10.10.10.102',
            'web3_ip': '10.10.10.103',
            'rproxy_ip': '10.10.10.200',
            'wan_kali_ip': '',
            'linux_user': 'root',
            'linux_password': 'eve@123',
            'is_nginx_reverse_proxy': False,
        }
    },
}