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
    """ The option type for TTSService

    Google Cloud Text-to-speech service can generate different audio according to
    the customized option. Compared with the existing option management, This type
    provides a better experience when user try to change the configuration of
    TTSService, without any knowledge of the Google Cloud API type.

    """

    def __init__(self,
                 language_code=None,
                 voice_name=None,
                 pitch=None,
                 volume_gain_db=None,
                 speaking_rate=None):
        """Initialized the options

        :param language_code: Optional. A BCP-47 language tag.
            Default is 'en-US'.
        :param voice_name: Optional. The name of this voice. Each distinct voice has a unique name.
            Default is 'en-US-Wavenet-D'.
        :param pitch: Optional. Speaking pitch, in the range [-20.0, 20.0].
            Default is '0'.
        :param volume_gain_db: Optional. Volume gain (in dB) of the normal native volume supported by
                         the specific voice, in the range [-96.0, 16.0].
            Default is 0.
        :param speaking_rate: Optional. The synthesis sample rate (in hertz) for this audio.
            Default is 1.0.
        """
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
        self.voice = texttospeech.types.VoiceSelectionParams(
            language_code=self.options.language_code,
            name=self.options.voice_name)
        self.audio_config = texttospeech.types.AudioConfig(
            pitch=self.options.pitch,
            volume_gain_db=self.options.volume_gain_db,
            speaking_rate=self.options.speaking_rate,
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

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
            # Write the response to the output file.p
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
