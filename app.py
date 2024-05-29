from flask import Flask, request
import requests
import urllib.parse
from flask_compress import Compress, Cache

app = Flask(__name__)
app.config["COMPRESS_REGISTER"] = False  # disable default compression of all eligible requests
compress = Compress()
compress.init_app(app)

cache = Cache(app, config={
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 60*60  # 1 hour cache timeout
})
def get_cache_key(request):
    return request.url


compress.cache = cache
compress.cache_key = get_cache_key



methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']

@app.route('/', defaults={'path': ''})
@app.route("/<string:path>", methods=methods)
@app.route('/<path:path>', methods=methods)
@compress.compressed()
def general(path):
    print(request.headers)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': request.headers.get('Authorization')
    }
    BASE_URL = 'https://api.openai.com/v1/'
    new_url = urllib.parse.urljoin(BASE_URL, path)
    resp = requests.request(request.method, new_url, headers=headers, json=request.json, timeout=300)
    new_headers = dict(resp.headers)
    new_headers.pop('Content-Encoding', None)
    new_headers.pop('Transfer-Encoding', None)
    new_headers.pop('Connection', None)
    new_headers.pop('CF-Cache-Status', None)
    return  resp.content, resp.status_code, resp.headers.items()


if __name__ == '__main__':
    app.run(port=4999, debug=True)