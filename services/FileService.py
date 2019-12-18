# -*- coding: UTF8 -*-

import time
import datetime
import os


class FileService(object):

    def __init__(self):
        pass

    '''把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''
    def TimeStampToTime(self, timestamp):
        timeStruct = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)

    '''获取文件的大小,结果保留两位小数，单位为MB'''
    def get_FileSize(self, filePath):
        fsize = os.path.getsize(filePath)
        fsize = fsize/float(1024*1024)
        return round(fsize, 2)

    '''获取文件的访问时间'''
    def get_FileAccessTime(self, filePath):
        t = os.path.getatime(filePath)
        return self.TimeStampToTime(t)

    '''获取文件的创建时间'''
    def get_FileCreateTime(self, filePath):
        t = os.path.getctime(filePath)
        return self.TimeStampToTime(t)

    '''获取文件的修改时间'''
    def get_FileModifyTime(self, filePath):
        t = os.path.getmtime(filePath)
        return self.TimeStampToTime(t)
