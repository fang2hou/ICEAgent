
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
from google.cloud import texttospeech
import audioplayer


class TTSServiceOptions:

    def __init__(self,
                 language_code=None,
                 voice_name=None,
                 pitch=None,
                 volume_gain_db=None,
                 speaking_rate=None):
        self.language_code = language_code or 'en-US'
        self.voice_name = voice_name or 'en-US-Wavenet-D'
        self.pitch = pitch or 0
        self.volume_gain_db = volume_gain_db or 0
        self.speaking_rate = speaking_rate or 1.0


class TTSService:
    def __init__(self, options: TTSServiceOptions = None):
        self.options = options or TTSServiceOptions()
        self.client = texttospeech.TextToSpeechClient()
        self.synthesis_input = None

    def set_text(self, text):
        self.synthesis_input = texttospeech.types.SynthesisInput(text=text)

    def update_options(self, options: TTSServiceOptions):
        self.voice = texttospeech.types.VoiceSelectionParams(
            language_code=options.language_code,
            name=options.voice_name)

        self.audio_config = texttospeech.types.AudioConfig(
            pitch=options.pitch,
            volume_gain_db=options.volume_gain_db,
            speaking_rate=options.speaking_rate,
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    def save_as_file(self, path):
        response = self.client.synthesize_speech(self.synthesis_input, self.voice, self.audio_config)
        with open(path, 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file {}'.format(path))


class PlayableTTSService(TTSService):
    def __init__(self):
        super(PlayableTTSService, self).__init__()
        self.p = audioplayer.Mp3Player()

    def speak(self, text):
        temp_file_path = 'temp_media.mp3'

        self.set_text(text)
        self.save_as_file(temp_file_path)
        self.p.set_path(temp_file_path)
        self.p.play()
