from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route('/click-to-call', methods=['POST'])
def click_to_call():
    from_number = request.form['From']
    to_number = request.form['To']

    response = VoiceResponse()
    response.dial(to_number, caller_id=from_number)

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)