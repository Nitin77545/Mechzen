# accounts/utils.py
import requests

FAST2SMS_API_KEY = 'G9CjxVkgKhRUB28EuZP4ITaerDzsFylq3O5Lfb7Mwtdc106XQNmuXs2HzZ9IpVRvtkx7a8fKiLCodeGN'

def send_otp(phone_number, otp):
    url = "https://www.fast2sms.com/dev/bulkV2"
    headers = {
        "authorization": FAST2SMS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "route": "v3",
        "sender_id": "FSTSMS",
        "message": f"Your OTP is {otp}",
        "numbers": phone_number
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
