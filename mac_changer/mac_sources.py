import re
import json
import time
import requests


def mac_generator(separator=None):
    for i in range(281474976710656):
        mac_address = ''.join(
            ['0'*(12 - len(str(hex(i)[2:]))), str(hex(i)[2:])])
        if separator:
            mac_address = re.findall(r'\w\w', mac_address)
            mac_address = f'{separator}'.join(mac_address)
        yield mac_address




def get_mac_address_info(mac_address=None):
    url = 'https://macaddress.io/mac-address-lookup'
    headers = {
        'X-CSRF-TOKEN': 'd4YueD1K2M8ISAKGlgKbwImxnxi0AUkZdxFGeX5p',
        'Content-Type': 'application/json;charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
        'Cookie': 'mac_address_vendor_lookup_session=eyJpdiI6ImRDUWhlaHEwcWZReUZNcUJhNlFOZ3c9PSIsInZhbHVlIjoiQzVtdmJxNTJzV3JiTVFjXC84eGJ1bWpLUnltekRyREFJZlFnU3BsVlZJckVoeDVvRDhcL3lUYlYzMkNnZEhxcHRFIiwibWFjIjoiNmIzNTIwOGYyZjVlM2Q0NWJmMTBmM2ViNDc0YzFmYWY0ZGM1NDQ3OTAyZmY1MDc4NzFkNThiNmQ0N2VjYWQ2MSJ9'
    }

    data = {
        'macAddress': f'{mac_address}',
        'not-web-search': True
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.json())

# 23:00
# test_mac = '00:e9:3a:37:7e:69'
# get_mac_address_info(test_mac)

mac_adresses = mac_generator(':')
for mac in mac_adresses:
    print('=' * 20)
    get_mac_address_info(mac)
    time.sleep(0.5)


'''
sources_list = [
    'https://macaddress.io/mac-address-lookup'
    ]
url = 'https://macaddress.io/mac-address-lookup'

headrs = {
    'content-type':'application/json'

}
data = {
    'macAddress': '00:e9:3a:37:7e:69',
    'not-web-search':True
}

response = requests.get(url, headers=headrs, data=json.dumps(data))
print(response.text)


import requests
import json

url = "https://macaddress.io/mac-address-lookup"

payload = json.dumps({
  "macAddress": "00:00:3a:37:7e:00",
  "not-web-search": True
})
headers = {
  'Content-Type': 'application/json',
  'X-XSRF-TOKEN': 'eyJpdiI6Im05Z0RVMVwvUlwvYnZ4bzVubHRpRlhTQT09IiwidmFsdWUiOiJMU05zUEVIVFlSS0hVaFhRamdKTnpXZ2FHckVtbUd1Y2xXMmUxMXFIc3BweTdtQ2xGeE5RZ3VIYlhRdFJtcE1RIiwibWFjIjoiNzEyMDgxOTc0Mjg2NjZmYmJlNzc0YmM2NDFlOTM3M2NjMzVlZGQ2Y2MwZmMyYjdlN2JmMWJhOGYzMWFjZGVlNyJ9',
  'X-CSRF-TOKEN': '53mEIlRCr49l83yHzT2Pr5HLpF8GRdCfTppKzChr',
  'Cookie': 'XSRF-TOKEN=eyJpdiI6IlkzQkVrcVRFYlJXQ09vS1wvTkI2amNRPT0iLCJ2YWx1ZSI6IllhSEw3SlBMXC93cXN2dzc2QkJzZ2ZsXC9ScFRVVUpLVjBqekdKbWVCTWVQWlZ4YmNCeVhrbnVsbUUydEJoQXBZayIsIm1hYyI6IjI3OGQxNWY2YjY3YjE5MjE2NzM5ODFlODg4YTdmMTdlMDJhZGRjZTIzYTYyMTIxMjZiM2JhZWEzNzFhYmE4MDQifQ%3D%3D; mac_address_vendor_lookup_session=eyJpdiI6ImFlWm5ERHU0M01uTjlEYjVTN3NJT3c9PSIsInZhbHVlIjoiSzd6eVRPd3pSZFVaXC95Tk9EZVwveFNJYXAwVGV5R3FkY2FRN0M0Qk1xZWw5dnIxWElMXC8rbVFUV0Q1am5nZWpyWCIsIm1hYyI6IjkxMmUzODg2ZjdmOTVlZGU1YjQzMjU3N2RkODhjOTdiNmEyODY5NmE3ZjEwNGI3YWE4MTkwNzI3YmVkZDI3NzMifQ%3D%3D'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)


for i in range(10, 100):

    payload = json.dumps({
    "macAddress": f"00:00:{i}:37:7e:00",
    "not-web-search": True
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    print(f'============= {i} {response.status_code} ==============', )
    print(response.text)
    time.sleep(0.2)


for i in range(10, 100):

    payload = json.dumps({
    "macAddress": f"{i}:00:3a:37:00:00",
    "not-web-search": True
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    print(f'============= {i} {response.status_code} 2!!!! ==============', )
    print(response.text)
    time.sleep(0.2)
'''
