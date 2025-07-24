import requests
import json

def consultar_cliente(cedula):
    url = "http://localhost:5003/cliente"  
    headers = {"Content-Type": "application/json"}
    payload = {"ci": cedula}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el servicio: {e}")
        return None

if __name__ == '__main__':
    print("--- Consultando cliente existente (CI: 4133266) ---")
    resultado1 = consultar_cliente("4133266")
    if resultado1:
        print(json.dumps(resultado1, indent=4))

    print("\n--- Consultando cliente no existente (CI: 4133267) ---")
    resultado2 = consultar_cliente("4133267")
    if resultado2:
        print(json.dumps(resultado2, indent=4))

    print("\n--- Consultando cliente con cédula vacía ---")
    resultado3 = consultar_cliente("")
    if resultado3:
        print(json.dumps(resultado3, indent=4))

    print("\n--- Consultando cliente con formato de CI incorrecto (ejemplo: 'abc') ---")
    resultado4 = consultar_cliente("abc")
    if resultado4:
        print(json.dumps(resultado4, indent=4))