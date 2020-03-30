from http.server import  BaseHTTPRequestHandler,HTTPServer

'''
模块的 BaseHTTPRequestHandler 类会帮我们处理对请求的解析，并通过确定请求的方法来调用其对应的函数，比如方法是 GET ,该类就会调用名为 do_GET 的方法。
RequestHandler 继承了 BaseHTTPRequestHandler 并重写了 do_GET 方法，其效果如代码所示是返回 Page 的内容。 
Content-Type 告诉了客户端要以处理 .html 文件的方式处理返回的内容。end_headers 方法会插入一个空白行，如之前的 request 结构图所示。
'''
class RequestHandler(BaseHTTPRequestHandler):
    #处理请求且返回页面
    Page = '''\
            <html>
            <body>
            <table>
            <tr>  <td>Header</td>         <td>Value</td>          </tr>
            <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
            <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
            <tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
            <tr>  <td>Command</td>        <td>{command}</td>      </tr>
            <tr>  <td>Path</td>           <td>{path}</td>         </tr>
            </table>
            </body>
            </html>
    '''
    #处理一个get请求
    def do_Get(self):

    def create_page(self):
        values = {
        'date_time'   : self.date_time_string(),
        'client_host' : self.client_address[0],
        'client_port' : self.client_address[1],
        'command'     : self.command,
        'path'        : self.path
        }
        page = self.Page.format(**values)
        return page

    def send_content(self,page):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page.encode('utf-8'))

if __name__ == '__main__':
    serverAddress = ('',8080)
    server = HTTPServer(serverAddress,RequestHandler)
    server.serve_forever()

