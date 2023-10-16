#WLO plotting
#Author: Xi-Feng Cha
#Begun coding: 2023-Oct-16 10:46

import matplotlib.pyplot as Mplot
import time

"""
===Table of weather information===
#Description
1) I.T.: Temprature inside the Dome
2) O.T.: Temprature outside the Dome
3) I.H.: Humidity inside the Dome
4) O.H.: Humidity outside the Dome
5) P: Atmospheric Pressure
6) WS: Wind Speed
7) Rain: Rainfall per minite
8) Rrate: Intensity of Rainfall
9) iTHW: Temperature-Humidity-Wind Index
"""

#Raw File
date_1 = 20231014
date_2 = date_1 +1
Txt_1 = f"WLO{date_1}.txt"
Txt_2 = f"WLO{date_2}.txt"

#List of Value
datetime = [] #local date time
datatempin, datatempout = [], [] #temperature
datahumin, datahumout = [], [] #humidity
datapressure = [] #pressure
datarain, datarrate = [], [] #rain and rain rate
dataws = [] #wind speed
datathw = [] #heat index (temp-hum-wind index)

def WLOdata(file):
      with open(file, "r") as wlodata:
            data = wlodata.readlines()
            for i in range(17, len(data)-1):
                  value = data[i].replace("[", "").replace("]", "").replace("\n", "").split(", ")
                  datetime.append(value[0])
                  for N in range(1, len(value)):
                        if N == 1:
                              datatempin.append(float(value[N]))
                        elif N == 2:
                              datatempout.append(float(value[N]))
                        elif N == 3:
                              datahumin.append(float(value[N]))
                        elif N == 4:
                              datahumout.append(float(value[N]))
                        elif N == 5:
                              datapressure.append(float(value[N]))
                        elif N == 6:
                              dataws.append(float(value[N]))
                        elif N == 7:
                              datarain.append(float(value[N]))
                        elif N == 8:
                              datarrate.append(float(value[N]))
                        elif N == 9:
                              datathw.append(float(value[N]))
            print(f"Success to loading the datas in {file}")
                              
WLOdata(Txt_1)
WLOdata(Txt_2)
time.sleep(2)

#Plotting the figure
print("[1] Temperature\n[2] Humidity\n[3] Pressure\n[4] Wind speed\n[5] Rain\n")

Mplot.grid(True)
Mplot.xlabel("Datetime (GMT+8)")
while True:
      num =  int(input("which one do you want to plot?: "))
      if num == 1:
            Mplot.scatter(datetime, datatempin, c="blue", label = "Inside the Dome")
            Mplot.scatter(datetime, datatempout, c="red", label = "Outside the Dome")
            #Mplot.scatter(datetime, datathw, c="purple", label = "Heat index")
            Mplot.title("Temperature in Lulin Observatory")
            Mplot.ylim(0, 40)
            Mplot.ylabel("Temperature (Celsius)")
            Mplot.legend()
            Mplot.xticks(["'2023-10-14T00:00:00'", "'2023-10-14T06:04:00'", "'2023-10-14T12:00:00'", "'2023-10-14T18:00:00'", "'2023-10-15T00:00:00'", "'2023-10-15T06:00:00'", "'2023-10-15T12:07:00'", "'2023-10-15T18:08:00'"], rotation = 20)
            Mplot.show()
            break
      elif num == 2:
            Mplot.scatter(datetime, datahumin, c="blue", label = "Inside the Dome")
            Mplot.scatter(datetime, datahumout, c="red", label = "Outside the Dome")
            Mplot.title("Humidity in Lulin Observatory")
            Mplot.ylim(0, 100)
            Mplot.ylabel("Humidity (%)")
            Mplot.legend()
            Mplot.xticks(["'2023-10-14T00:00:00'", "'2023-10-14T06:04:00'", "'2023-10-14T12:00:00'", "'2023-10-14T18:00:00'", "'2023-10-15T00:00:00'", "'2023-10-15T06:00:00'", "'2023-10-15T12:07:00'", "'2023-10-15T18:08:00'"], rotation = 20)
            Mplot.show()
            break
      elif num == 3:
            Mplot.plot(datetime, datapressure, "o-")
            Mplot.title("Atmospheric pressure in Lulin Observatory")
            Mplot.ylabel("Atmospheric pressure (mb)")
            Mplot.xticks(["'2023-10-14T00:00:00'", "'2023-10-14T06:04:00'", "'2023-10-14T12:00:00'", "'2023-10-14T18:00:00'", "'2023-10-15T00:00:00'", "'2023-10-15T06:00:00'", "'2023-10-15T12:07:00'", "'2023-10-15T18:08:00'"], rotation = 20)
            Mplot.show()
            break
      elif num == 4:
            Mplot.plot(datetime, dataws, "ro-")
            Mplot.title("Wind Speed in Lulin Observatory")
            Mplot.ylabel("Wind Speed (m/s)")
            Mplot.xticks(["'2023-10-14T00:00:00'", "'2023-10-14T06:04:00'", "'2023-10-14T12:00:00'", "'2023-10-14T18:00:00'", "'2023-10-15T00:00:00'", "'2023-10-15T06:00:00'", "'2023-10-15T12:07:00'", "'2023-10-15T18:08:00'"], rotation = 20)
            Mplot.show()
            break
      elif num == 5:
            Mplot.bar(datetime, datarain)
            Mplot.title("Rain in Lulin Observatory")
            Mplot.ylim(0, 2)
            Mplot.ylabel("Rain (mm)")
            Mplot.xticks(["'2023-10-14T00:00:00'", "'2023-10-14T06:04:00'", "'2023-10-14T12:00:00'", "'2023-10-14T18:00:00'", "'2023-10-15T00:00:00'", "'2023-10-15T06:00:00'", "'2023-10-15T12:07:00'", "'2023-10-15T18:08:00'"], rotation = 20)
            Mplot.show()
            break
      else:
            print("Exceed range, try again!")
            continue

#Latest update: 2023-Oct-16 21:18



