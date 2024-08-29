#!/usr/bin/env python3
"""
SocketIO サンプルコード

# 参考
https://qiita.com/Yu_unI1/items/53570f021363d9f57d4c

# 準備
pip install --upgrade pip
pip install Flask
pip install Flask-SocketIO
"""

from flask import Flask, render_template
from flask_socketio import SocketIO
import time

# インスタンスを作成
app = Flask(__name__)
socketio = SocketIO(app)


# メインページを render する
@app.route('/')
def index():
    return render_template('index.html')


# SocketIO を実行
# JS から
#   socket.emit("send_message", {message: userMessage});
# が実行されると {message: userMessage} の dict で送られてくる。
# この userMessage が handle_message(data) の data にはいる
@socketio.on('send_message')
def handle_message(data):
    print(f"received {data}")  # 送られてきた dict を表示

    response_message = f"You typed {str(data['message'])}!"

    # クラアントに対してイベントを送る
    for dev in data['message']:
        time.sleep(3)
        socketio.emit('receive_message', {dev: '取得しました！'})

    # 終了したら {'status': 'completed'} を送る
    # JS 側でダウンロードリンクを表示
    socketio.emit('receive_message', {'status': 'completed'})


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port="8888")



