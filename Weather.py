import requests
from datetime import datetime
import pymongo

api_Key = "5c1523e79e4fc459d20d3d6f784e3337"
location = input("Enter the city name: ")
# Date = int(input("Enter a Date: "))

Url = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_Key
api_link = requests.get(Url)
api_data = api_link.json()

Date = int(datetime.now().strftime("%d"))
for i in range (2, Date):
    if Date % i == 0:
        print("Date is Not Prime so no date")
        break
else:
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    
    print ("-------------------------------------------------------------")
    print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print ("-------------------------------------------------------------")
    print (api_data)
    
    # ************************* MongoDB Database*********************
    
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["W_Data"]
    mycol = mydb["Weateher_Data"]
    mydict = (api_data)
    x = mycol.insert_one(mydict)
    print("\nAudit Data Added in Database..!")
