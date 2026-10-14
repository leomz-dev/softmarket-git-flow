"""Pruebas unitarias del caso de uso RegistrarCliente."""
import pytest

from softmarket.aplicacion.registrar_cliente import RegistrarCliente
from softmarket.dominio.cliente import Cliente, TipoCliente
from softmarket.dominio.validadores import ValidadorEmail, ValidadorNombre


class RepositorioEnMemoria:
    """Doble de prueba del puerto RepositorioClientes."""

    def __init__(self) -> None:
        self.guardados: list[Cliente] = []

    def guardar(self, cliente: Cliente) -> None:
        self.guardados.append(cliente)

    def buscar(self, email: str) -> Cliente | None:
        return next((c for c in self.guardados if c.email == email), None)


class NotificadorEspia:
    """Doble de prueba del puerto ServicioNotificacion."""

    def __init__(self) -> None:
        self.notificados: list[Cliente] = []

    def notificar(self, cliente: Cliente) -> None:
        self.notificados.append(cliente)


def armar_caso_de_uso():
    repositorio = RepositorioEnMemoria()
    notificador = NotificadorEspia()
    caso = RegistrarCliente(
        validadores=[ValidadorNombre(), ValidadorEmail()],
        repositorio=repositorio,
        notificador=notificador,
    )
    return caso, repositorio, notificador


def test_registra_un_cliente_valido():
    caso, repositorio, notificador = armar_caso_de_uso()
    cliente = Cliente("SoftMarket", "contacto@softmarket.dev", TipoCliente.CORPORATIVO, 5000.0)

    caso.ejecutar(cliente)

    assert repositorio.guardados == [cliente]
    assert notificador.notificados == [cliente]


def test_rechaza_un_nombre_demasiado_corto():
    caso, repositorio, _ = armar_caso_de_uso()
    cliente = Cliente("Al", "al@softmarket.dev", TipoCliente.MINORISTA, 10.0)

    with pytest.raises(ValueError):
        caso.ejecutar(cliente)

    assert repositorio.guardados == []


def test_rechaza_un_correo_sin_dominio_con_punto():
    caso, repositorio, _ = armar_caso_de_uso()
    cliente = Cliente("Ana Pérez", "ana@softmarket", TipoCliente.MINORISTA, 10.0)

    with pytest.raises(ValueError):
        caso.ejecutar(cliente)

    assert repositorio.guardados == []


def test_rechaza_un_corporativo_sin_saldo_minimo():
    caso, repositorio, _ = armar_caso_de_uso()
    cliente = Cliente("Corporativo XYZ", "pagos@xyz.dev", TipoCliente.CORPORATIVO, 500.0)

    with pytest.raises(ValueError):
        caso.ejecutar(cliente)

    assert repositorio.guardados == []
