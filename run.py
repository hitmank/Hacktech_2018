# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse

#from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    
    response = MessagingResponse()
    message = Message()
    message.body('Store Location: 123 Easy St.')
    message.media(request.form["MediaUrl0"])
    response.append(message)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
