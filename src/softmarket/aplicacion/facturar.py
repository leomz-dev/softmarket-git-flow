"""Caso de uso: emitir una factura."""
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from typing import Protocol

DOS_DECIMALES = Decimal("0.01")


class CalculadoraImpuesto(Protocol):
    """Contrato para calcular el impuesto de una base gravable."""

    def calcular(self, base: Decimal) -> Decimal:
        """Devuelve el impuesto correspondiente a la base."""
        ...


class IvaColombia:
    """IVA del 19 por ciento aplicado en Colombia."""

    TARIFA = Decimal("0.19")

    def calcular(self, base: Decimal) -> Decimal:
        return (base * self.TARIFA).quantize(DOS_DECIMALES, rounding=ROUND_HALF_UP)


class IvaExento:
    """Tarifa cero para productos exentos."""

    def calcular(self, base: Decimal) -> Decimal:
        return Decimal("0.00")


@dataclass(frozen=True)
class Factura:
    """Resultado del cálculo de una factura."""

    base: Decimal
    impuesto: Decimal
    total: Decimal


def emitir_factura(base: Decimal, calculadora: CalculadoraImpuesto) -> Factura:
    """Calcula el impuesto y el total de una factura."""
    impuesto = calculadora.calcular(base)
    return Factura(base=base, impuesto=impuesto, total=base + impuesto)
