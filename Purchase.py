import requests
import json
test_ = {"CourseID":2717,"TeeTime":"2020-12-01T09:24:00","ReservationDate":"2020-12-01T00:00:00","Sponsors":[{"SponsorID":1728,"FlatRateIcons":3,"ReservationTypeID":11996,"FeeID":155058,"FlatRate":-1,"FlatRateFeeID":433813,"ValueIconString":"3"}],"SessionID":"ne4kb3zmez2foohbskxynojc"}
with open("Test.json") as f:
    Testing = json.load(f)
Payload = {"Login":"Number1GolferOfTheWorld","Password":"chamChap906","SessionID":"","MasterSponsorID":"1728"}
with requests.Session() as s:
        whattttt = s.post('https://miacomet.ezlinksgolf.com/api/login/login', Payload)
        print(whattttt.content.decode("utf-8"))
        kool = json.loads(whattttt.content.decode("utf-8"))
        hi = dict(kool)
        #print(hi)
        SESID = (hi.get("SessionID"))
        CRCF = (hi.get("CsrfToken"))
        test_['SessionID'] = SESID
        okboomer = s.post("https://miacomet.ezlinksgolf.com/api/search/reservation", test_)
        print(okboomer.content.decode("utf-8"))
        Testing['SessionID'] = SESID
        Testing['CsrfToken'] = CRCF
        wahtRo = s.post("https://miacomet.ezlinksgolf.com/api/cart/add", Testing)
        print(wahtRo.content.decode("utf-8"))