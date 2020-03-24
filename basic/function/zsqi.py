def authority(function_to_decorate):
    def auth():
        username = input("请输入用户名：")
        password = input("请输入用户密码：")
        if username == 'crisimple' and password == '123456':
            print("......认证成功......")
            function_to_decorate()
        else:
            print("......认证失败......")
    return auth200


@authority
def view_space():
    print("......欢迎进入哔哩哔哩个人空间......")


if __name__ == "__main__":
    view_space()
    print("view_space.__name__ is: ", view_space.__name__)
