import re
import json
import time
import requests

mac_info_save = []


def mac_generator(separator=None):
    for i in range(281474976710656):
        mac_address = ''.join(
            ['0'*(12 - len(str(hex(i)[2:]))), str(hex(i)[2:])])
        if separator:
            mac_address = re.findall(r'\w\w', mac_address)
            mac_address = f'{separator}'.join(mac_address)
        yield mac_address


 
def get_sourse_keys():
    response = requests.get('https://macaddress.io/mac-address-lookup', verify=False)
    csrf_token = re.search(r'csrf-token" content=".+>', response.text).group(0)
    csrf_token = csrf_token[csrf_token.find('=') + 2: -2]
    mac_address_vendor_lookup_session = response.cookies['mac_address_vendor_lookup_session']
    return csrf_token, mac_address_vendor_lookup_session

def get_mac_address_info(mac_address=None):
    global mac_info_save
    x_csrf_token, mac_address_vendor_lookup_session = get_sourse_keys()

    url = 'https://macaddress.io/mac-address-lookup'
    headers = {
        'X-CSRF-TOKEN': f'{x_csrf_token}',
        'Content-Type': 'application/json;charset=utf-8',
        # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
        'Cookie': f'mac_address_vendor_lookup_session={mac_address_vendor_lookup_session}'
    }
    data = {
        'macAddress': f'{mac_address}',
        'not-web-search': True
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print('CODE:', response.status_code)
    print(response.json())


    #mac_info_save.append(response.json())
    #if len(mac_info_save) == 10:
        #with open ('mac_info_save', 'a') as file:
            #for i_mac in mac_info_save:
                #file.write(''.join([json.dumps(i_mac), '\n']))
        #mac_info_save.clear()


# testing tokens

count = 0
mac_gens = mac_generator()
for mac in mac_gens:
    print(f'request {count} ', '='*100)
    get_mac_address_info(mac)
    count = count + 1
    time.sleep(60)



# requests.exceptions.SSLError: HTTPSConnectionPool(host='macaddress.io', port=443): Max retries exceeded with url: /mac-address-lookup (Caused by SSLError(SSLZeroReturnError(6, 'TLS/SSL connection has been closed (EOF) (_ssl.c:997)')))
# 784