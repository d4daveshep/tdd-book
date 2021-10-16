from selenium import webdriver

browser = webdriver.Firefox()

# Check out the homepage
browser.get('http://localhost:8000')

# Homepage title  and header mention to-do lists

assert 'To-do' in browser.title

browser.quit()


