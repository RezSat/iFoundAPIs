from config import *
import requests
import json

def upload_image(file):
    payload = {'no_resize': '1'}
    files=[
        ('image',('1eef9d23-3db6-4a10-aeda-33dc221a4047',open(file,'rb'),'application/octet-stream'))
    ]
    headers = {
        'Host': TEMP_BASE_URL,
        'User-Agent': 'photoLabFreeAndroid-v9056',
        'Content-Length': '67216',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'close'
    }

    response = requests.request("POST", TEMP_UPLOAD_URL, headers=headers, data=payload, files=files)
    if response.status_code == 200:
        print("Upload Success!")
        return json.loads(response.text)
    else:
        print("Upload Fail!")
        return json.loads(response.text)
