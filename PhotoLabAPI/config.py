TEMP_BASE_URL = 'temp.ws.pho.to'

TEMP_UPLOAD_URL = f"https://{TEMP_BASE_URL}/upload.php"

USER_AGENT = "photoLabFreeAndroid-v9056"

SOCIAL_API_URL = "photolabsocialapi.pho.to"

API_1_URL = f"https://{SOCIAL_API_URL}/api/v1"

OPEAPI_URL = "https://opeapi.ws.pho.to"

APP_VERSION = "3.13.6"

VERSION_CODE = 9056

DEVICE = "unknown_Pixel_5"

OS = "android"

OS_VERSION = "6.0"

OS_VERSION_CODE = 23

SCREEN_DENSITY = 2.7

SCREEN_W = 1080

SCREEN_H = 2210

IS_TABLET = 0

LANG_COUNTRY = "US"

LANG = "en"

NETWORK = "wifi"

ANDROID_ID = "b1ba0"

LOCALTZ = "America/New_York"

WEBVIEW_VERSION = "74.0.3729.186"

IS_PRO = 1

def default_configs(**kwargs):
    return {
        "app_version": kwargs.get("app_version", APP_VERSION),
        "version_code": kwargs.get("version_code", VERSION_CODE),
        "device": kwargs.get("device", DEVICE),
        "os": kwargs.get("os", OS),
        "os_version": kwargs.get("os_version", OS_VERSION),
        "os_version_code": kwargs.get("os_version_code", OS_VERSION_CODE),
        "screen_density": kwargs.get("screen_density", SCREEN_DENSITY),
        "screen_w": kwargs.get("screen_w", SCREEN_W),
        "screen_h": kwargs.get("screen_h", SCREEN_H),
        "is_tablet": kwargs.get("is_tablet", IS_TABLET),
        "lang_country": kwargs.get("lang_country", LANG_COUNTRY),
        "lang": kwargs.get("lang", LANG),
        "network": kwargs.get("network", NETWORK),
        "android_id": kwargs.get("android_id", ANDROID_ID),
        "localtz": kwargs.get("localtz", LOCALTZ),
        "webview_version":  kwargs.get("webview_version", WEBVIEW_VERSION),
        "is_pro": kwargs.get("is_pro", IS_PRO),
    }