# importamos el modulo requests
import requests

# Creamos la instancia a la API
API_KEY = 'cH6wfcwfKZntuT2Nd6bP5VxNcQfr120S2I8dP4xA'
API_URL = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'

# Creamos la funcion para obtener la informacion de la API
def get_info(url):
    # Creamos la variable para almacenar la informacion
    info = None

    # Hacemos una peticion a la API
    response = requests.get(url)

    # Si la peticion fue exitosa
    if response.status_code == 200:
        # Obtenemos la informacion de la API
        info = response.json()
        
        # Verificamos si la informacion es valida
        if 'title' and 'date' and 'explanation' and 'hdurl' and 'copyright' in info:
            # Mostramos la informacion
            print(f"Título: {info['title']}\n")
            print(f"Fecha: {info['date']}\n")
            print(f"Explicación: {info['explanation']}\n")
            print(f"derechos de autor: {info['copyright']}\n")

            # Guardo la imagen en un archivo en el directorio actual
            with open(f"{info['title']}.jpg".replace("\:|\!|\?", '') , "wb") as f:
                f.write(requests.get(info['hdurl']).content)

            # Retornamos ok
            return f"¡Listo! {response.status_code}"

        else:
            # Retornamos error
            return "Error: No se pudo obtener la informacion"

    else:
        print('¡Error! Verifique la URL\n')

        # Retornamos error
        return f"Error: {response.status_code}, info: {info}"


print(get_info(API_URL))