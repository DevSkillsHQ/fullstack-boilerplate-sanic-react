from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS

app = Sanic("My-Hello-World-App")
CORS(app)

@app.route('/ping')
async def test(request):
    return json({'result': 'pong'})

if __name__ == '__main__':
    app.run()