# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 22:31:17 2025

@author: sruiz
"""

import requests
import pandas as pd
import os  

# Configuramos nuestra clave de API
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXX"
BASE_URL = "https://api.elsevier.com/content/search/scopus"

# Definimos el operador booleano con filtro de año=2025
query = 'TITLE-ABS-KEY("artificial intelligence" AND "impact" AND ("economy" OR "economic growth" OR "macroeconomics" OR "labor market")) AND PUBYEAR = 2025'

# Parámetros de la consulta
params = {
    "query": query,
    "apiKey": API_KEY,
    "httpAccept": "application/json",
    "view": "COMPLETE",
    "start": 0,
    "count": 25  
}

# Creamos una lista para almacenar los datos (fuera del bucle)
publications = []

while True:
    # Realizamos la solicitud a la API
    response = requests.get(BASE_URL, headers={"X-ELS-APIKey": API_KEY}, params=params)

    # Verificamos si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        results = data.get("search-results", {}).get("entry", [])

        for entry in results:
            title = entry.get("dc:title", "")
            journal = entry.get("prism:publicationName", "")
            year = entry.get("prism:coverDate", "")[:4]
            pub_type = entry.get("subtypeDescription", "")  
            abstract = entry.get("dc:description", "")  
            doi = entry.get('prism:doi', '')

            # Extraemos información de autores
            authors = entry.get("author", [])
            author_info = [author.get("authname", "") for author in authors]

            # Unimos a los autores en una sola cadena separada por punto y coma
            author_names = '; '.join(author_info)
            
            # Agregamos datos a la lista
            publications.append([title, author_names, journal, year, pub_type, abstract, doi])

        # Verificamos si hay más páginas
        total_results = int(data.get('search-results', {}).get('opensearch:totalResults', 0))
        items_per_page = int(data.get('search-results', {}).get('opensearch:itemsPerPage', 25))
        current_start = int(params['start'])
        next_start = current_start + items_per_page

        if next_start >= total_results:
            break  
        else:
            params['start'] = next_start  

    else:
        print(f"Error en la solicitud: {response.status_code}")
        print(response.text)  
        break

# Creamos un DataFrame de pandas
df = pd.DataFrame(publications, columns=["Título", "Autores", "Revista", "Año", "Tipo de Publicación", "Resumen", "DOI"])

# Nombramos al archivo Excel
excel_file = "scopus_publications.xlsx"
    
# Exportamos a Excel
df.to_excel(excel_file, index=False)
print(f"Datos exportados correctamente a '{excel_file}'")
    
# Abrimos el archivo automáticamente
try:
    if os.name == "nt":  # Windows
        os.startfile(excel_file)
    elif os.name == "posix":  # macOS/Linux
        subprocess.run(["open" if "darwin" in os.sys.platform else "xdg-open", excel_file])
except Exception as e:
    print(f"No se pudo abrir el archivo automáticamente: {e}")
    
else:
    print(f"Error en la solicitud: {response.status_code} - {response.text}")
