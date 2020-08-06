from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
ulr = r'http://www.baidu.com'
driver.get( ulr )

# 点击百度首页的搜索设置，打开目标页面
print("点击百度首页的搜索设置，打开目标页面")
driver.find_element_by_id('s-usersetting-top').click()
driver.find_element_by_link_text('搜索设置').click()
time.sleep(2)

# 开始使用示例方法定位
# 首先定位到下拉框控件,并展开下拉框，使得下拉框选项可见
select =  driver.find_element_by_css_selector('select#nr')
select.click()


# 通过value值定位下拉框选项
Select(select).select_by_value('50')
time.sleep(2)

# 通过text值定位下拉框选项
Select(select).select_by_visible_text('每页显示20条')
time.sleep(2)

# 通过索引定位下拉框选项
Select(select).select_by_index(0)
time.sleep(2)

# ======================================================
# 运行结果：
# 下拉框默认选项是每页显示10条，通过代码，下拉框会依次显示选择每页显示50条，
# 每页显示20条，每页显示10条，
# ======================================================

