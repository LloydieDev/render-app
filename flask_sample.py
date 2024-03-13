from flask import Flask, request, jsonify

from flask_cors import CORS  # Import CORS from flask_cors
import requests


app = Flask(__name__)
CORS(app)

base_urls = "https://trual8.phdialer.com/vicidial/non_agent_api.php"

@app.route('/add_dnc_phone', methods=['POST'])
def add_dnc_phone():
    phone_number = request.json.get('phone_number')
    
    if not phone_number:
        return jsonify({"error": "Phone number not provided"}), 400
    

    responses = {}
    data = {
            "source": "TA",
            "function": "add_dnc_phone",
            "user": "IMMORTAL",
            "pass": "121252534232343",
            "phone_number": phone_number,
            "campaign_id": "SYSTEM_INTERNAL"
        }
    
        
    response = requests.post(base_urls, data=data)
    responses[base_urls] = {"status_code": response.status_code, "response_text": response.text}
    
    return jsonify(responses)

if __name__ == '__main__':
    app.run()
