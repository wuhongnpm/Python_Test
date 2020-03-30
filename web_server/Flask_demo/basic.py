#导入了类 Flask。这个类的实例化将会是我们的 WSGI 应用。
from flask import Flask
#创建一个该类的实例。第一个参数是应用模块或包的名称，这样 Flask 才会知道去哪里寻找模板、静态文件等等。
# 如果你使用的是单一的模块（就如本例），第一个参数应该使用 __name__。
app = Flask(__name__)
#使用装饰器route()告诉 Flask 哪个URL才能触发我们的函数。
@app.route('/')
#定义一个函数，该函数名也是用来给特定函数生成 URLs，并且返回我们想要显示在用户浏览器上的信息。
def hello_word():
    return 'Hello World!'