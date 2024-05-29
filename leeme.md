# OPENAI PROXY
Este es un proxy para ejecutar la librería de OpenAI con la IP de un país restringido como lo es Venezuela.
Para que funcione necesitas subir este repositorio a un servidor web alojado en un país no restringido. 
Instalas las dependencias, ejecutas el servidor. Y luego en cualquier proyecto que quieras usar la librería de OpenAI, colocas como variable de entorno OPENAI_BASE_URL con la URL del proxy.

## Pre requisitos

- Python3 instalado


## Instalación

1. Clona el repositorio
2. Instala las dependencias
3. Ejecuta el servidor (Puedes colocar el puerto que quieras, o el host 0.0.0.0 para que sea publico)

```bash
git clone https://github.com/estresmo/openai-proxy.git
cd openai-proxy
pip install -r requirements.txt
gunicorn app:app -b 127.0.0.1:8000
```

## Uso

Puedes usarlo de dos formas:

1. Colocar la URL del proxy en la variable de entorno `OPENAI_BASE_URL` en tu proyecto.
```env
...
OPENAI_BASE_URL=http://127.0.0.1:8000/
```
2. o usar la librería de OpenAI de tu proyecto, y pasar la URL del proxy como parámetro.
```python
import openai
client = openai.Client(base_url="http://127.0.0.1:8000/")
```

## Ejemplo

https://estresmo.pythonanywhere.com/ Este es un servidor de prueba que puedes usar como proxy para probar esta librería

```env
...
OPENAI_BASE_URL=https://estresmo.pythonanywhere.com/ 
```
o 
```python
import openai
client = openai.Client(base_url="https://estresmo.pythonanywhere.com/ ")
```

Este servidor es solo para pruebas, por lo que no se garantiza que este funcionando siempre. De igual forma puedes hacer deploy gratuitamente en varios hostings.

## Hosting gratuito

- [PythonAnywhere](https://www.pythonanywhere.com/)
- [Railway](https://railway.app/)
- [Render](https://render.com/)
- [AWS](https://aws.amazon.com/) 

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Puedes encontrar el archivo de licencia en el directorio raíz del proyecto.