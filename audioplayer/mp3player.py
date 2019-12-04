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

import vlc


class Mp3Player:
    """

    A player which is able to decode and play mp3 file. This player use LibVLC as
    backend, it will use another process to play files.

    """
    def __init__(self):
        """Initialize the MP3 player"""
        self.p = vlc.MediaPlayer()

    def set_path(self, path):
        """Set MRL of the file.
        :arg path: The path of the mp3 file
        """
        self.p.set_mrl(path)

    def play(self):
        """Play the MP3 file."""
        if self.p.is_playing():
            self.stop()

        self.p.play()

    def stop(self):
        """Force to stop the playing."""
        self.p.stop()

    def is_playing(self):
        """ Check the player is playing some file or not.

        :return: Boolean value indicated whether player is playing or not.
        """
        return self.p.is_playing()