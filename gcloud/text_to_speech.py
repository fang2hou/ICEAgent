from google.cloud import texttospeech


class TTSService:
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()
        self.synthesis_input = None
        self.voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
        self.audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    def set_text(self, text):
        self.synthesis_input = texttospeech.types.SynthesisInput(text=text)

    def save_as_file(self, path):
        response = self.client.synthesize_speech(self.synthesis_input, self.voice, self.audio_config)
        with open(path, 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file {}'.format(path))