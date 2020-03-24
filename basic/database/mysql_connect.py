import pymysql
from sshtunnel import SSHTunnelForwarder

def write_log(message, file_name="item_count.txt"):
    mylog = open(file_name, mode='a', encoding='utf-8')
    print(message, file=mylog)
    mylog.close()


class ConnectMysql:
    def __init__(self):
        self.db_host = "47.95.140.227"
        self.db_port = 22
        self.db_user = "root"
        self.db_password = "123456"

        self.get_connect()

    # 建立连接
    def get_connect(self):
        self.server = SSHTunnelForwarder(
                (self.db_host, self.db_port),
                ssh_username="root",
                ssh_password="Dy19970727",
                remote_bind_address=('127.0.0.1', 3306)
        )
        self.server.start()

        self.connect = pymysql.connect(
            host="127.0.0.1",
            port=self.server.local_bind_port,
            user=self.db_user,
            password=self.db_password,
            db='soapeye',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def close_connect(self):
        try:
            if self.connect:
                self.connect.close()
        except Exception as e:
            print("Error %s" % e)

