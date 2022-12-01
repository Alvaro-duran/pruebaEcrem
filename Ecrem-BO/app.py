from flask import Flask, jsonify, request
import time
from ua_parser import user_agent_parser
import pprint
from topic.topicApi import sendTopic
from geopy.geocoders import Nominatim

import requests
import json
import datetime
import csv

def UrlCsv(url,title,time):
   myFile = open('./UrlData.csv', 'r+')
   print(myFile.read())
   myDict = {'Url':url, 'Title': title,'Time':time}
   writer = csv.writer(myFile)
   writer.writerow(myDict.values())
   myFile.close()


app = Flask(__name__)
url_timestamp = {}
url_viewtime = {}
prev_url = ""
UrlUser=list()
timeUrls=list()
titleList=list()
def url_strip(url):
    if "http://" in url or "https://" in url:
        url = url.replace("https://", '').replace("http://", '')
    #if "/" in url:   // para quitar a partir de /
        #url = url.split('/', 1)[0]
    return url




@app.route('/send_location', methods=['POST'])
def send_location():

    
    resp_json = request.get_data()
    params = resp_json.decode()

    lenData=(len(params))
    pos=params.index("title:")
    title=(params[pos+6:lenData])
    params=params.replace(title,"")
    params=params.replace("title:","")  

    lenData=(len(params))
    pos=(params.index("url:"))
    url=(params[pos+4:lenData])
    params=params.replace(url,"")
    params=params.replace("url:","")

    lenData=(len(params))
    pos=(params.index("long:"))
    lon=(params[pos+5:lenData])
    params=params.replace(lon,"")
    params=params.replace("long:","")

    lenData=(len(params))
    pos=(params.index("lat:"))
    lat=(params[pos+4:lenData])
    params=params.replace(lat,"")
    params=params.replace("lat:","")


    print("currently viewing: " + url_strip(url))
    parent_url = url_strip(url)

    titleList.append(title)

    so=str(request.user_agent)
    
    
    pp = pprint.PrettyPrinter(indent=4)
    ua_string = so
    parsed_string = user_agent_parser.Parse(ua_string)
    pp.pprint(parsed_string)

    UrlUser.append(parent_url)
    print(UrlUser)
    global url_timestamp
    global url_viewtime
    global prev_url

    print("initial db prev tab: ", prev_url)
    print("initial db timestamp: ", url_timestamp)
    print("initial db viewtime: ", url_viewtime)

    if parent_url not in url_timestamp.keys():
        url_viewtime[parent_url] = 0

    if prev_url != '':

        geolocator = Nominatim(user_agent="app.py")
        location = geolocator.reverse(str(lat)+","+str(lon))
        print(location.address)
        address=location.address
        
        time_spent = int(time.time() - url_timestamp[prev_url])
        url_viewtime[prev_url] = url_viewtime[prev_url] + time_spent

        titlePrev=titleList[len(titleList)-2]

        topic=sendTopic(titlePrev)

        print(titleList)
        print(topic)
        print(titlePrev)
        print(title)
        print(prev_url)
        print(time_spent)
        
        if topic !=8:
        
            #UrlCsv(url,titlePrev,time_spent)
            #publishData(prev_url,titleCsv,time)

            todaydate=str(datetime.datetime.utcnow().isoformat() + "Z")


            url = "http://176.31.144.113:8099/api/memories"

            payload = json.dumps({
                "data": {
                "userId": "1",
                "title": str(titlePrev),
                "url": str(prev_url),
                "date": todaydate,
                "timeInMinutes": time_spent,
                "topic":str(topic),
                "geolocation": {
                                "latitude": str(lat),
                                "longitude": str(lon),
                                "address": address
                            }
                }
            })

            headers = {
                'accept': 'application/json',
                'Content-Type': 'application/json'
                }

            #response = requests.request("POST", url, headers=headers, data=payload)
            response=  requests.post(url,headers=headers, data = payload)
            print(response.text)
 

            timeUrls.append(time_spent)
        else:
            print("irrelevant")
            print(topic)
            timeUrls.append(time_spent)

    b = int(time.time())

    print(b)
    url_timestamp[parent_url] = b
    prev_url = parent_url
    print("final timestamps: ", url_timestamp)
    print("final viewtimes: ", url_viewtime)

    

    #41.9212968 -4.4902875 chrome://settings/ Configuración

    


    return jsonify({'message': 'success!'}), 200



@app.route('/quit_url', methods=['POST'])
def quit_url():
    resp_json = request.get_data()
    print("Url closed: " + resp_json.decode())
    return jsonify({'message': 'quit success!'}), 200

app.run(host='0.0.0.0', port=5000)