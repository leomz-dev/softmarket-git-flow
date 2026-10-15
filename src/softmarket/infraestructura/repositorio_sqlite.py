"""Adaptador de persistencia sobre SQLite."""
import sqlite3

from softmarket.dominio.cliente import Cliente, TipoCliente

ESQUEMA = (
    "CREATE TABLE IF NOT EXISTS clientes ("
    " nombre TEXT NOT NULL,"
    " email TEXT NOT NULL UNIQUE,"
    " tipo TEXT NOT NULL,"
    " saldo REAL NOT NULL"
    ")"
)


class RepositorioClientesSqlite:
    """Implementa el puerto RepositorioClientes usando SQLite."""

    def __init__(self, conexion: sqlite3.Connection) -> None:
        self._conexion = conexion
        self._conexion.execute(ESQUEMA)

    def guardar(self, cliente: Cliente) -> None:
        """Inserta el cliente y confirma la transacción."""
        cursor = self._conexion.cursor()
        cursor.execute(
            "INSERT INTO clientes (nombre, email, tipo, saldo) VALUES (?, ?, ?, ?)",
            (cliente.nombre, cliente.email, cliente.tipo.value, cliente.saldo),
        )
        self._conexion.commit()

    def buscar(self, email: str) -> Cliente | None:
        """Recupera un cliente por su correo electrónico."""
        fila = self._conexion.execute(
            "SELECT nombre, email, tipo, saldo FROM clientes WHERE email = ?",
            (email,),
        ).fetchone()
        if fila is None:
            return None
        return Cliente(
            nombre=fila[0],
            email=fila[1],
            tipo=TipoCliente(fila[2]),
            saldo=float(fila[3]),
        )
