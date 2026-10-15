# ADR 0002: Aplicar SOLID en el módulo de clientes

- Estado: aceptado
- Fecha: 2026-09-10
- Decisores: Leonardo Meza, Camila Serge

## Contexto

La clase ClienteService concentraba validación, reglas de saldo, persistencia en
SQLite y notificación por SMTP. Cada nuevo tipo de cliente obligaba a modificar
la misma clase y no era posible probarla sin base de datos ni servidor de correo.

## Decisión

Separar responsabilidades en cuatro piezas y depender de abstracciones:

- El dominio define entidades, políticas y puertos (Protocol).
- La aplicación contiene el caso de uso RegistrarCliente.
- La infraestructura implementa los puertos con SQLite y SMTP.
- La composición ocurre en interfaces/api.py mediante inyección de dependencias.

## Consecuencias

- Positivas: clases con una sola razón de cambio, extensión sin modificar lo
  existente y pruebas unitarias sin infraestructura.
- Negativas: más archivos y una indirección adicional que el equipo debe conocer.
