from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

app = Flask(__name__)


lastTelephone = "Oh Hello World"

query = ''.join(lastTelephone.split())

account_sid = 'AC7119e83de9a686d0d56bc8491d80526a'
auth_token = 'fcf3e5c1691051282836a49d26ff38c4'
client = Client(account_sid, auth_token)

call = client.calls.create (
        url = 'https://handler.twilio.com/twiml/EH06f621851a96b743015a43371effcf68?Message=' + query,  
        to='+17205142454',
        from_='+17207704132'
                )

print(call.sid)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a 'Hello world' message"""
    
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say(query)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
