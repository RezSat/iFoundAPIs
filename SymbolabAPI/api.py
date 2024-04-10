import requests
import json
import urllib.parse

def string_to_query(text):
    # Replace spaces with plus signs and escape special characters
    return urllib.parse.quote_plus(text)

def query_to_string(query_text):
    # Replace plus signs with spaces and unescape special characters
    return urllib.parse.unquote_plus(query_text)

def requestToken():
    url = "https://scibug.com/api/mobile/token"

    payload = {}
    headers = {
    'Cookie': 'sy.platform=Android; sy.app=Symbolab%2F9.6.1.2788; sy.device=HUAWEI_CAM-L21; sy.os=6.0_(23); sy.installation=faf11e93-0b08-45ea-816e-3a22572602ce; sy.orientation=portrait; sy.store.approved=true; sy2.decimal=5; sy2.variation=1; PLAY_SESSION=d49eb73365709e99c59294e985fd4b0b4de51c42-___ID=ba120288-67b1-4312-8c7e-2722366188bc; sy2.app=Symbolab%2F9.6.1.2788; sy2.device=HUAWEI_CAM-L21; sy2.installation=faf11e93-0b08-45ea-816e-3a22572602ce; sy2.orientation=portrait; sy2.os=6.0_(23); sy2.platform=Android; sy2.pub.token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3d3dy5zeW1ib2xhYi5jb20iLCJ1ZGlkIjpudWxsLCJzdWJzY3JpYmVkIjpudWxsLCJleHAiOjE3MDc4NTIxMjN9.8jZwi726c4O4YsLHpTAfLRCQKJqSkQTvsgQ_Yj2tQzo; sy2.token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3d3dy5zeW1ib2xhYi5jb20iLCJ1ZGlkIjpudWxsLCJzdWJzY3JpYmVkIjpudWxsLCJleHAiOjE3MDc3MzAyMjR9.qsv0ZKoQn9vuFVsBwtxiYM0cqet1FYFl2PFYjAJA_kY; sy2.variation=1',
    'Host': 'scibug.com',
    'User-Agent': 'okhttp/4.9.3'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)['jwt']


def detailLog(token):
    url = "https://scibug.com/detailedLog"
    payload = 'query=&subtopic=&subject=&connected=&topic=&language=en&info1=Key&responseTimeMs=0&type=Pad&info2=Basic_2'
    geneated_cookies = {
        'sy.platform':'Android',
        "sy.app":"Symbolab%2F9.6.1.2788",
        "sy.device":"HUAWEI_CAM-L21",
        "sy.os":"6.0_(23)",
        "sy.installation":"faf11e93-0b08-45ea-816e-3a22572602ce",
        "sy.orientation":"portrait",
        "sy.store.approved":"true",
        "sy2.decimal":'5',
        "sy2.token":token,
        "sy2.pub.token": token,
        "sy2.variation":"1",
    }
    cookies_str = "; ".join([f"{key}={value}" for key, value in geneated_cookies.items()])
    headers = {
        'Host': 'scibug.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'okhttp/4.9.3',
        'Cookie': cookies_str
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response
    

def Symbolab(query):
    url = f"https://scibug.com/pub_api/steps?query={query}&language=en&userId=fe&license=Unlimited&origin=input&plotRequest=PlotOptional&page=z3.a%3Cjava.lang.String%3E"

    token=requestToken()
    geneated_cookies = {
        'sy.platform':'Android',
        "sy.app":"Symbolab%2F9.6.1.2788",
        "sy.device":"HUAWEI_CAM-L21",
        "sy.os":"6.0_(23)",
        "sy.installation":"faf11e93-0b08-45ea-816e-3a22572602ce",
        "sy.orientation":"portrait",
        "sy.store.approved":"true",
        "sy2.decimal":'5',
        "PLAY_SESSION":detailLog(token).cookies.get("PLAY_SESSION"),
        "sy2.variation":"1",
        "sy2.token":token,
        "sy2.pub.token": token,
    }
    cookies_str = "; ".join([f"{key}={value}" for key, value in geneated_cookies.items()])

    payload = {}
    headers = {
    'Host': 'scibug.com',
    'User-Agent': 'okhttp/4.9.3',
    'Cookie': cookies_str
    }

    response = requests.request("GET", url, headers=headers)
    return response.text