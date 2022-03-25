from sanic import Sanic
from sanic.response import json

app = Sanic("My Hello, world app")

@app.route('/ping')
async def test(request):
    return json({'result': 'pong'})

if __name__ == '__main__':
    app.run()