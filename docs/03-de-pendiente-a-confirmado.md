# Sesión 3 · De pendiente a confirmado

[Anterior: sesión 2](02-seguir-un-pago.md) · [Recorrido](README.md) · [Después: objetivos de las sesiones 4–8](README.md#mapa-de-sesiones)

**Pregunta:** ¿qué cambia exactamente cuando un pago entra en un bloque?

**Punto de partida:** el pago pendiente de la sesión 2 y el mismo directorio de datos. Si ya se confirmó, anotar qué ocurrió y preparar un nuevo pago equivalente. Nunca presentar un estado reconstruido como una captura del experimento anterior.

**Lo que construirás:** un seguimiento pequeño en Python que compare el mismo pago antes y después de generar bloques. Tú decides si usa consultas puntuales, un bucle u otra organización. No necesita interfaz web ni servicio permanente.

## Predice antes de generar un bloque

- ¿El hecho de que Bob vea el pago implica que esté confirmado?
- ¿Qué esperas encontrar en la mempool del nodo y qué en la cadena?
- ¿Qué dato cambiará al generar un bloque? ¿Y al generar otro?
- ¿Esperas que cambie el identificador de este mismo pago solo por confirmarse?

## Preparar una observación limpia

Registrar la altura actual, el identificador del pago y las wallets implicadas. Para los bloques nuevos, usar una dirección de recompensa de una tercera wallet de laboratorio, dedicada a minería. Así la recompensa nueva no se mezcla con el pago que sigues en Alice y Bob.

Si las wallets ya contienen recompensas antiguas, pueden madurar al avanzar la cadena. Por eso el objeto principal del experimento será esta transacción y sus salidas concretas, no solo la diferencia de saldo global.

## Experimento guiado

1. Observar el pago desde la wallet de Alice, desde Bob y desde la mempool del nodo. Identificar qué pregunta responde cada consulta.
2. Guardar una primera observación antes de generar bloques. Distinguir la información de cadena de la información local sobre transacciones pendientes.
3. Generar un bloque dirigido a la wallet de minería.
4. Comprobar que el pago está realmente incluido en ese bloque. No asumirlo solo porque has generado uno.
5. Consultar de nuevo la misma transacción, las salidas relevantes y la mempool. Comparar con la observación anterior.
6. Generar otro bloque y repetir. Justificar el número de confirmaciones usando las alturas observadas.
7. Implementar en Python una forma de obtener y comparar estas observaciones sin fijar de antemano los valores que esperas ver.

Si el pago no entra, el experimento sigue siendo útil: investigar su presencia en mempool, validez, tasa y posibles dependencias antes de repetir a ciegas.

## Cómo interpretar los resultados

La mempool es local a cada nodo; en este laboratorio observamos la de uno. No existe una única cola mundial con un estado idéntico para todos.

Una wallet puede mostrar fondos pendientes o tratar de forma distinta su propio cambio y un pago recibido. Confirmación, visibilidad y posibilidad de gasto no son sinónimos. Hay que decir qué consulta y qué filtros se han utilizado.

Confirmarse no cambia por sí solo los bytes de la transacción observada. Añade contexto de inclusión en la cadena. Una reorganización podría cambiar esa inclusión: la estudiaremos con varios nodos en la sesión 8.

## Una variación

Parar el nodo ordenadamente, volver a iniciarlo con los mismos datos y consultar el pago confirmado. Predecir primero qué debería conservarse. Si una consulta de wallet falla, distinguir wallet sin cargar de pérdida de los datos.

## Para cerrar

- Hay tres observaciones reales del mismo pago: pendiente, incluido en un bloque y con un bloque posterior.
- Puedes mostrar el bloque que contiene el pago y explicar cómo contaste las confirmaciones.
- Puedes explicar por qué ver un pago, encontrarlo en mempool y confirmarlo son observaciones distintas.
- Tu explicación no depende de que todos los saldos globales cambien de una manera concreta.
- Puedes volver a consultar el resultado después de reiniciar el nodo.

Guardar el código y una [nota](plantilla-sesion.md). Actualizar [progreso](progreso.md) con lo que has ejecutado y explicado. Las dudas sobre conflictos o reorganizaciones servirán para preparar las siguientes sesiones.

<details>
<summary>Pistas de diagnóstico</summary>

- Busca operaciones de mempool, consulta de bloques y consulta de wallet en `help`. Compara sus alcances antes de elegir una.
- Algunas consultas de mempool devuelven un error si la transacción ya no está allí. Esa ausencia no demuestra por sí sola confirmación: comprueba el bloque.
- La aceptación de una transacción pendiente y su selección para un bloque no son la misma operación.
- Si el total de Alice sube mientras sigues un pago saliente, revisa si ha madurado una recompensa anterior. Eso no invalida la contabilidad de la transacción.
- Un pago confirmado en la cadena activa con altura de inclusión conocida permite deducir sus confirmaciones a partir de la altura actual. Revisa el caso de su primer bloque antes de generalizar la fórmula.

</details>

## Referencias

- [Referencia RPC de Bitcoin Core 30.0](https://bitcoincore.org/en/doc/30.0.0/): familias blockchain y wallet.
- [Confirmaciones y contexto de wallet: gettransaction](https://bitcoincore.org/en/doc/30.0.0/rpc/wallet/gettransaction/).
- [Control de bloques en regtest](https://developer.bitcoin.org/examples/testing.html#regtest-mode).
