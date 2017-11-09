from bs4 import BeautifulSoup
import requests
import os
import json
import sqlite3
import time

try:
    conn = sqlite3.connect("bmtc.db")
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS fares')
    c.execute('CREATE TABLE fares(Stage INTEGER, Adults INTEGER, Child INTEGER, Senior INTEGER)')
except:
    print("Database Connection error")
    os._exit(1)

print("enter the type of bus")
bustype=input()

if (bustype=='A/C'):
    url1="https://www.mybmtc.com/ac-service?fareid=acs&qt-home_quick_tab_bottom=2"
elif (bustype=='General'):
    url1="https://www.mybmtc.com/general-service?fareid=gns&qt-home_quick_tab_bottom=2"
else:
    print("Please Type valid bus service")
    os._exit(1)


data = []
req1=requests.get(url1)
data1 =req1.text
soup=BeautifulSoup(data1,"html.parser")
table=soup.find_all('table')[:2]
for i in table:
    sub_data=[]
    rows = i.find_all('tr')[1:]

    for row in rows:
   
        cols = row.find_all('td')
        #print(cols)
        #cols = [ele.text.strip() for ele in cols]
        #data.append([ele for ele in cols if ele])

        tab_row = {}
        tab_row["Fare Stage Number"]=cols[0].get_text()
        tab_row["Adults"]=cols[1].get_text()
        tab_row["Child"]=cols[2].get_text()
        try:
            tab_row["Senior Citizen"]=cols[3].get_text()
        except:
            tab_row["Senior Citizen"]="0"
        
        sub_data.append(tab_row)
        try:
            c.execute("INSERT INTO fares (Stage, Adults, Child, Senior) values (? , ? , ? , ?)", (tab_row["Fare Stage Number"],tab_row["Adults"],tab_row["Child"],tab_row["Senior Citizen"] )  )
        except:
            print("Can't insert into database")
    data.append(sub_data)

time.ctime()
timestr = time.strftime("%b_%d_%Y")
fare="bmtc_fare_scrap_"+timestr

with open(fare+'.json', 'w') as outfile:
    json.dump(data, outfile)

conn.commit()

c.close()
conn.close()

