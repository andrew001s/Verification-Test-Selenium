from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_login(browser):
    browser.get('https://localhost:7223/')
    elements = browser.find_elements(By.ID, "correo") and browser.find_elements(By.ID, "contrasena") and browser.find_elements(By.ID, "btningreso")
    assert elements, "No se encontraron todos los elementos de un Login"
    browser.find_element(By.ID, "correo").send_keys("")
    browser.find_element(By.ID, "contrasena").send_keys("")
    browser.find_element(By.ID, "btningreso").click()
    assert browser.find_element(By.CLASS_NAME, "error-alert"), "No se controla el ingreso de usuarios"
    assert browser.find_element(By.CLASS_NAME, "register-link"), "No se encontro el link de registro"

def test_admin(browser):
    browser.get('https://localhost:7223/')
    browser.find_element(By.ID, "correo").send_keys("admin")
    browser.find_element(By.ID, "contrasena").send_keys("admin1015")
    browser.find_element(By.ID, "btningreso").click()
    assert 'Tables - SB Admin' in browser.title, "No se encontro la pagina de administrador"
    assert  browser.find_elements(By.ID, "myPieChart") or browser.find_elements(By.ID, "myBarChart") , "No se encontro el graficos"



if __name__ == "__main__":
    pytest.main([__file__,"--html=reporte_pruebas.html"])
