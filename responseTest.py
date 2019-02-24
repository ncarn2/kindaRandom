from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

app = Flask(__name__)

message = "Hello, This is a Test. Electric Boogaloo!"

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a 'Hello world' message"""
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    call - client.calls.create (
            url = 'twiml.xml',   
            to='+17205142454',
            from_='+17207704132'
                    )

    print(call.sid)
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say(message)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
