# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
import requests
#from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    body = request.values.get('Body', None)
    info = body.split()
    from_text = str(info[0].split(':'))
    dest_text = str(info[1].split(':'))
    response = MessagingResponse()
    message = Message()
   # message.body('Store Location: 123 Easy St.')
   # message.media(request.form["MediaUrl0"])
   # response.append(message)
    source_location = "Minneapolis"
    dest_location = "St. Paul"
    r = requests.get("http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0="+from_text+"&wp.1="+dest_text+"&optmz=distance&routeAttributes=routePath&key=AmAugBLaNYZ5kK48nDsSyH2IkXZTMgLdevV0cwJkIohl5A4hitqxiCmKhDAAq7cr")
    data = r.json() 
    message.body(str(r.status_code))   
    response.append(message)
    print(str(data))
    return str(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
