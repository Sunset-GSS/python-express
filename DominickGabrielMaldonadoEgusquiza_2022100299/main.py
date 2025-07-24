from flask import Flask, request, jsonify

app = Flask(__name__)

clientes_db = {
    "4133266": {"nombre": "Derlis", "apellidos": "Caballero Mendoza"}
}

@app.route('/cliente', methods=['POST'])
def obtener_cliente():

    if not request.is_json:
        return jsonify({
            "accion": "Error en el formato de la solicitud",
            "codRes": "ERROR",
            "menRes": "Se esperaba un JSON",
            "ci": None
        }), 400

    data = request.get_json()
    cedula = data.get("ci")

    if not cedula:
        return jsonify({
            "accion": "Error",
            "codRes": "ERROR",
            "menRes": "Cédula no proporcionada",
            "ci": None
        }), 400

    cliente = clientes_db.get(cedula)

    if cliente:
        return jsonify({
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": cedula,
            "nombre": cliente["nombre"],
            "apellidos": cliente["apellidos"]
        }), 200
    else:
        return jsonify({
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": cedula
        }), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003, debug=True)