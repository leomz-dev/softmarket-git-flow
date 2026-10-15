# ADR 0001: Adoptar Git Flow como modelo de ramas

- Estado: aceptado
- Fecha: 2026-09-08
- Decisores: Leonardo Meza, Camila Serge

## Contexto

El equipo publicaba cambios directamente en la rama principal, sin ramas por
funcionalidad ni revisiones. Los errores llegaban a producción y no era posible
saber qué versión estaba desplegada.

## Decisión

Adoptar Git Flow adaptado: dos ramas permanentes (main y develop) y tres tipos
de ramas de soporte (feature, release y hotfix). main y develop quedan
protegidas: no admiten commits directos, solo merges mediante pull request con
al menos una aprobación y la integración continua en verde.

## Consecuencias

- Positivas: historia trazable, versiones identificables con etiquetas y
  separación clara entre desarrollo, preparación y producción.
- Negativas: exige más disciplina y agrega pasos antes de integrar.
