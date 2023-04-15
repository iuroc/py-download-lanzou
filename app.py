from flask import Flask, request, redirect
from lanzou import get_down_url

app = Flask(__name__)


@app.route('/down')
def index():
    file_id = request.args.get('id')
    down_url = get_down_url(file_id)
    return redirect(down_url)


if __name__ == '__main__':
    app.run()
