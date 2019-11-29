import vlc


class Mp3Player:
    def __init__(self):
        self.p = vlc.MediaPlayer()

    def set_path(self, path):
        self.p.set_mrl(path)

    def play(self):
        if self.p.is_playing():
            self.stop()

        self.p.play()

    def stop(self):
        self.p.stop()
