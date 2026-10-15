"""Puertos que el dominio exige al exterior."""
from typing import Protocol

from softmarket.dominio.cliente import Cliente


class ValidadorCliente(Protocol):
    """Contrato de validación de un cliente."""

    def validar(self, cliente: Cliente) -> None:
        """Valida el cliente o lanza ValueError."""
        ...


class RepositorioClientes(Protocol):
    """Contrato de persistencia de clientes."""

    def guardar(self, cliente: Cliente) -> None:
        """Persiste el cliente."""
        ...

    def buscar(self, email: str) -> Cliente | None:
        """Devuelve el cliente con ese correo, o None si no existe."""
        ...


class ServicioNotificacion(Protocol):
    """Contrato de notificación a clientes."""

    def notificar(self, cliente: Cliente) -> None:
        """Envía la notificación de bienvenida."""
        ...
