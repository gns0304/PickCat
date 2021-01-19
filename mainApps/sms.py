import requests
import os
SMS_API_GATEWAY = 'https://sms.service.iwinv.kr/send/'
SMS_SENDER = os.environ.get('SMS_SENDER')
API_KEY = os.environ.get('SMS_API_KEY')

def sms(to,text):
    if not (API_KEY and SMS_SENDER):
        return 99
    headers = {
        'secret' : API_KEY,
    }
    i=0
    recv = ''
    if isinstance(to, list):
        for a in to:
            recv += f"{i}={a}&"
            i+=1
    else:
        recv = to
    data = {
        'from' : SMS_SENDER,
        'to' : recv,
        'text': text
    }
    files={'a' : None}
    status = requests.post(SMS_API_GATEWAY,data=data,headers=headers,files=files)
    return status.text