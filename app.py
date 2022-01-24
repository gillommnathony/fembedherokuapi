from flask import Flask, request
import json, time
import lk21

app = Flask(__name__)

@app.route('/', methods=['GET'])

def home_page():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    data_set = {'Page': 'Home', 'Message': f'Home Page And IP :  {ip}', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/fembed/', methods=['GET'])

def request_page():
    user_query = str(request.args.get('url'))
    bypasser = lk21.Bypass()
    dl_url =bypasser.bypass_fembed(user_query)
    json_dump = json.dumps(dl_url)
    return json_dump

if __name__ == '__main__':
    app.run()
