# -*- coding: UTF-8 -*-
import pymysql
import pymysql.cursors
from DBUtils.PooledDB import PooledDB

from Exec.dbutil import DB_config

'''
@功能：PT数据库连接池
'''


class PTConnectionPool(object):
    __pool = None

    def __enter__(self):
        self.conn = self.getConn()
        self.cursor = self.conn.cursor()
        return self

    def getConn(self):
        if self.__pool is None:
            self.__pool = PooledDB(creator=pymysql, mincached=DB_config.DB_MIN_CACHED,
                                   maxcached=DB_config.DB_MAX_CACHED,
                                   maxshared=DB_config.DB_MAX_SHARED, maxconnections=DB_config.DB_MAX_CONNECYIONS,
                                   blocking=DB_config.DB_BLOCKING, maxusage=DB_config.DB_MAX_USAGE,
                                   setsession=DB_config.DB_SET_SESSION,
                                   host=DB_config.DB_TEST_HOST, port=DB_config.DB_TEST_PORT,
                                   user=DB_config.DB_TEST_USER, passwd=DB_config.DB_TEST_PASSWORD,
                                   db=DB_config.DB_TEST_DBNAME, use_unicode=True, charset=DB_config.DB_CHARSET,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )

        return self.__pool.connection()

    """
    @summary: 释放连接池资源
    """

    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()


'''
@功能：获取PT数据库连接
'''


def getPTConnection():
    return PTConnectionPool()
