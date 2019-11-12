"""
   测试套件：
        按照需求组合被执行的测试函数
"""
# 1 导包
import unittest

# 2 实例化套件对象，组织被测试的测试函数
import app
from case.Test_iHRM_Emp import Test_Emp
from case.Test_iHRM_login import Test_Login
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(Test_Login("test_login_success"))  # 组织登录成功的测试函数
suite.addTest(Test_Emp("test_add"))  # 组织员工新增的测试函数
suite.addTest(Test_Emp("test_update"))  # 组织员工修改的测试函数
suite.addTest(Test_Emp("test_get"))  # 组织员工查询的测试函数
suite.addTest(Test_Emp("test_delete"))  # 删除
# # 3 执行套件，生成测试报告
# runner = unittest.TextTestRunner()
# runner.run(suite)
# 添加的ID1193818098175922176
with open(app.PRO_PATH + "/report/report.html","wb") as f:
    # 创建 HTMLTestRunner 对象
    runner = HTMLTestRunner(f, title="人力资源管理系统测试报告", description="测试员工模块的增删改查相关接口")
    # 执行
    runner.run(suite)
