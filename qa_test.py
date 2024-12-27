import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Fixture to set up and tear down the WebDriver
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()  
    driver.maximize_window()
    yield driver
    driver.quit()

def test_open_page(browser):
    url = 'https://www.lambdatest.com/selenium-playground/table-sort-search-demo'
    browser.get(url)
    assert browser.current_url.startswith('https://www.lambdatest.com'), "Failed to open the page"
    time.sleep(2)

def test_validate_url(browser):
    # Expected URL
    expected_url = 'https://www.lambdatest.com/selenium-playground/table-sort-search-demo'
    actual_url = browser.current_url
    assert expected_url in actual_url, f"Expected URL to contain {expected_url}, but got {actual_url}"
    time.sleep(2)

def test_validate_title(browser):
    # Check the name of the header
    header = browser.find_element(By.TAG_NAME, 'h1').text
    expected_header = "Table Sorting And Searching"
    assert header == expected_header, f"Expected header to be '{expected_header}', but got '{header}'"
    time.sleep(2)

def test_search_new_york(browser):
    # Locate the search box and perform a search for "New York"
    search_box = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[aria-controls="example"]')) ) 
    search_box = WebDriverWait(browser, 10).until( EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-controls="example"]')) )
    browser.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top + window.scrollY - 200);", search_box)
    time.sleep(2)
    search_box.clear()
    search_box.send_keys("New York")
    time.sleep(2)

def test_validate_results(browser):
    # Validate that the search results show 5 entries out of 24 total entries
    # rows = browser.find_elements(By.ID, "example")
    # visible_rows = [row for row in rows if row.is_displayed()]
    # assert len(visible_rows) == 5, f"Expected 5 results, but got {len(visible_rows)}"
    demo =  browser.find_element(By.ID, 'example_info').text
    expected_demo = 'Showing 1 to 5 of 5 entries (filtered from 24 total entries)'
    assert demo == expected_demo, f"Expected demo to be '{expected_demo}', but got '{demo}'"
    time.sleep(3)

if __name__ == "__main__":
    pytest.main(['-v', '--html=report.html'])
