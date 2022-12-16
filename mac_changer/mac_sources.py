import requests
import datetime
import time
import functools
import json
def timer(func):

    @functools.wraps(func)

    def wrapped_func(*args):
        time_start = time.time()

        result = func(*args)
        
        time_delta = time.time() - time_start
        print(time_delta)
        return result
    return wrapped_func

'''


test_mac = '00:e9:3a:37:7e:69'


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

'''

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
'''
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


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

result = '{"vendorDetails":{"oui":"000029","isPrivate":false,"companyName":"Imc Networks Corp","companyAddress":"16931 MILLIKEN AVE. IRVINE CA 92714-5013 US","countryCode":"US"},"blockDetails":{"blockFound":true,"borderLeft":"000029000000","borderRight":"000029FFFFFF","blockSize":16777216,"assignmentBlockSize":"MA-L","dateCreated":"2000-11-09","dateUpdated":"2015-09-27"},"macAddressDetails":{"searchTerm":"00:00:29:37:7e:00","isValid":true,"virtualMachine":"Microsoft Virtual PC / Virtual Server","applications":["Reserved and require IESG ratification for assignment"],"transmissionType":"unicast","administrationType":"UAA","wiresharkNotes":"No details","comment":""}}'

print(type(result))

result = json.loads(result)
print(type(result))
print(result['vendorDetails']['oui'])

# 00:00:00:00:00:00
#from 0 to 99

#from a to f

import string

ascii_symbols = string.ascii_letters
print(ascii_symbols[:6])
print(type(string.digits))

def mac_generator():
    mac_symbols_string =''.join([string.digits,ascii_symbols[:6]])
    mac_parts_list = ['0','0']
    
    for i in range(1, -1, -1):

        for sym in mac_symbols_string:
            mac_parts_list[i] = sym
            print(''.join(mac_parts_list))


  



mac_generator()
    