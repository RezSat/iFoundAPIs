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
    
def trending_filters():
    params = {
      "idfa": "",
      "app_id": 1,
      "aid": "214c711bbb764b38205cdf206c98ce46",
      "plid": "83293f35-8454-43b5-b513-2b816cb10389",
      "config_id": "hk-1104241601",
      "config_dt": "2024-04-11T16%3A03%3A52",
      "session_idx": 3,
      "param5": 0,
      "param6": 44287720,
      "last_tab": "compositions",
      "photo_chooser_id": 2,
      "processing_ad_idx": 0,
      "postprocessing_ad_idx": 0,
      "smart_fs": -1,
      "icu": 0,
      "installer": "",
      "is_low": 1,
      "ishk": 1,
      "af_uid": "1712993725956-3116072534899486430",
      "th_fab_shape": "rounded",
      "th_fab_bg": "D3E3FF",
      "th_fab_ic": "001C3B",
      "th_primary": "005FB1",
      "cc": 1,
      "ccb": "h"
    }
    
    url = f"{API_1_URL}/channel/photolab"

    headers = {
        'Host': SOCIAL_API_URL,
        'User-Agent': USER_AGENT,
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'close'
    }

    try:
      response = requests.get(url, params=params+default_configs(), headers=headers)
      response.raise_for_status()  # Raise an exception for non-2xx status codes
      print(response.text)
    except requests.exceptions.RequestException as e:
      print(f"Error fetching trending filters: {e}")
