# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
import requests
import route_parser
from twilio.twiml.voice_response import VoiceResponse, Say
#from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
import urllib
import re
import shutil
from flask import send_from_directory
from flask import send_file
import string, random
import base64
import json
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""

    if request.form['NumMedia'] != '0':
  image1 = request.form['MediaUrl0']        
        the_url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction/58efabf4-d519-417c-8f4f-5a4550cac311/url?iterationId=35d96f2d-3e3f-4178-9e97-8b2635207616"
        res = requests.post(url = the_url,
                    data=json.dumps({"Url":image1}),
                    headers={'Content-Type': 'application/json',"Prediction-Key":"5dddbd7652e24ea99576c57ef9fb381a"})
        print(res.json())    
        return "dummy"

    else:
      # Start our response
      body = request.values.get('Body', None) 
      body = body.lower()
      #from_text = re.search(r'from(.*?)to', body).group(1)
      #dest_text =  body.split("to",1)[1]
      grp = re.search(r'from(.*?)to(.*?)by(.*?)',body)
      from_text = grp.group(1)
      dest_text = grp.group(2)
      if (grp.group(3)):  
      mode = body.split("by",1)[1]
      else:
    mode = None
      print from_text
      print dest_text
      print mode
      if(mode == "walk"):
    md = "Walking"
      else:
    md = "Driving"
      print md
      response = MessagingResponse()
      message_directions = Message()
      message_mapImage = Message()
   # message.body('Store Location: 123 Easy St.')
   # message.media(request.form["MediaUrl0"])
   # response.append(message)
      r = requests.get("http://dev.virtualearth.net/REST/V1/Routes/"+md+"?wp.0="+from_text+"&wp.1="+dest_text+"&optmz=distance&routeAttributes=routePath&key=AmAugBLaNYZ5kK48nDsSyH2IkXZTMgLdevV0cwJkIohl5A4hitqxiCmKhDAAq7cr")
      data = r.json() 
    #print data
      message_directions.body(route_parser.extract_path((data)))
      response.append(message_directions)
    #print(str(data))
    #print str(response)
    
    
    #static image
      image_request = requests.get("https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0="+from_text+"&wp.1="+dest_text+"&key=AmAugBLaNYZ5kK48nDsSyH2IkXZTMgLdevV0cwJkIohl5A4hitqxiCmKhDAAq7cr")
   # print(image_request.text)
      name = ''.join(random.sample(string.ascii_lowercase, 10)) + ".jpg"
      with open("img/"+name, 'wb') as out_file:
        out_file.write(image_request.content)
   # message_mapImage.body('Image of the route')
      message_mapImage.media("http://159.65.68.139:5000/uploads/{}".format(name))
      response.append(message_mapImage)
    #res1 = str(response) 
    #print res1 
      return str(response)

@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
   # return send_from_directory("home/karan/twilio/img",
    #                           "robo.jpg"
   return send_file("img/"+filename, mimetype='image/jpg')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")



