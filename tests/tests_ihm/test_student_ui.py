from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Assurez-vous d'avoir ChromeDriver installé
    yield driver
    driver.quit()

def test_add_student(browser):
    browser.get('http://localhost:5000')
    browser.find_element_by_id('studentName').send_keys('John Doe')
    browser.find_element_by_id('studentAge').send_keys('20')
    browser.find_element_by_id('studentGrade').send_keys('A')
    browser.find_element_by_id('addStudentForm').submit()
    assert 'John Doe' in browser.page_source