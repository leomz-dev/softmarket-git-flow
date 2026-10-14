# ADR 0003: Conventional Commits y versionado semántico

- Estado: aceptado
- Fecha: 2026-09-12
- Decisores: Leonardo Meza, Camila Serge

## Contexto

Los mensajes de commit eran genéricos ("cambios", "fix") y no existían
etiquetas de versión, de modo que era imposible reconstruir la historia o saber
qué versión estaba publicada.

## Decisión

Usar Conventional Commits con el formato tipo(alcance): descripción, con los
tipos feat, fix, docs, style, refactor, test, chore, perf y ci. Aplicar
versionado semántico (MAJOR.MINOR.PATCH) a las etiquetas de main.

## Consecuencias

- Positivas: historial legible, generación automática de cambios y versiones
  predecibles.
- Negativas: el equipo debe recordar la convención; se apoya en revisión de
  código y en la plantilla de pull request.
