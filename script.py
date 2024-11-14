from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Configuraciones del navegador
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL de la pagina de Ingenieria de Sistemas
url = 'https://cybertesis.unmsm.edu.pe/collection/8c7c6dc5-2beb-4b23-a722-50012376769e'
driver.get(url)
time.sleep(5)

# Hacer clic en el botón "Titulos"
titulos_button = driver.find_element(By.XPATH, "//h6[contains(text(), 'Títulos')]")
titulos_button.click()
time.sleep(10)

titulos = []
anios = []
autores = []


while True:
    # Extraer los titulos
    titulos_elements = driver.find_elements(By.XPATH, "//a[contains(@class, 'MuiTypography-h5')]")
    titulos.extend([titulo.text for titulo in titulos_elements])

    # Extraer los anios
    anios_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'css-gg4vpm')]")
    anios.extend([anio.text.split()[-1] for anio in anios_elements])

    # Extraer los autores (1 o 1+)
    autores_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'MuiStack-root css-kvb41a')]")
    for autor in autores_elements:
        # Obtener todos los elementos <span> dentro del contenedor de autores y concatenarlos
        autores_texto = ", ".join([span.text for span in autor.find_elements(By.TAG_NAME, "span")])
        autores.append(autores_texto)

    # Validacion de tamanio de listas
    if not (len(titulos) == len(anios) == len(autores)):
        print("Error: Las cantidades de títulos, años y autores no coinciden. Revisar los selectores.")
        break

    # Saltar a la siguiente pagina
    try:
        next_button = driver.find_element(By.XPATH, "//button[@aria-label='Go to next page']")
        next_button.click()
        time.sleep(5)
    except:
        print("No hay mas paginas...")
        break


data = pd.DataFrame({'Titulo': titulos, 'Anio': anios, 'Autor(es)': autores})
data.to_csv('publicaciones.csv', index=False)

# Cerrar el navegador
driver.quit()
