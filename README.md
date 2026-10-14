# SoftMarket

Núcleo de gestión de clientes y facturación de SoftMarket S.A., refactorizado
aplicando los principios SOLID sobre un flujo de versionamiento Git Flow.

## Problema que resuelve

El código original concentraba la validación, las reglas de negocio, la
persistencia y la notificación en una sola clase acoplada directamente a SQLite
y a SMTP. En esta versión el dominio no conoce la infraestructura: los casos de
uso dependen de abstracciones (puertos) y la composición se hace en el borde
del sistema.

## Estructura del proyecto

    softmarket/
    |-- src/softmarket/
    |   |-- dominio/          entidades, políticas, validadores y puertos
    |   |-- aplicacion/       casos de uso
    |   |-- infraestructura/  adaptadores de SQLite y SMTP
    |   |-- interfaces/       punto de entrada y composición
    |-- tests/
    |   |-- unit/             pruebas sin base de datos ni red
    |   |-- integration/      pruebas contra SQLite en memoria
    |-- docs/adr/             registros de decisiones de arquitectura
    |-- .github/workflows/    integración continua

## Requisitos

- Python 3.11 o superior

## Instalación

    python -m venv .venv
    .venv/Scripts/activate
    pip install -e ".[dev]"

## Pruebas

    pytest

## Modelo de ramas

- main: código en producción, siempre estable; cada merge recibe una etiqueta.
- develop: rama de integración donde convergen las funcionalidades.
- feature/*: una rama por funcionalidad; nace de develop y regresa a develop.
- release/*: preparación de una versión.
- hotfix/*: corrección urgente sobre producción.

Nota: en este repositorio de demostración las ramas de soporte se conservan
después del merge para poder ver el modelo completo. En operación normal se
eliminan al integrarse.

## Convención de commits

Los mensajes siguen Conventional Commits:

    feat(clientes): agrega la entidad Cliente y las políticas de saldo
    fix(facturacion): redondea el impuesto a dos decimales
    test(clientes): cubre el caso de uso RegistrarCliente

## Flujo de contribución

1. Crear una rama feature/nombre a partir de develop.
2. Confirmar cambios pequeños con mensajes Conventional Commits.
3. Abrir un pull request hacia develop y solicitar revisión.
4. Esperar la integración continua en verde y al menos una aprobación.
5. Fusionar con --no-ff y eliminar la rama.

## Decisiones de arquitectura

El detalle de las decisiones está en docs/adr.
