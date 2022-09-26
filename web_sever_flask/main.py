from contextlib import redirect_stderr
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #127.0.0.1 or localhost 주소에 '/'가 끝나면 hello를 반환하는 함수
def hello():
    return 'hello'

@app.route('/coder')
def autocoder():
    return 'I am AutoCoder'

def main():
    app.run(host = "127.0.0.1", debug=False, port=443)

if __name__ == "__main__":
    main()

 