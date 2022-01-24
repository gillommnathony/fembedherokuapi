from flask import Flask, request
import json, time
import lk21
import requests
import re
from http.cookiejar import LWPCookieJar
# App is behind one proxy that sets the -For and -Host headers.

app = Flask(__name__)


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
    bypasser = lk21.Bypass()
    dl_url =bypasser.bypass_fembed(user_query)
    lst_link = []
    for i in dl_url:
        lst_link.append(dl_url[i])
    data_set = dl_url
    json_dump = json.dumps(data_set)
    json_obj = json.loads(json_dump)
    linkr = json_obj["480p/mp4"]
    print(linkr)

    return '''<video width="320" height="240" controls>
              <source src="{}" type="video/mp4">
              <source src="movie.ogg" type="video/ogg">
              Your browser does not support the video tag.
              </video>'''.format(linkr)

if __name__ == '__main__':
    app.run()
