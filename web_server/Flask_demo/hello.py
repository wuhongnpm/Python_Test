from flask import Flask
from flask import abort,redirect,url_for
app = Flask(__name__)

#如果访问/,返回Index Page
@app.route('/')
def index():
    return 'Index Page'

#如果访问/hello,返回hello world
@app.route('/hello')
def hello():
    return 'Hello World!'

#添加变量
@app.route('/user/<username>')
def show_user_profile(username):
    # 显示用户名
    return 'User {}'.format(username)
# with app.test_request_context():
#      print(url_for('hello'))

#请求对象
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # 当请求形式为“GET”或者认证失败则执行以下代码
    return render_template('login.html', error=error)

#重定向
@app.route('/jingtai')
def jingtai():
    return redirect(url_for('basic'))

#abort()提前中断一个请求且返回一个错误代码
@app.route('/basic')
def basic():
    abort(401)
    this_is_never_executed()