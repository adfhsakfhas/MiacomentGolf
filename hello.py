import os
import requests
import bs4
from bs4 import BeautifulSoup
import html
import json


def checkTimes(Date, NumOfPlay, NumOfHoles, StartTime, EndTime):
    paynoal = {"date":Date,"numHoles":NumOfHoles,"numPlayers":NumOfPlay,"startTime":StartTime,"endTime":EndTime,"courseIDs":[2717]}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    with requests.Session() as s:
        choo = s.post(url='https://miacomet.ezlinksgolf.com/api/search/search', data=paynoal, headers= headers)
        choo = choo.content
        
        
        choo2 = choo.decode("utf-8")
        
        text_file = open("data.json", "w")
        text_file.write(choo2)
        text_file.close()
        f = open('data.json')
        data = json.load(f)
        f.close()
        x = 0
        for (k, v) in data.items():
            if k == "Reservations":
                #print(v)
                hi = v
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
        file2 = open("file2.json", "w")
        hi = json.dumps(hi)
        file2.write(hi)
        file2.close
        file2 = open("file2.json", "r")
        helpme = json.load(file2)
        file2.close
        x = 0
        for k in helpme:
            x+=1
            with open("proccesing{}.json".format(x), "w") as fip:
                json.dump(k, fip)
                fip.close
        y = 1
        finished_list = {}

        while y <= x:
            
            print("")
            with open("proccesing{}.json".format(y), "r") as fipr:
                current = json.load(fipr)
                fipr.close
                plsno = {
                    'ReservationNumber': current.get("RecNo"), 
                    'TeeDate': current.get("TeeDateDisplay"),
                    'TeeTime': current.get("TeeTimeDisplay"),
                    'Combine': current.get("TeeTime")
                }
                print(plsno)
                print("")
                finished_list[plsno.get("ReservationNumber")] = plsno
            
            y+=1
        print("")
        with open("finishedProcessing.json", "w") as just:
            json.dump(finished_list, just)
        zz=0

        while zz <10:
            print("")
            zz+=1
        print(finished_list)
        return x
        
        
                            
                    
            

        


