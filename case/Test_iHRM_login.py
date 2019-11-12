"""

   封装 unittest 相关实现
"""
import json

import app
from api.loginAPI import Login

"""1 导包"""
import unittest
import requests

"""2 创建测试类"""
# 参数化 步骤1: 导包-------------------------------------
from parameterized import parameterized


#      步骤2：解析--------------------------------------
def read_json_file():
    # 1 创建空列表接受数据
    data = []
    # 2 解析文件流 ，将数据追加进列表
    with open(app.PRO_PATH + "/data/login_data.json", "r", encoding="utf-8") as f:
        for v in json.load(f).values():
            mobile = v.get("mobile")
            password = v.get("password")
            success = v.get("success")
            code = v.get("code")
            message = v.get("message")
            # 组织成元祖
            ele = (mobile, password, success, code, message)
            # 追加进列表
            data.append(ele)
    # 3返回列表
    return data


class Test_Login(unittest.TestCase):
    """3 初始化函数"""

    def setUp(self) -> None:
        """初始化 session"""
        self.session = requests.Session()
        # 初始化api对象
        self.login_obj = Login()

    # """4 资源卸载函数"""

    def tearDown(self) -> None:
        self.session.close()

    # """5 测试函数 - 登陆"""

    # 5-1参数化
    @parameterized.expand(read_json_file())
    def test_login(self, mobile, password, success, code, message):
        print("-" * 50)
        print("参数化读取的数据", mobile, password, success, code, message)
        # 5-2请求业务
        response = self.login_obj.login(self.session, mobile, password)
        print("登录响应结果:", response.json())
        # 5-3断言业务
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))

    def test_login_success(self):
        # 1 直接通过提交正向数据发送请求业务
        response = self.login_obj.login(self.session, "13800000002", "123456")
        # 2断言业务
        print("登录成功结果：", response.json())
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
        token = response.json().get("data")
        print("登录后相应的token:",token)
        app.TOKEN = token
