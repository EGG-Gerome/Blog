from flask import Flask

app = Flask(__name__)
# 路由URL
@app.route('/')
def home():
    return "这是主页！"

@app.route('/login')
def login():
    return "登录网页！"

@app.route('/logout')
def logout():
    return "登出网页！"

@app.route('/user/<username>',methods=['GET'])
def user_profile(username):
    return f"Hello, {username}! 这是个人信息页面"

if __name__ == '__main__':
    app.run(debug=True)

