import sqlite3
from pathlib import Path

BANCO = Path(__file__).parent / "jarvis.db"


def _conectar():
    return sqlite3.connect(BANCO)


def iniciar():
    """Cria a tabela de fatos se ela ainda não existir."""
    con = _conectar()
    con.execute(
        """CREATE TABLE IF NOT EXISTS fatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL,
            criado_em TEXT DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    con.commit()
    con.close()


def salvar(texto):
    con = _conectar()
    con.execute("INSERT INTO fatos (texto) VALUES (?)", (texto,))
    con.commit()
    con.close()


def listar():
    con = _conectar()
    linhas = con.execute("SELECT id, texto FROM fatos ORDER BY id").fetchall()
    con.close()
    return linhas


def apagar(id_fato):
    con = _conectar()
    apagados = con.execute("DELETE FROM fatos WHERE id = ?", (id_fato,)).rowcount
    con.commit()
    con.close()
    return apagados > 0