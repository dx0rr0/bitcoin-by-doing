# Bitcoin by doing

Me gusta mucho Bitcoin y quiero entender cómo funciona por dentro. Empecé con *Programming Bitcoin*, pero la parte de matemáticas se me hizo cuesta arriba. Aquí voy a aprender haciendo experimentos en Python y volviendo a la teoría cuando la necesite.

El recorrido empieza con un nodo local de pruebas. Después vienen las transacciones, las firmas, los bloques y algunos experimentos con varios nodos. La criptografía se usa primero; sus matemáticas quedan para profundizar más adelante.

**Estado:** guías de las sesiones 0–3 preparadas. Los ejercicios todavía no están hechos y el entorno se comprobará en la sesión 0.

## Por dónde empezar

1. Leer [cómo trabajaremos](docs/metodo.md).
2. Abrir la [sesión 0: preparar el entorno juntos](docs/00-empezar-juntos.md).
3. Continuar con las sesiones [1](docs/01-donde-estan-los-bitcoins.md), [2](docs/02-seguir-un-pago.md) y [3](docs/03-de-pendiente-a-confirmado.md).

Cada sesión tiene una pregunta, un experimento y una comprobación de lo aprendido. Los ejercicios no incluyen soluciones, funciones vacías ni interfaces que tenga que seguir. El diseño del código también forma parte del aprendizaje.

## El recorrido

| Sesión | Pregunta | Material |
| --- | --- | --- |
| 0 | ¿Cómo preparo un entorno que entiendo y puedo volver a arrancar? | [Guía](docs/00-empezar-juntos.md) |
| 1 | ¿Dónde están los bitcoins de una wallet? | [Guía](docs/01-donde-estan-los-bitcoins.md) |
| 2 | ¿Qué ocurre cuando envío un pago? | [Guía](docs/02-seguir-un-pago.md) |
| 3 | ¿Qué cambia cuando se confirma? | [Guía](docs/03-de-pendiente-a-confirmado.md) |
| 4 | ¿Qué impide gastar dos veces lo mismo? | Por preparar |
| 5 | ¿Qué autoriza una firma? | Por preparar |
| 6 | ¿Cómo se representa una transacción en bytes? | Por preparar |
| 7 | ¿Qué significa minar un bloque? | Por preparar |
| 8 | ¿Cómo convergen dos nodos que conocen historias distintas? | Por preparar |

[Alcance y profundidad](docs/README.md) · [Progreso](docs/progreso.md) · [Puente a open source](docs/hacia-open-source.md)

## Qué habrá aquí

```text
docs/          Guías, recorrido y seguimiento
experiments/   El código que vaya escribiendo durante las sesiones
notes/         Mis predicciones, resultados y explicaciones
```

La instalación se decide en la sesión 0. Todavía no hay dependencias Python, scripts de arranque ni una arquitectura elegida. Los datos del nodo y las wallets quedan fuera de Git.

## Referencias

Las guías se apoyan en la documentación de Bitcoin Core y en ejercicios propios. *Programming Bitcoin*, de Jimmy Song, queda como referencia para profundizar; este repositorio no reproduce sus ejercicios ni sus soluciones.

[Fuentes y documentación](docs/recursos.md)
