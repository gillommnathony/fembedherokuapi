from flask import Flask, request
import json, time
import lk21
import requests
import re
from http.cookiejar import LWPCookieJar
# App is behind one proxy that sets the -For and -Host headers.

app = Flask(__name__)
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
                #direct = bypass_redirect(f)
                #result[f"{d['label']}/{d['type']}"] = direct
            return f

@app.route('/', methods=['GET'])

def home_page():
    data_set = {'Page': 'Home', 'Message': 'This is Home Page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/fembed/', methods=['GET'])

def request_page():
    session = requests.Session()
    session.headers[
        "User-Agent"] = "Mozilla/5.0 (Linux; Android 7.0; 5060 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"
    session.cookies = LWPCookieJar()
    user_query = str(request.args.get('url'))
  
    dl_url = bypass_fembed(user_query)
    print(dl_url)
    #data_set = dl_url
    #json_dump = json.dumps(data_set)
    #json_obj = json.loads(json_dump)
    #linkr = json_obj["480p/mp4"]
    #print(linkr)

    return '''<video width="320" height="240" controls>
              <source src="{}" type="video/mp4">
              <source src="movie.ogg" type="video/ogg">
              Your browser does not support the video tag.
              </video>'''.format(dl_url)

if __name__ == '__main__':
    app.run(debug=True)
