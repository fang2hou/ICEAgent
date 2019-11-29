#  Copyright (c) 2019. Zhou Fang
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights to
#  use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#  of the Software, and to permit persons to whom the Software is furnished to
#  do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.

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
