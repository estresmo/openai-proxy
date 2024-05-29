from flask import Flask, request
import requests
import urllib.parse

app = Flask(__name__)

methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']

@app.route('/', defaults={'path': ''})
@app.route("/<string:path>", methods=methods)
@app.route('/<path:path>', methods=methods)
def general(path):
    print(request)
    headers = request.headers
    BASE_URL = 'https://api.openai.com/v1/'
    new_url = urllib.parse.urljoin(BASE_URL, path)
    resp = requests.request(request.method, new_url, headers=headers, data=request.data)
    return  resp.content, resp.status_code, resp.headers.items()


if __name__ == '__main__':
    app.run(port=4999, debug=True)