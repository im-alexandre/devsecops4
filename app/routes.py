from pathlib import Path
import sqlite3

from flask import Flask, jsonify, request

DB_PATH = Path("clientes.db")
app = Flask(__name__)


def conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def inicializar_banco():
    with conectar() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS clientes ("
            "id INTEGER PRIMARY KEY, "
            "nome TEXT NOT NULL, "
            "email TEXT NOT NULL)"
        )
        conn.execute("DELETE FROM clientes")
        conn.executemany(
            "INSERT INTO clientes (nome, email) VALUES (?, ?)",
            [
                ("Ana Lima", "ana@example.com"),
                ("Bruno Costa", "bruno@example.com"),
            ],
        )
        conn.commit()


@app.get("/clientes")
def buscar_clientes():
    nome = request.args.get("nome", "")
    sql = "SELECT id, nome, email FROM clientes WHERE nome = ?"

    with conectar() as conn:
        resultados = conn.execute(sql, (nome,)).fetchall()

    return jsonify([dict(cliente) for cliente in resultados])


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    inicializar_banco()
    app.run(host="127.0.0.1", port=5000, debug=False)
