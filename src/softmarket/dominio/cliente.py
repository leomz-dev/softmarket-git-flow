"""Entidades y políticas de negocio del cliente."""
from dataclasses import dataclass
from enum import Enum


class TipoCliente(Enum):
    """Tipos de cliente soportados por SoftMarket."""

    CORPORATIVO = "corporativo"
    MINORISTA = "minorista"


@dataclass(frozen=True)
class Cliente:
    """Cliente del sistema: entidad inmutable del dominio."""

    nombre: str
    email: str
    tipo: TipoCliente
    saldo: float


class PoliticaSaldo:
    """Política de saldo mínimo exigido a un tipo de cliente."""

    def saldo_minimo(self) -> float:
        """Devuelve el saldo mínimo exigido."""
        return 0.0


class PoliticaCorporativo(PoliticaSaldo):
    """Un cliente corporativo debe mantener un saldo mínimo."""

    def saldo_minimo(self) -> float:
        return 1000.0


class PoliticaMinorista(PoliticaSaldo):
    """Un cliente minorista no puede tener saldo negativo."""

    def saldo_minimo(self) -> float:
        return 0.0


POLITICAS_POR_TIPO = {
    TipoCliente.CORPORATIVO: PoliticaCorporativo,
    TipoCliente.MINORISTA: PoliticaMinorista,
}


def politica_para(tipo: TipoCliente) -> PoliticaSaldo:
    """Devuelve la política de saldo correspondiente al tipo de cliente."""
    if tipo not in POLITICAS_POR_TIPO:
        raise ValueError("Tipo de cliente sin política de saldo definida")
    return POLITICAS_POR_TIPO[tipo]()
