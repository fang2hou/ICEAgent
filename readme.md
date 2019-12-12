ICEAgent
=============
![](https://img.shields.io/badge/Ritsumeikan-ICE%20Lab-blue.svg?longCache=true&colorA=990000&colorB=444444&longCache=true&style=for-the-badge) ![](https://img.shields.io/badge/Python-3.7.5-blue.svg?longCache=true&style=for-the-badge) ![](https://img.shields.io/badge/Flask-1.1.1-orange.svg?longCache=true&style=for-the-badge) 

A local service for research.  
ICEAgent allow you to add custom functionality via modules.  
The main propose of this project is helping you use Google Cloud TTS more regularly.

Get Started
-----
1. Prepare a virtual Python `3.7` environment. (`3.8` is not support yet)  
_`conda` is recommended, `venv` is also a good choice._
2. Enter into the root directory of `ICEAgent`, run `pip install -r requirements.txt` in Terminal/Command Prompt.  
3. Add `GOOGLE_APPLICATION_CREDENTIALS` to your PATH.  
    - __You can get your credential file from [Google](https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries)__  
    - <ins>Windows</ins>: Search "edit environment variables" in your Start Menu, and find PATH to add the path of your json file.  
    - <ins>macOS/Linux</ins>: run `env GOOGLE_APPLICATION_CREDENTIALS=path/to/your/json/file` in Terminal.
    - <ins>IDE(PyCharm etc.)</ins>: Add environment variables to your project.
5. Install VLC media player.  
    - <ins>macOS with Homebrew</ins>: run `brew cask install vlc` in Terminal  
    - <ins>Others</ins>: Download from [VLC homepage](https://www.videolan.org/vlc/index.html).

4. Install Postman. (Optional, Just for testing)  
    - <ins>macOS with Homebrew</ins>: run `brew cask install postman` in Terminal.  
    - <ins>Others</ins>: Download from [Postman homepage](https://www.getpostman.com/).
5. run `ICEAgent` with `python main.py`.

FAQ
-----
1. It warns me that the program cannot find LibVLC.  
__A:__ Add vlc folder to your PATH. Same as you add GOOGLE_APPLICATION_CREDENTIALS.

2. I want to add my own modules.  
__A:__ `ICEAgent` use Flask Blueprint to handle modules. After you building a module with blueprint, you can easily add a route to your module in `main.py`

Author
-----
Zhou Fang @ [Intelligent Computer Entertainment Laboratory of Ritsumeikan Unviersity](http://www.ice.ci.ritsumei.ac.jp/researches.html)

License
-----
```
ICEAgent, including all git submodules are free software:
you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
```
