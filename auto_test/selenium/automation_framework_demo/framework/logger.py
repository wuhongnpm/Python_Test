
# -*- coding:utf-8 -*-

# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2019-12-19
@author: 北京-宏哥   QQ交流群：705269076
Project: 《《一头扎进》系列之Python+Selenium框架设计篇3- 价值好几K的框架，不看别后悔，过时不候
'''

# 3.导入模块
import logging
import logging.handlers
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        '''''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个日志器logger，并设置其日志级别为DEBUG
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 项目根目录下/Logs 保存日志
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录
        log_name = log_path + rq + '.log'
        # 创建一个文件处理器handler并设置其日志级别为INFO
        #fh = logging.FileHandler(log_name, maxBytes=1024 * 1024, backupCount=5,
         #                                               encoding='utf-8')

        fh = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024 * 1024, backupCount=5,
                                                         encoding='utf-8')  # 实例化handler

        #fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        '''
        创建一个流处理器handler并设置其日志级别为INFO
        '''
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        #handler = logging.handlers.RotatingFileHandler(fh, maxBytes=1024 * 1024, backupCount=5,
        #                                                 encoding='utf-8')  # 实例化handler
        '''
        创建一个格式器formatter并将
        '''
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给日志处理器logger添加上面创建的handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger