from flask import Blueprint, request

import gcloud

icetts = Blueprint('icetts', __name__)

tts = gcloud.playableTTSService()


def get_conf_by_key(request, arg):
    try:
        return request.args[arg]
    except KeyError:
        return None


@icetts.route('/play', methods=['POST'])
def play_tts():
    if request.method != 'POST':
        return "Use POST to submit requests."

    tts_opts = gcloud.TTSServiceOptions(
        language_code=get_conf_by_key(request, 'language_code'),
        voice_name=get_conf_by_key(request, 'voice_name'),
        pitch=get_conf_by_key(request, 'pitch'),
        volume_gain_db=get_conf_by_key(request, 'gain'),
        speaking_rate=get_conf_by_key(request, 'rate'),
    )
    tts.update_options(tts_opts)
    tts.speak(request.args['text'])
    return 'TTS is playing.'
