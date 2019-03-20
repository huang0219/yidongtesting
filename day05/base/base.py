from selenium.webdriver.support.wait import WebDriverWait
def __init__(self, driver):
    self.driver = driver

class Base:
    # 获取driver
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def base_find_element(self,loc):
        return WebDriverWait(self.driver,timeout=10,poll_frequency=0.5).until(lambda x:x.find_element(*loc))

    # 拖拽方法
    def base_drag_and_drop(self,el1,el2):
        self.base_drag_and_drop(el1,el2)
    # 点击
    def base_click(self,loc):
        self.base_find_element(loc).click()
    # 获取文本方法封装
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    def base_input(self,loc,value):
        el=self.base_find_element(loc)
        el.clear()
        el.send_keys(value)