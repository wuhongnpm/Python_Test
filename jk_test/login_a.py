form common import Common

url = '/'
comm = Common()
response_index = comm.get(url)
print('Response内容'+ response_index.text)
