import requests
import re
from http.cookiejar import LWPCookieJar


session = requests.Session()
session.headers[
    "User-Agent"] = "Mozilla/5.0 (Linux; Android 7.0; 5060 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"
session.cookies = LWPCookieJar()
def bypass_redirect(url):
        """
        regex: https?://bit\.ly/[^>]+
        regex: https?://(?:link\.zonawibu\.cc/redirect\.php\?go|player\.zafkiel\.net/blogger\.php\?yuzu)\=[^>]+
        """
        head = session.head(url)
        return head.headers.get("Location", url)
def bypass_fembed(url):
        """
        regex: https?://(?:www\.naniplay|naniplay)(?:\.nanime\.(?:in|biz)|\.com)/file/[^>]+
        regex: https?://layarkacaxxi\.icu/[fv]/[^>]+
        regex: https?://fem(?:bed|ax20)\.com/[vf]/[^>]+
        """

        url = url.replace("/v/", "/f/")
        raw = session.get(url)
        api = re.search(r"(/api/source/[^\"']+)", raw.text)
        if api is not None:
            result = {}
            raw = session.post(
                "https://layarkacaxxi.icu" + api.group(1)).json()
            for d in raw["data"]:
                f = d["file"]
                direct = bypass_redirect(f)
                result[f"{d['label']}/{d['type']}"] = direct
            return result

urls = bypass_fembed('https://www.fembed.com/v/zdgj3hj4m-ydgjg')
print(urls)
