#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@version:
author:sunjoy
@time: 2017/10/09
@file: mysql_test.py
"""
import pymysql.cursors
#Connect to the database
contection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    db = 'test',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

try:
    with contection.cursor() as cursor:
        #Create a new record
        sql = 'INSERT INTO guest (realname, phone, email, sign, event_id, create_time) VALUES ("alen", 18800110001, "alen@mail.com", 0, 1, NOW());'
        cursor.execute(sql)

    #connection is not autocommit by default.So you must commit to save your change.
    contection.commit()

    with contection.cursor() as cursor:
        # Read a single record
        sql = "SELECT realname,phone, email, sign FROM sign_guest WHERE phone=%s"
        cursor.execute(sql, ('18800110001',))
        result = cursor.fetchone()
        print(result)

finally:
    contection.close()