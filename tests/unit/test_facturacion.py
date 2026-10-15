"""Pruebas unitarias del cálculo de facturas."""
from decimal import Decimal

from softmarket.aplicacion.facturar import IvaColombia, IvaExento, emitir_factura


def test_calcula_el_iva_al_19_por_ciento():
    factura = emitir_factura(Decimal("100.00"), IvaColombia())

    assert factura.impuesto == Decimal("19.00")
    assert factura.total == Decimal("119.00")


def test_redondea_el_impuesto_a_dos_decimales():
    factura = emitir_factura(Decimal("15.30"), IvaColombia())

    assert factura.impuesto == Decimal("2.91")


def test_la_tarifa_exenta_no_cobra_impuesto():
    factura = emitir_factura(Decimal("100.00"), IvaExento())

    assert factura.impuesto == Decimal("0.00")
    assert factura.total == Decimal("100.00")
