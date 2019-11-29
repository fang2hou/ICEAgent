import audioplayer
import gcloud
from time import sleep

if __name__ == '__main__':

    tts = gcloud.TTSService()

    tts.set_text("Lots of learning tasks require dealing with graph data which contains rich relation information among elements. Modeling physics system, learning molecular fingerprints, predicting protein interface, and classifying diseases require a model to learn from graph inputs.")
    tts.save_as_file("speech.mp3")

    p = audioplayer.Mp3Player()
    p.set_path("speech.mp3")
    p.play()

    sleep(12)
    p.stop()