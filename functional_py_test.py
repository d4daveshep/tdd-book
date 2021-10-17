from selenium import webdriver
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
	assert 'To-do' == browser.title
	


