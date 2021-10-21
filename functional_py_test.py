from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import pytest

# This fixture creates a browser object to be used later in tests
# it also cleans up the browser once it's finished being used - cool eh!
@pytest.fixture
def browser():
	browser = webdriver.Firefox()
	yield browser
	browser.quit()
	
	
# Uses the browser fixture
def test_can_start_a_list_and_retrive_it_later(browser):
	# Check out the homepage
	browser.get('http://localhost:8000')
        
	# Homepage title  and header mention to-do lists
	assert browser.title.find('To-Do') >= 0
	header_text = browser.find_element_by_tag_name('h1').text
	assert header_text.find('To-Do') >= 0

	# Enter a to-do list item straight away
	inputbox = browser.find_element_by_id('id_new_item')
	assert inputbox.get_attribute('placeholder') == 'Enter a to-do item'

	# Enter something into the text box
	inputbox.send_keys('Buy peacock feathers')
		
	# Hit enter, page updates and now lists item just entered
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
		
	table = browser.find_element_by_id('id_list_table')
	rows = table.find_elements_by_tag_name('tr')
	assert any(row.text == '1: Buy peacock feathers' for row in rows), "New to-do item did not appear in table"

	#pytest.fail('Finish the test!')
	


