from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_id('search_query_top').send_keys('Hola Mundo')
driver.find_element_by_name('submit_search').click()
time.sleep(2)
tc.assertEqual('No results were found for your search "Hola Mundo"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text)
driver.find_element_by_link_text('Women').click()
time.sleep(2)
driver.find_element_by_partial_link_text('res').click()
time.sleep(2)
#Link Text
driver.find_element_by_link_text('Casual Dresses').click()
#partial Link Text
driver.find_element_by_partial_link_text('Casual').click()
#por classname
driver.find_elements_by_class_name('subcategory-name').click()
#por cssselector
driver.find_elements_by_css_selector('a.subcategory-name').click()
#por xpath
driver.find_element_by_xpath('//*[@id="subcategories"]/ul/li[1]/h5/a').click()
#por tag
driver.find_elements_by_tag_name('a').click()
driver.close()
driver.quit()