from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    is_android = 'Android' in user_agent
    is_ios = 'iPhone' in user_agent or 'iPad' in user_agent
    is_mobile = is_android or is_ios
    return render_template("index.html",
                           is_mobile=is_mobile, is_android=is_android, is_ios=is_ios)

if __name__ == '__main__':
    app.run(debug=True)
