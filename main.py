from modules.fightingice_uki_bridge import fu_bridge
from modules.icetts import icetts
from flask import Flask

app = Flask(__name__)
app.register_blueprint(fu_bridge, url_prefix='/fu_bridge')
app.register_blueprint(icetts, url_prefix='/icetts')


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(port=1688, debug=True)
