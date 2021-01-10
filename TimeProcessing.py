from datetime import datetime
import json

file2 = open("finishedProcessing.json", "r")
helpme = json.load(file2)
file2.close
dict(helpme)

#print(helpme)
def doIt(Total, BestCase):
    x = 1
    listthing = []
    seconds_in_day = 24 * 60 * 60
    while x <= Total:
        lol = helpme.get(str(x))
        #print(lol)
        x = x +1
        current_time_check = dict(lol).get("Combine")
        
        date_time_str = current_time_check.replace("T", " ")
        date_time_str = date_time_str.replace("-", "/")
        
        lolol = BestCase.replace("T", " ")
        lolol = lolol.replace("-", "/")
        #print(BestCase)
        #print(date_time_str)
        date_time_obj_best = datetime.strptime(lolol, '%Y/%m/%d %H:%M:%S')
        date_time_obj = datetime.strptime(date_time_str, '%Y/%m/%d %H:%M:%S')
        difference = abs(date_time_obj - date_time_obj_best) 
        hahahahaha = divmod(difference.days * seconds_in_day + difference.seconds, 60)
        listthing.append(hahahahaha[0])
    x = 1
    ratatatata = min(listthing)
    while x <= Total:
        lol = helpme.get(str(x))
        #print(lol)
        
        current_time_check = dict(lol).get("Combine")
        
        date_time_str = current_time_check.replace("T", " ")
        date_time_str = date_time_str.replace("-", "/")
        
        lolol = BestCase.replace("T", " ")
        lolol = lolol.replace("-", "/")
        
        date_time_obj_best = datetime.strptime(lolol, '%Y/%m/%d %H:%M:%S')
        date_time_obj = datetime.strptime(date_time_str, '%Y/%m/%d %H:%M:%S')
        difference = abs(date_time_obj - date_time_obj_best) 
        hahahahaha = divmod(difference.days * seconds_in_day + difference.seconds, 60)
        if (hahahahaha[0] == ratatatata):
            RecNo = current_time_check = dict(lol).get("ReservationNumber")
            return RecNo
        x = x +1
    print(listthing)
    print(ratatatata)
        
        



