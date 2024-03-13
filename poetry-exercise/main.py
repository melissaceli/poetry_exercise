from flask import Flask, request, Response
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"


@app.get("/translate")
def translate_text():
    if 'language' not in request.args or 'text' not in request.args:
        return Response("Bad request",status=400,)
    language = request.args.get('language')
    text = request.args.get('text')
    translated = GoogleTranslator(source='auto', target=language).translate(text)
    return {"language": language, "translated": translated}


if __name__ == '__main__':
    app.run()
