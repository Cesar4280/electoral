from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

app.config["MYSQL_DB"] = "votacion"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def hello():
    return jsonify({"ping": "pong" })

@app.route("/votantes/<string:dni>/", methods=["GET", "POST"])
def add_voter(dni):
    connection = mysql.connection
    if connection is None:
        return print("Bad connection!")
    cursor = connection.cursor()
    if request.method == "POST":
        cursor.execute("""
            INSERT INTO votante(
                edad,
                cedula,
                primer_nombre,
                otros_nombres, 
                primer_apellido,
                otros_apellidos,
                candidato_id
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            request.json["edad"],
            request.json["cedula"],
            request.json["primer_nombre"],
            request.json["otros_nombres"],
            request.json["primer_apellido"],
            request.json["otros_apellidos"],
            request.json["candidato_id"]
        ))
        connection.commit()
    else:
        cursor.execute("""
            SELECT * 
                FROM votante 
            WHERE 
                cedula = %s
            LIMIT 1
        """, (dni,))
        voter = cursor.fetchone()
        print(voter)
        return jsonify({ "data": voter, "success": bool(voter) })
    cursor.close()

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)