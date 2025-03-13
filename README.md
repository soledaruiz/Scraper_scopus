# Scraper_scopus
# 📚 Scraper de Scopus con Python

Este proyecto es un scraping permite extraer información de publicaciones científicas desde la API de Scopus. Para este ejercicio vamos a extraer publicaciones de Scopus acerca del impacto de la inteligencia artificial en la economía, esto a través del uso de operadores booleanos.  

## 🚀 Características
- 💪 **Acceso a la API de Scopus**
- 🔍 **Filtrado por palabras clave y año de publicación**
- 💑 **Extracción de título, autores, revista, año, tipo de publicación, resumen y DOI**
- 📊 **Exportación de resultados a un archivo Excel**

## 📦 Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/TU_USUARIO/Scraper_scopus.git
   cd Scraper_scopus
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura tu API Key de Scopus**:
   - Regístrate en Elsevier y obtén una API Key.
   - Coloca tu clave en la variable `API_KEY` dentro del script.

## 🛠 Uso

Ejecuta el script con:
```bash
python scraper_scopus.py
```
Esto generará un archivo `scopus_publications.xlsx` con los resultados.

## 🛠 Tecnologías utilizadas
- Python 3.12
- Requests
- Pandas
- OpenPyXL

## 📅 Licencia
Este proyecto no cuenta con derechos de propiedad intelectual

---
📧 **Contacto**: www.linkedin.com/in/soleda-sandra-ruiz-lopez-a7b3a8124  
🌟 Si te resulta útil, dale una estrella al repo!
