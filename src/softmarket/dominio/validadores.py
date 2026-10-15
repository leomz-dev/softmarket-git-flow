"""Validadores de cliente: cada uno con una sola responsabilidad."""
from softmarket.dominio.cliente import Cliente

LONGITUD_MINIMA_NOMBRE = 3


class ValidadorNombre:
    """Verifica que el nombre tenga la longitud mínima."""

    def validar(self, cliente: Cliente) -> None:
        if len(cliente.nombre.strip()) < LONGITUD_MINIMA_NOMBRE:
            raise ValueError("El nombre debe tener al menos 3 caracteres")


class ValidadorEmail:
    """Verifica que el correo tenga usuario y dominio con punto."""

    def validar(self, cliente: Cliente) -> None:
        usuario, separador, dominio = cliente.email.partition("@")
        if not separador or not usuario or "." not in dominio:
            raise ValueError("El correo electrónico no es válido")
