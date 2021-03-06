from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrive_it_later(self):
		# Check out the homepage
		self.browser.get('http://localhost:8000')
        
		# Homepage title  and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# Enter a to-do list item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
		
		# Enter something into the text box
		inputbox.send_keys('Buy peacock feathers')
		
		# Hit enter, page updates and now lists item just entered
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows),
			"New to-do item did not appear in table")
		
		# Enter a second item in text box
				
		#self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()
#	pass
	
