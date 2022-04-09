from flask import Flask, render_template
import os
import re
app = Flask(__name__)


@app.route('/')
def music():
    path = os.path.dirname(os.path.abspath(__file__))
    path = path + '/static/music/'
    all_files = os.listdir(path)
    music_list = []
    for i in all_files:
        x = re.findall(r'(.*?).mp3', i)
        music_list.append(x[0])
    return render_template('index.html', music_list=music_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
