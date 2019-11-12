"""
测试员工模块的增删改实现
"""
# 1 导包
import logging
import unittest
import requests

import app
from api.EmpAPI import EmpCRUD


# 2 创建测试类


class Test_Emp(unittest.TestCase):
    # 3 初始化函数
    def setUp(self) -> None:
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    # 4资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 5测试函数  1 增
    def test_add(self):
        logging.info("增加员工日志信息")
        # 1 请求业务
        response = self.emp_obj.add(self.session, username="zxdfgdfgdg9", mobile="13497999979")
        print("响应结果:", response.json())
        # 响应结果: {'success': True, 'code': 10000, 'message': '操作成功！', 'data': {'id': '1193820038821662720'}}
        # 提取ID
        id = response.json().get("data").get("id")
        app.USER_ID = id
        print("新增员工的id:", id)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 6测试函数  2 改
    def test_update(self):
        logging.warning("修改员工日志信息")
        response = self.emp_obj.update(self.session, app.USER_ID, "ghjgjghjgjh")
        # 断言业务
        print("修改后的员工信息:", response.json())
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 7测试函数  3 查
    def test_get(self):
        logging.info("查询员工日志信息")
        response = self.emp_obj.get(self.session, app.USER_ID)
        print("查询员工信息:", response.json())
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 8测试函数  4 删
    def test_delete(self):
        logging.info("删除员工日志信息")
        response = self.emp_obj.delete(self.session, app.USER_ID)
        print("删除员工:", response.json())
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
