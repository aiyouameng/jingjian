import tornado.web
from dao import userdao
from util import utils, deco
import json


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html', msg="")

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        rs = userdao.getUserByUserPass(username=username, password=password)
        if rs != None:
            self.set_secure_cookie("username", username)
            data = json.dumps({"username": username, "pasword": password, "id": rs.id})
            utils.setMem(username, data)
            self.redirect('/index')
        else:
            self.render('login.html', msg="登录失败")


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('register.html', msg='')

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        rs = userdao.getUserByUsername(username=username)
        if rs[0] > 0:
            self.render('register.html', msg="此用户已存在")
        else:
            userdao.insertUser(username=username, password=password)
            self.redirect('/')


class IndexHandler(tornado.web.RequestHandler):
    @deco.auth_login_redirect
    def get(self, *args, **kwargs):
        data = kwargs["data"]
        print(data["username"])
        self.render('index.html', username=data["username"])


class ModifyPassWordHandler(tornado.web.RequestHandler):
    @deco.auth_login_redirect
    def get(self, *args, **kwargs):
        self.render('password.html')

    @deco.auth_login_redirect
    def put(self, *args, **kwargs):
        data = kwargs["data"]
        password = self.get_argument("newpass")
        self.write({"retCode":1})
