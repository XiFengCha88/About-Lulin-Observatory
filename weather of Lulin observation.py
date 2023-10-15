#Weather inS Lulin Observatory
#Author: Xi-Feng Cha
#Begun Coding: 2023-Oct-14 11:41

import urllib.request as ur
from bs4 import BeautifulSoup as bs
import json

Date = input("please input the date (yyyymmdd): ") #Input the date.
rawfile = f"raw_weather{Date}.txt" #Raw file

def dataraw(file, date):
      url = f"https://www.lulin.ncu.edu.tw/weather/api/weather/{date}/date"#api in offical website of Lulin Observatory
      site=ur.urlopen(url)
      soup=bs(site,"html.parser")
      with open(file, "w") as raw:
            raw.write(str(soup))

dataraw(rawfile, Date)
rraw = open(rawfile, "r")
JRAW = json.loads(rraw.readlines()[0])
Info = JRAW["dataset"]["datasetInfo"]["fields"]

def unit(u):
      return Info[u]["unit"]
def descript(d):
      return Info[d]["description"]

para = [r"datetime", r"Temp_In", r"Temp_Out", r"Hum_In", r"Hum_Out", r"Bar", r"Wind_Speed", r"Rain", r"Rain_Rate", r"THW_Index"]

#Discription of every parameter
ddate = descript(para[0])
dIT, dOT, dIH, dOH = descript(para[1]), descript(para[2]), descript(para[3]), descript(para[4])
dP, dWS, dRain, dRrate = descript(para[5]), descript(para[6]), descript(para[7]), descript(para[8])
diTHW = descript(para[9])

#Unit of every parameter
tzdate = Info["datetime"]["tz"]
uIT, uOT, uIH, uOH = unit(para[1]), unit(para[2]), unit(para[3]), unit(para[4])
uP, uWS, uRain, uRrate = unit(para[5]), unit(para[6]), unit(para[7]), unit(para[8])
uiTHW = unit(para[9])

#Table #Data
rawdata = JRAW["dataset"]["data"]
def value(i, v):
      return rawdata[i][v]

with open(f"WLO{Date}.txt", "w") as wlow:
      #description
      wlow.write("===Table of weather information===\n#Description\n")
      wlow.write("tz: "+ descript(para[0]) + "\n")
      wlow.write("I.T.: "+ descript(para[1]) + "\n")
      wlow.write("O.T.: "+ descript(para[2]) + "\n")
      wlow.write("I.H.: "+ descript(para[3]) + "\n")
      wlow.write("O.H.: "+ descript(para[4]) + "\n")
      wlow.write("P: "+ descript(para[5]) + "\n")
      wlow.write("WS: "+ descript(para[6]) + "\n")
      wlow.write("Rain: "+ descript(para[7]) + "\n")
      wlow.write("Rrate: "+ descript(para[8]) + "\n")
      wlow.write("iTHW: "+ descript(para[9]) + "\n\n")
      wlow.write("#Data\n")
      
      #parameter
      text = "tz ({}) | I.T. ({}) | O.T. ({}) | I.H. ({}) | O.H. ({}) | P ({}) | WS ({}) | Rain ({}) | Rrate ({}) | iTHW ({})".format(tzdate, uIT, uOT, uIH, uOH, uP, uWS, uRain, uRrate, uiTHW)
      wlow.write("="*len(text) + "\n")
      wlow.write(text + "\n")
      wlow.write("-"*len(text) + "\n")

#Fill in the value
for i in range(0, len(rawdata), 10):
      V = str([value(i, j) for j in para])
      with open(f"WLO{Date}.txt", "a") as wloa: #WLO: weather of Lulin Observatory
            wloa.write(V)
            wloa.write("\n")
with open(f"WLO{Date}.txt", "a") as wloa:
      wloa.write("-"*len(text) + "\n")

print(f"Save the datas in WLO{Date}.txt!")
rraw.close()
#Updated: 2023-Oct-15 23:26
