from util import utils, dbmysql


def insertUser(username, password):
    try:
        sql = "insert into user(username,password,insertTime) VALUES ('%s','%s',now());" % (username, password)
        return dbmysql.query(sql)
    except Exception as e:
        utils.logger.error(e)


def getUserByUsername(username):
    try:
        sql = "select count(1) from user where username='%s';" % username
        return dbmysql.first(sql)
    except Exception as e:
        utils.logger.error(e)
        return None


def getUserByUserPass(username, password):
    try:
        sql = "select * from user where username='%s' and password='%s';" % (username, password)
        return dbmysql.first(sql)
    except Exception as e:
        utils.logger.error(e)
        return None
