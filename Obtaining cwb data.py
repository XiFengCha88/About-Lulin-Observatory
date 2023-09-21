import urllib.request as ur
import time
import json
url="https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=CWB-4A6C99B8-2562-497B-AA8F-6A27AFDC9F55&format=JSON&locationName=%E4%B8%AD%E5%A3%A2&elementName=TEMP,WDIR,WDSD,HUMD"
print('(Observation local time), (Local temperture(℃)), (Local relative humidity(%)), (wind direction(degree)), (wind speed(m/s))')
txt=open("Weatherdata.txt","wt")
txt.write("obsTIME, TEMP, HUMD, WDIR, WDSD")
for i in range(0,240):
    site = ur.urlopen(url)
    page = site.read()
    contents = page.decode()
    data = json.loads(contents)
    obsTIME=data['records']['location'][0]['time']
    WDIR=data['records']['location'][0]['weatherElement'][0]['elementValue']
    WDSD=data['records']['location'][0]['weatherElement'][1]['elementValue']
    TEMP=data['records']['location'][0]['weatherElement'][2]['elementValue']
    HUMD=data['records']['location'][0]['weatherElement'][3]['elementValue']
    print(obsTIME, TEMP, HUMD, WDIR, WDSD, sep=", ")
    t=time.sleep(60)
    i+=1
    txt.write("\n")
    txt.write(str(obsTIME))
    txt.write(", ")
    txt.write(str(TEMP))
    txt.write(", ")
    txt.write(str(HUMD))
    txt.write(", ")
    txt.write(str(WDIR))
    txt.write(", ")
    txt.write(str(WDSD))
txt.close()

