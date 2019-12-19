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

from flask import Blueprint, request

fu_bridge = Blueprint('fu_bridge', __name__)


class FightingICEUkiBridge:
    """ The communication bridge between FightingICE and UKI.

    This object provides a instance to persistent the data and use simple http
    request to make the communication easier.

    """
    def __init__(self):
        """Initialize the object."""
        self.data = ''

    def save(self, text: str):
        """Save the data with text

        :param text: A data string.
        """
        self.data = text

    def get(self):
        """Read the data saved.

        :return: A data string.
        """
        return self.data


bridge = FightingICEUkiBridge()


@fu_bridge.route('/save', methods=['POST'])
def save():
    if request.method != 'POST':
        return 'Use POST to submit requests.'

    try:
        data = request.form['data']
        bridge.save(data)
        return 'Saved'
    except KeyError:
        return "Save is failed."

@fu_bridge.route('/read', methods=['GET'])
def read():
    if request.method != 'GET':
        return 'Use GET to submit requests.'

    return bridge.get()
