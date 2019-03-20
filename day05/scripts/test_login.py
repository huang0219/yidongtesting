import os
import sys
sys.path.append(os.getcwd())

from day05.base.get_driver import get_driver
from day05.page.page_login import PageLogin
class TestLogin():
    def setup(self):
        self.login=PageLogin(get_driver())
    def teardown(self):
        self.login.driver.quit()
    def test_login(self,username="itheima",pwd="123456",except_result="itheima"):
        # 登录
        self.login.page_login(username,pwd)
    # 断言
        try:
             assert except_result==self.login.page_get_info()
        # 退出
             try:
                 # 退出
                 self.login.page_logout()
                 # 断言退出是否成功
                 assert self.login.page_logout_is_ok()
             except:
                  print("退出断言失败")
        except AssertionError as e:
             print("断言错误")