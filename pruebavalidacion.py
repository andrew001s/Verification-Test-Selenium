from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import requests

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_login(browser):
        browser.get('https://localhost:7223/')
        elements = element_exists(browser,By.ID, "correo") and element_exists(browser,By.ID, "contrasena") and element_exists(browser,By.ID, "btningreso")
        assert elements, "No se encontraron todos los elementos de un Login"
        browser.find_element(By.ID, "correo").send_keys("")
        browser.find_element(By.ID, "contrasena").send_keys("")
        browser.find_element(By.ID, "btningreso").click()
        assert element_exists(browser,By.CLASS_NAME, "error-alert"), "No se controla el ingreso de usuarios"
        assert element_exists(browser,By.CLASS_NAME, "register-link"), "No se encontro el link de registro"


def test_admin(browser):
    browser.get('https://localhost:7223/')
    browser.find_element(By.ID, "correo").send_keys("admin")
    browser.find_element(By.ID, "contrasena").send_keys("admin1015")
    browser.find_element(By.ID, "btningreso").click()
    assert 'Tables - SB Admin' in browser.title, "No se encontro la pagina de administrador"
    assert  element_exists(browser,By.ID, "myPieChart") or browser.find_elements(By.ID, "myBarChart") , "No se encontró graficos"
    browser.get('https://localhost:7223/Administrador/Administrador')
    assert element_exists(browser, By.ID, "botonNuevo"), "No se encontró el botón de agregar"
    assert element_exists(browser, By.CLASS_NAME, "deleteBtn"), "No se encontró el botón de eliminar"
    assert element_exists(browser, By.CLASS_NAME, "editBtn"), "No se encontró el botón de editar"
    response=requests.get('https://localhost:7223/Administrador/Auditoria', verify=False)
    assert response.status_code==200, "No se encontro la pagina de auditoria"



def test_ofertas(browser):
    browser.get('https://localhost:7223/')
    browser.find_element(By.ID, "correo").send_keys("aroman@gmail.com")
    browser.find_element(By.ID, "contrasena").send_keys("123456")
    browser.find_element(By.ID, "btningreso").click()
    assert element_exists(browser, By.ID, "ofertas"), "No se encontró el botón de ofertas"

    

def test_categoria(browser):
    browser.get('https://localhost:7223/')
    browser.find_element(By.ID, "correo").send_keys("aroman@gmail.com")
    browser.find_element(By.ID, "contrasena").send_keys("123456")
    browser.find_element(By.ID, "btningreso").click()
    assert element_exists(browser, By.CLASS_NAME, "catalog-separator-container"), "No se encontró el botón de categorias"
    
def test_carrito(browser):
    response=requests.get('https://localhost:7223/Carrito/Carrito', verify=False)
    assert response.status_code==200, "No se encontro la pagina de carrito"	
    
    
def test_carrito(browser):
    response=requests.get('https://localhost:7223/Home/AcercaDe', verify=False)
    assert response.status_code==200, "No se encontro la pagina de carrito"	
 
def test_product(browser):
    response=requests.get('https://localhost:7223/Producto/Producto', verify=False)
    assert response.status_code==200, "No se encontro la pagina de producto"	
    
def element_exists(browser, by, value, timeout=10):
    try:
        WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    pytest.main([__file__,"--html=reporte_pruebas.html"])
