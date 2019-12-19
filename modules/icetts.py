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

import gcloud

icetts = Blueprint('icetts', __name__, static_folder='../webapp/jimaku/')

tts = gcloud.PlayableTTSService()

def get_conf_by_key(resp: request, key):
    """ Get configuration by key

        Unpack the form data in a better way.

        Args:
            resp: A Flask request.
            key: A key to fetch form data.

        Returns: A string contains data mapping specific key or None if the key
                 is not included in request.

        """
    try:
        return resp.form[key]
    except KeyError:
        return None


# Check the site
# https://cloud.google.com/text-to-speech/docs/voices
@icetts.route('/play', methods=['POST'])
def play_tts():
    """ Play TTS

    Fetch audio from Google Cloud Text-to-speech service and play it.

    Returns: A message indicating whether the operation succeed or not.

    """
    if request.method != 'POST':
        return "Use POST to submit requests."

    tts_opts = gcloud.TTSServiceOptions(
        language_code=get_conf_by_key(request, 'language_code'),
        voice_name=get_conf_by_key(request, 'voice_name'),
        pitch=get_conf_by_key(request, 'pitch'),
        volume_gain_db=get_conf_by_key(request, 'gain'),
        speaking_rate=get_conf_by_key(request, 'rate'),
    )

    try:
        force = request.form['force']
        force = True if force == 'true' else False
    except KeyError:
        force = False

    try:
        text = request.form['text']
    except KeyError:
        print('No text found')
        return 'No text found.'

    tts.update_options(tts_opts)

    result = tts.speak(text, force)

    if result:
        print('[ICETTS] Now playing\n'
              'Language Code: {}\n'
              'Voice Name: {}\n'
              'Pitch: {}\n'
              'Volume Gain Db: {}\n'
              'Speaking Rate: {}\n'
              'Text: {}\n'
              '===================================='
              .format(tts_opts.language_code, tts_opts.voice_name, tts_opts.pitch,
                      tts_opts.volume_gain_db, tts_opts.speaking_rate, text)
              )

        return 'TTS is playing.'
    else:
        return 'TTS is now playing another audio.'


@icetts.route('/get/subtitle', methods=['GET'])
def subtitle_get():
    if request.method != 'GET':
        return "Use GET to submit requests."

    return tts.subtitle

@icetts.route('/jimaku', methods=['GET'])
def subtitle_index():
    return icetts.send_static_file('index.html')