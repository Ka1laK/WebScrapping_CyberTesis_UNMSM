# 📚 Cybertesis UNMSM Web Scraper 🕸️

Bienvenido a **Cybertesis UNMSM Web Scraper**! Este proyecto es un **script en Python** que utiliza `Selenium` para navegar 
por el sitio de [Cybertesis de la UNMSM](https://cybertesis.unmsm.edu.pe/) y recopilar datos de tesis de la Escuela Profesional de Ingeniería de Sistemas e Informática. 
La información extraída incluye los títulos de las tesis, los autores y el año de publicación 📅.

![image](https://github.com/user-attachments/assets/27f8d54c-63af-4a91-b3f2-6c635cdf0401)


---

## 🎯 Objetivo

Automatizar la recolección de datos académicos y almacenarlos en un archivo CSV para análisis o investigación futura. 
Este script puede ser útil para estudiantes, investigadores y docentes que deseen explorar el repositorio de tesis de la UNMSM en busca de 
tendencias o referencias bibliográficas.

---

## 🚀 Instalación y Ejecución

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/cybertesis-unmsm-web-scraper.git
cd cybertesis-unmsm-web-scraper
```
### 2. Instala las dependencias

Asegúrate de tener instalado pip y luego instala las dependencias ejecutando:

```bash
pip install -r requirements.txt
```
### 3. Ejecuta el Script🖥️
Para iniciar la extracción de datos:
```bash
python scripts/scraper.py
```


## 📋 Funcionalidades
-  Navegación automatizada: El script navega desde la página principal de Cybertesis, siguiendo enlaces hasta la sección de la Escuela Profesional de Ingeniería de Sistemas e Informática.
-  Extracción de datos: Obtiene el título de la tesis, el año y el autor o autores.
-  Almacenamiento en CSV: Todos los datos se guardan en un archivo llamado publicaciones_cybertesis_UNMSM.csv.

## 🔨 Tecnologías Utilizadas
-  Python 🐍
-  Selenium para la navegación automatizada 🌐
-  Pandas para el almacenamiento de datos en formato CSV 📄

## 📝 Estructura del Proyecto
```bash
cybertesis-unmsm-web-scraper/
├── README.md
├── scraper.py              # Script principal de extracción
├── requirements.txt        # Dependencias del proyecto
└── publicaciones_cybertesis_UNMSM.csv # Archivo de salida con los datos recolectados
```

## 🌟 Cómo Funciona
El script sigue estos pasos:

-  Acceso a la página principal de Cybertesis de la UNMSM.
-  Navegación automática a través de varias secciones, hasta llegar a "Tesis EP Ingeniería de Sistemas".
-  Extracción de datos de cada página de tesis, incluyendo título, año y autor(es).
-  Almacenamiento de los datos en un archivo publicaciones_cybertesis_UNMSM.csv para su análisis.

## ¡Gracias por visitar este proyecto! 🚀
