from twilio.twiml.voice_response import VoiceResponse, Say

response = VoiceResponse()
response.say('Welcome to Hacktech 2018', voice='woman', language='fr')

print(response)