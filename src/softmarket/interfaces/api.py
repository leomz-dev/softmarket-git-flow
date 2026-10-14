"""Punto de entrada de ejemplo: composición e invocación del caso de uso."""
import sqlite3

from softmarket.aplicacion.registrar_cliente import RegistrarCliente
from softmarket.dominio.cliente import Cliente, TipoCliente
from softmarket.dominio.validadores import ValidadorEmail, ValidadorNombre
from softmarket.infraestructura.notificador_email import NotificadorEmail
from softmarket.infraestructura.repositorio_sqlite import RepositorioClientesSqlite

SERVIDOR_SMTP = "smtp.softmarket.dev"
RUTA_BASE_DATOS = "softmarket.db"


def construir_registrador() -> RegistrarCliente:
    """Compone las dependencias concretas y devuelve el caso de uso listo."""
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    return RegistrarCliente(
        validadores=[ValidadorNombre(), ValidadorEmail()],
        repositorio=RepositorioClientesSqlite(conexion),
        notificador=NotificadorEmail(SERVIDOR_SMTP),
    )


def registrar_cliente_demo(nombre: str, email: str, saldo: float) -> None:
    """Registra un cliente corporativo de demostración."""
    cliente = Cliente(
        nombre=nombre,
        email=email,
        tipo=TipoCliente.CORPORATIVO,
        saldo=saldo,
    )
    construir_registrador().ejecutar(cliente)
