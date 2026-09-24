# Del taller a una primera contribución

[Recorrido](README.md)

Las ocho sesiones dan una base práctica para entender una reproducción de un fallo y empezar a leer tests. Contribuir requiere además conocer las convenciones, el entorno y el comportamiento concreto del proyecto elegido.

No hace falta esperar a saberlo todo para revisar documentación o reproducir un problema. Tampoco hay que dar por hecho que un test útil se escribirá en una tarde.

## Un puente de tres pasos

| Paso | Trabajo | Criterio para avanzar |
| --- | --- | --- |
| 1. Leer y ejecutar | Elegir un proyecto, seguir su guía de desarrollo y ejecutar una prueba relevante. En Core, leer `example_test.py` y un test funcional cercano a lo que ya experimentaste. | Explicar qué prepara, qué acción realiza y qué comprueba. Poder repetirla. |
| 2. Investigar un caso | Buscar un fallo acotado o una PR que necesite pruebas. Comprobar su estado actual y reproducir el comportamiento en una versión identificada. | Conservar una secuencia mínima, resultado esperado y observado. Distinguir un fallo del producto de un error del experimento. |
| 3. Aportar | Escribir una reproducción, revisar un test o proponer uno nuevo siguiendo las convenciones del proyecto. | Entender cada comprobación y explicar qué regresión detecta. Para una corrección, comprobar el caso antes y después cuando sea posible. |

El primer resultado puede ser una reproducción útil o una revisión bien explicada. No depende de encontrar enseguida una modificación que los mantenedores quieran incorporar.

## Dónde encaja Python

- **Bitcoin Core:** sus tests funcionales usan Python para controlar nodos y comprobar comportamientos RPC y P2P. El código de producto está mayoritariamente en C++; algunos fallos requieren leerlo o modificarlo. [Guía de tests](https://github.com/bitcoin/bitcoin/blob/master/test/functional/README.md) y [ejemplo comentado](https://github.com/bitcoin/bitcoin/blob/master/test/functional/example_test.py).
- **Electrum:** buena opción si interesa profundizar en wallets con Python. Hace falta aprender su arquitectura y ejecutar su suite; las guías del taller no cubren toda la seguridad de una wallet. [Contribuir a Electrum](https://github.com/spesmilo/electrum#contributing).
- **Warnet:** escenarios de experimentación de redes en Python. Añade conocimientos de contenedores y despliegue; puede tener sentido después del experimento con dos nodos. [Escenarios](https://github.com/bitcoin-dev-project/warnet/blob/main/docs/scenarios.md).

La elección se hará después de comprobar qué partes del taller te han interesado. No hay issues reservados ni tareas externas prometidas.

## Usar IA al contribuir

El tutor puede ayudarte a entender un fragmento, localizar documentación o revisar una hipótesis. Tú debes poder explicar el cambio, sus pruebas y sus límites.

Bitcoin Core permite ayuda de IA bajo condiciones: conocer el lenguaje, entender el código y asumir la autoría humana. Su política exige comunicación propia con mantenedores y no admite PRs conducidas por agentes autónomos. Consultar la [política vigente](https://github.com/bitcoin/bitcoin/blob/master/doc/AI_POLICY.md) antes de participar; otros proyectos pueden tener reglas distintas.

## Cómo decidir si estás preparado

Cuando puedas leer un test pequeño, anticipar su resultado, introducir una variación y explicar por qué falla o pasa, tienes un punto de partida para investigar una contribución de ese alcance. Eso no acredita todavía capacidad para revisar consenso, diseñar criptografía o auditar una wallet.

El [PR Review Club](https://bitcoincore.reviews/) ofrece lecturas y discusiones para aprender el proceso de revisión. Sus archivos se pueden consultar sin comprometerse a una actividad programada.
