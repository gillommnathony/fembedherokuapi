from flask import Flask, request
import json, time
import lk21
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
app = Flask(__name__)
if request.headers.getlist("X-Forwarded-For"):
    ip = request.headers.getlist("X-Forwarded-For")[0]
else:
    ip = request.remote_addr
app.asgi_app = ProxyHeadersMiddleware(app.asgi_app, trusted_hosts=[f"{ip}"])
@app.route('/', methods=['GET'])


def home_page():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    data_set = {'Page': 'Home', 'Message': f'This is Home Page {ip}', 'Timestamp': time.time()}
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
