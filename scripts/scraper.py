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

# URL de la pagina principal
url = 'https://cybertesis.unmsm.edu.pe/'
driver.get(url)
time.sleep(5)

# Ir a "Ingenieria"
ingenieria_link = driver.find_element(By.XPATH, "//a[contains(@href, '/community/d2dd9c8c-0bfd-4502-aeb1-52184b55f950') and contains(., 'Ingeniería')]")
ingenieria_link.click()
time.sleep(5)

# Ir a "Facultad de Ingenieria de Sistemas e Informatica"
facultad_link = driver.find_element(By.XPATH, "//a[contains(@href, '/community/c7f57711-06e9-4821-8ccb-639c2874b28b') and contains(., 'Facultad de Ingeniería de Sistemas e Informática')]")
facultad_link.click()
time.sleep(5)

# Ir a "EP Ingenieria de Sistemas"
ep_sistemas_link = driver.find_element(By.XPATH, "//a[contains(@href, '/community/c2bac64b-44f7-4357-b0d3-696a076a6dcb') and contains(., 'EP Ingeniería de Sistemas')]")
ep_sistemas_link.click()
time.sleep(5)

# Ir a "Tesis EP Ingenieria de Sistemas"
tesis_sistemas_link = driver.find_element(By.XPATH, "//a[contains(@href, '/collection/8c7c6dc5-2beb-4b23-a722-50012376769e') and contains(., 'Tesis EP Ingeniería de Sistemas')]")
tesis_sistemas_link.click()
time.sleep(5)

# Ir a "Titulos"
titulos_button = driver.find_element(By.XPATH, "//h6[contains(text(), 'Títulos')]")
titulos_button.click()
time.sleep(10)

titulos = []
anios = []
autores = []

while True:
    # Extraer los titulos
    encontrar_titulos = driver.find_elements(By.XPATH, "//a[contains(@class, 'MuiTypography-h5')]")
    titulos.extend([titulo.text for titulo in encontrar_titulos])

    # Extraer los anios
    encontrar_anios = driver.find_elements(By.XPATH, "//div[contains(@class, 'css-gg4vpm')]")
    anios.extend([anio.text.split()[-1] for anio in encontrar_anios])

    # Extraer los autores
    encontrar_autores = driver.find_elements(By.XPATH, "//div[contains(@class, 'MuiStack-root css-kvb41a')]")
    for autor in encontrar_autores:
        # Obtener todos los elementos <span> dentro del contenedor de autores y concatenarlos
        autores_texto = " | ".join([span.text for span in autor.find_elements(By.TAG_NAME, "span")])
        autores.append(autores_texto)

    # Verificador de longitud de listas
    if not (len(titulos) == len(anios) == len(autores)):
        print("Error: Las cantidades de titulos, anios y autores no coinciden. Revisar los selectores.")
        break

    # Ir a la siguiente pagina
    try:
        pagina_sig = driver.find_element(By.XPATH, "//button[@aria-label='Go to next page']")
        pagina_sig.click()
        time.sleep(5)  
    except:
        print("No hay mas paginas...")
        break

data = pd.DataFrame({'Titulo': titulos, 'Anio': anios, 'Autor(es)': autores})
data.to_csv('data_output/publicaciones_cybertesis_UNMSM.csv', index=False)
driver.quit()
