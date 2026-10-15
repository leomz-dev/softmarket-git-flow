"""Pruebas de integración del adaptador SQLite."""
import sqlite3

from softmarket.dominio.cliente import Cliente, TipoCliente
from softmarket.infraestructura.repositorio_sqlite import RepositorioClientesSqlite


def test_guarda_y_recupera_un_cliente():
    conexion = sqlite3.connect(":memory:")
    repositorio = RepositorioClientesSqlite(conexion)
    cliente = Cliente("Distribuidora Sur", "compras@sur.dev", TipoCliente.CORPORATIVO, 2500.0)

    repositorio.guardar(cliente)

    assert repositorio.buscar("compras@sur.dev") == cliente


def test_devuelve_none_si_el_cliente_no_existe():
    conexion = sqlite3.connect(":memory:")
    repositorio = RepositorioClientesSqlite(conexion)

    assert repositorio.buscar("nadie@softmarket.dev") is None
