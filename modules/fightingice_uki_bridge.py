from flask import Blueprint, request

fu_bridge = Blueprint('fu_bridge', __name__)


class FightingICEUkiBridge:
    def __init__(self):
        self.data = ''

    def save(self, text: str):
        self.data = text

    def get(self):
        return self.data


bridge = FightingICEUkiBridge()


@fu_bridge.route('/save', methods=['POST'])
def save():
    if request.method != 'POST':
        return 'Use POST to submit requests.'

    bridge.save(request.args['data'])
    return 'Saved'


@fu_bridge.route('/read', methods=['GET'])
def read():
    if request.method != 'GET':
        return 'Use GET to submit requests.'

    return bridge.get()
