from sanic import Sanic
from sanic.response import json
from work import load_assets, shuffle_assets, generate_data
import os

app = Sanic()

@app.route('/generate')
async def generate(request):
    
    filters = {}
    if request.args:
        filters = {}
        for arg in request.raw_args:
            filters[arg] = request.raw_args[arg].split(",")
    
    output = generate_data(filters)
    return json(output)


if __name__ == '__main__':

    load_assets()
    shuffle_assets()

    app.run(host='0.0.0.0', port=8000, workers=4)