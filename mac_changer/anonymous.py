import re
import argparse
import subprocess

# выкачать БД мак адресов
mac_pattern = '\w\w:\w\w:\w\w:\w\w:\w\w:\w\w'

def get_options():
    parser = argparse.ArgumentParser(description='change mac address', usage='[interface] [options]')
    parser.add_argument('-i', '--interface', dest='interface', help='interface for new mac')
    parser.add_argument('-m', '--mac', dest='mac', help='new mac address')
    parser.add_argument('-r', '--random', action='store_true', help='randomize mac')
    options = parser.parse_args()
    return options

def get_current_mac(interface=None):
    global mac_pattern
    ifconfig_result = subprocess.check_output(['ifconfig', interface], encoding='utf-8')
    default_mac = re.search(r'{}'.format(mac_pattern), ifconfig_result)
    return default_mac.group(0)



def change_mac_address(new_mac):
    pass

def mac_is_valid(mac):
    return True

def gen_random_mac():
    random_mac = '00:00:00:00:00:00'
    return random_mac 




options = get_options()






current_mac = get_current_mac(options.interface)

print(current_mac)





'''

if options.random:
    change_mac_address(new_mac=gen_random_mac())
else:
    if mac_is_valid(options.mac):
        change_mac_address(options.mac)
    else:
        print('[-] mac value not valid')

'''




'''
class Anonymous():

    def __init__(self, interface='wlan0'):
        self.interface = interface
        self.mac_pattern = '\w\w:\w\w:\w\w:\w\w:\w\w:\w\w'
        self.default_mac = self.get_current_mac(self.interface)
        self.current_mac = self.get_current_mac(self.interface)

    def get_options(self):
        input_options = str(input)
    @getattr
    def get_current_mac(self, interface=None):
        ifconfig_result = subprocess.check_output(
            ['ifconfig', interface], encoding='utf-8')
        default_mac = re.search(r'{}'.format(
            self.mac_pattern), ifconfig_result)
        return default_mac.group(0)

    def set_current_mac(self):
        pass

    def mac_is_valid(self):
        pass

    def create_new_mac(self):
        pass

    def change_mac_address(self, interfase):
        pass

    def return_default_mac(self):
        pass
    
    def help(self):
        print('Usage: mac [TODO] [param]\nTODO:\nset\nget-current')


    def run(self):

        self.run()


'''
