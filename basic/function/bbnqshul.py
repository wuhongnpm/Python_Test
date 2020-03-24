# 0 1 1 2 3 5 8 13 21
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return "done"


g = fib(5)
while True:
    try:
        x = next(g)
        print("......: ", x)
    except StopIteration as e:
        print("生成器已迭代完毕...", e.value)
        print("生成器已迭代完毕...", e.args)
        bre