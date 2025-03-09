from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialisation du navigateur
driver = webdriver.Chrome()
driver.get("http://localhost:5000/classrooms")  # URL de la page de gestion des salles

# Test 1 : Ajout d'une salle de classe
def test_add_classroom():
    driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#addClassroomModal']").click()
    time.sleep(1)
    driver.find_element(By.ID, "name").send_keys("Salle A1")
    driver.find_element(By.ID, "capacity").send_keys("30")
    driver.find_element(By.ID, "submitAddClassroom").click()
    time.sleep(2)
    assert "Salle A1" in driver.page_source


# Exécution des tests
test_add_classroom()


# Fermeture du navigateur
driver.quit()