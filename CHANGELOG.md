# Registro de cambios

Todas las modificaciones relevantes se documentan en este archivo. El formato
sigue las convenciones de Keep a Changelog y el versionado semántico.

## [1.0.1] - 2026-09-29

### Corregido

- La transacción sobre SQLite no se confirmaba al guardar un cliente, por lo
  que el registro se perdía. Se agrega la confirmación y una prueba de
  integración que reproduce el fallo.

## [1.0.0] - 2026-09-22

### Agregado

- Registro de clientes con validación de nombre y correo electrónico.
- Políticas de saldo mínimo por tipo de cliente (corporativo y minorista).
- Cálculo de IVA con estrategia por tarifa y redondeo a dos decimales.
- Pruebas unitarias del caso de uso y del cálculo de facturas.
- Integración continua con Ruff y pytest.
