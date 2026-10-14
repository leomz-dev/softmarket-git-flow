"""Caso de uso: registrar un cliente nuevo."""
from softmarket.dominio.cliente import Cliente, politica_para
from softmarket.dominio.puertos import (
    RepositorioClientes,
    ServicioNotificacion,
    ValidadorCliente,
)


class RegistrarCliente:
    """Orquesta validación, política de saldo, persistencia y notificación."""

    def __init__(
        self,
        validadores: list[ValidadorCliente],
        repositorio: RepositorioClientes,
        notificador: ServicioNotificacion,
    ) -> None:
        self._validadores = validadores
        self._repositorio = repositorio
        self._notificador = notificador

    def ejecutar(self, cliente: Cliente) -> None:
        """Registra al cliente o lanza ValueError si no cumple las reglas."""
        for validador in self._validadores:
            validador.validar(cliente)

        politica = politica_para(cliente.tipo)
        if cliente.saldo < politica.saldo_minimo():
            raise ValueError(
                "El saldo mínimo para el tipo "
                + cliente.tipo.value
                + " es "
                + str(politica.saldo_minimo())
            )

        self._repositorio.guardar(cliente)
        self._notificador.notificar(cliente)
