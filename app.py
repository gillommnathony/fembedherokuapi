from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix
import json, time
import lk21

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/', methods=['GET'])


def home_page():
    data_set = {'Page': 'Home', 'Message': 'This is Home Page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/fembed/', methods=['GET'])

def request_page():
    user_query = str(request.args.get('url'))
    bypasser = lk21.Bypass()
    dl_url =bypasser.bypass_fembed(user_query)
    lst_link = []
    for i in dl_url:
        lst_link.append(dl_url[i])




    data_set = dl_url
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == '__main__':
    app.run()
