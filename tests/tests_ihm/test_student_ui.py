from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialisation du navigateur
driver = webdriver.Chrome()
driver.get("http://localhost:5000/students")  # URL de la page de gestion des étudiants

# Test 1 : Ajout d'un étudiant
def test_add_student():
    driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#addStudentModal']").click()
    time.sleep(1)
    driver.find_element(By.ID, "name").send_keys("Mor Ndiaye")
    driver.find_element(By.ID, "age").send_keys("20")
    driver.find_element(By.ID, "grade").send_keys("Licence")
    driver.find_element(By.ID, "submitAddStudent").click()
    time.sleep(2)
    assert "Mor Ndiaye" in driver.page_source


# Test 3 : Suppression d'un étudiant
def test_delete_student():
    delete_button = driver.find_element(By.XPATH, "//td[text()='Mor Ndiaye']/following-sibling::td/button[contains(text(), 'Supprimer')]")
    delete_button.click()
    time.sleep(1)
    driver.switch_to.alert.accept()  # Confirmer la suppression
    time.sleep(2)
    assert "Mor Ndiaye" not in driver.page_source

# Exécution des tests
test_add_student()

test_delete_student()

# Fermeture du navigateur
driver.quit()