# OPENAI PROXY
This is a reverse proxy to run the OpenAI library with the IP of a restricted country such as Venezuela.
For it to work you need to upload this repository to a web server hosted in a non-restricted country. 
You install the dependencies, you run the server. And then in any project that you want to use the OpenAI library, you set the OPENAI_BASE_URL environment variable with the proxy URL.

(Para la versión en español, [lee aquí](https://github.com/estresmo/openai-proxy/blob/main/leeme.md))

## Pre requirements

- Python3 installed


## Installation

1. Clone the repository
2. Install the dependencies
3. Run the server (You can set the port you want, or the host 0.0.0.0 to make it public)

```bash
git clone https://github.com/estresmo/openai-proxy.git
cd openai-proxy
pip install -r requirements.txt
gunicorn app:app -b 127.0.0.1:8000
```

## Usage

You can use it in two ways:

1. Set the OPENAI_BASE_URL environment variable in your project.
```env
...
OPENAI_BASE_URL=http://127.0.0.1:8000/
```
2. or use the OpenAI library in your project, and pass the proxy URL as a parameter.
```python
import openai
client = openai.Client(base_url="http://127.0.0.1:8000/")
```

## Example

https://estresmo.pythonanywhere.com/ This is a test server that you can use as a proxy to test this repository

```env
...
OPENAI_BASE_URL=https://estresmo.pythonanywhere.com/
```
or
```python
import openai
client = openai.Client(base_url="https://estresmo.pythonanywhere.com/")
```

This server is only for testing, so it is not guaranteed that it will always work. You can also deploy it for free on various hostings.

## Free hosting

- [PythonAnywhere](https://www.pythonanywhere.com/)
- [Railway](https://railway.app/)
- [Render](https://render.com/)
- [AWS](https://aws.amazon.com/)


## License

This project is licensed under the MIT License. You can find the license file in the root directory of the project.