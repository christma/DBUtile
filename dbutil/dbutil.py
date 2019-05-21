# Attention is your only currency. Allocate it sparingly.
# Drink copious amounts of water—every day.
# Listen to everyone, then disregard it.
# Never stop learning.
# Take breaks often.
# Keep breathing.
from Exec.dbutil.DB_connetion_pool import getPTConnection


def queryInfo():
    with getPTConnection() as db:
        try:
            sql = "SELECT * FROM roots WHERE sign = 0 LIMIT 1"
            if db.cursor.execute(sql):
                for result in db.cursor.fetchall():
                    sql2 = "UPDATE roots set sign = 1 WHERE id = {0}".format(result[0])
                    db.cursor.execute(sql2)
                    db.conn.commit()
                    return result[1]
            print('没有合适的url')
        except Exception as e:
            print(e)


def handleSql(url, name):
    with getPTConnection() as db:
        try:
            sql2 = "INSERT INTO company(url,name)VALUES({0},{1})".format("".join(url), "".join(name))
            db.cursor.execute(sql2)
            db.conn.commit()

        except Exception as e:
            print(e)
            pass


def getkeywords(parma):
    with getPTConnection() as db:
        try:
            sql1 = 'UPDATE keywords SET {0} = 10 WHERE {1} = 0 LIMIT 1'.format(parma, parma)
            sql2 = "SELECT * FROM keywords WHERE {0} = 10".format(parma)
            db.cursor.execute(sql1)
            db.conn.commit()
            db.cursor.execute(sql2)
            results = db.cursor.fetchall()
            for result in results:
                return result
        except Exception as e:
            print(e)
            pass


def insertsql(x):
    with getPTConnection() as db:
        try:
            sql = 'INSERT INTO tb_content(name,title,url,hosturl,wherefrom)VALUES (%s,%s,%s,%s,%s)'
            db.cursor.execute(sql, (x[0], x[1], x[2], x[3], x[4]))
            db.conn.commit()
        except Exception as e:
            print(x[3], e)
            pass


def updatesql(id, sign):
    with getPTConnection() as db:
        try:
            sql = 'UPDATE keywords SET {0} = 1 WHERE id = {1}'.format(sign, id)
            db.cursor.execute(sql)
            db.conn.commit()
        except Exception as e:
            print(e)
            pass


def selectmore():
    with getPTConnection() as db:
        try:
            # sql1 = 'UPDATE tb_content SET {0} = 10 WHERE {1} = 0 LIMIT 100'.format('wherefrom', 'handle')
            sql2 = "SELECT id, hosturl FROM tb_content WHERE {0} = 10 LIMIT 5000".format('wherefrom')
            # db.cursor.execute(sql1)
            # db.conn.commit()
            db.cursor.execute(sql2)
            results = db.cursor.fetchall()
            if results:
                return results
            else:
                print('没有数据')
        except Exception as e:
            print(e)
            pass


def updatamore(id, url):
    with getPTConnection() as db:
        try:
            sql1 = 'update tb_content set hosturl = "{1}" where id = {0}'.format(id, url)
            db.cursor.execute(sql1)
            db.conn.commit()
        except Exception as e:
            print(e)
            pass
