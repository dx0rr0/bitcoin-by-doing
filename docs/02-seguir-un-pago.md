# Sesión 2 · Seguir un pago de principio a fin

[Anterior: sesión 1](01-donde-estan-los-bitcoins.md) · [Recorrido](README.md) · [Siguiente: sesión 3](03-de-pendiente-a-confirmado.md)

**Pregunta:** cuando Alice paga a Bob, ¿qué se consume, qué se crea y dónde queda la comisión?

**Punto de partida:** Alice tiene fondos maduros en el laboratorio de la sesión 1. Bob es otra wallet local. Comprobar red, altura y fondos antes de empezar; no basta con recordar el estado anterior.

**Lo que construirás:** una explicación calculada en Python de una transacción concreta. Debe poder seguirse hasta las salidas anteriores que gasta. Tú eliges cómo consultarla, organizar el código y mostrar el resultado.

## Predice antes de enviar

- Si Alice usa una salida de más valor que el pago, ¿qué esperas que ocurra con la diferencia?
- ¿Crees que hay una salida llamada «comisión»?
- ¿Esperas que Bob vea algo antes de generar un bloque?

## Experimento guiado

1. Registrar las salidas de Alice y las categorías de saldo de ambas wallets.
2. Obtener una dirección de Bob y elegir un pago inferior a los fondos disponibles, dejando margen para la comisión. No enviar todo el saldo.
3. Hacer un único envío con las herramientas del nodo. Entender qué decisiones está tomando la wallet por ti. Si necesita una tasa de comisión explícita, consultar su unidad y fijarla para este laboratorio.
4. Guardar el identificador real y observar la transacción decodificada. **No generar bloques todavía:** la sesión 3 continuará con este pago pendiente.
5. Para cada entrada, localizar la transacción previa y la salida exacta que está consumiendo. Obtener su importe de esos datos.
6. Recorrer las salidas nuevas. Identificar las que reconocen Alice y Bob usando sus wallets, sin asumir que la primera es el pago o la última el cambio.
7. Calcular la comisión a partir de las cantidades de entrada y salida. Contrastar el resultado con el dato que muestra la wallet emisora, entendiendo su signo.
8. Repetir la inspección desde tu código Python y explicar el recorrido con una tabla o un dibujo propio.

No hace falta construir o firmar manualmente la transacción todavía. Ahora importa observar qué hizo la wallet; más adelante tomaremos algunas de esas decisiones nosotros.

## Qué debe quedar claro

Una entrada identifica una salida anterior: no incluye necesariamente el importe que necesitas para calcular la comisión. Por eso se rastrean los datos previos.

El cambio es una salida nueva, no un resto que permanece dentro de la salida gastada. En nuestro laboratorio podemos consultar las wallets para identificarlo; en una transacción ajena no siempre puedes saber quién controla cada salida.

El criterio contable de este ejercicio es:

> Suma de importes de las salidas anteriores consumidas = suma de salidas nuevas + comisión.

Trabajamos con una transacción normal. La coinbase tiene un tratamiento distinto y no es un ejemplo para aplicar esta igualdad de la misma forma.

## Una variación sin gastar más

- Consultar la misma transacción desde Alice y Bob: ¿por qué sus datos de wallet pueden diferir aunque la transacción sea la misma?
- Cambiar el orden en que tu programa presenta las salidas. ¿Sigue identificando correctamente a sus destinatarios conocidos?

No hace falta otro envío para cerrar la sesión. Primero conservamos y entendemos este caso.

## Para cerrar

- Puedes señalar la salida previa de cada entrada y de dónde obtuviste su importe.
- La suma cuadra exactamente con unidades coherentes. No has usado el campo de comisión de la wallet como único cálculo.
- Puedes explicar qué automatizó la wallet y qué has comprobado tú.
- Distingues una salida observada de una atribución sobre quién la controla.

Guardar código, un extracto de los datos públicos de prueba y una [nota](plantilla-sesion.md) con el identificador del pago, altura y estado observado. No guardar archivos de wallet. Mantener el pago pendiente para la sesión 3.

<details>
<summary>Pistas de diagnóstico</summary>

- Un nodo regtest nuevo puede no tener historial para estimar comisiones. Revisa `help sendtoaddress`: una tasa explícita evita depender de esa estimación. No confundas sat/vB con BTC/kvB.
- `gettransaction` describe una transacción desde una wallet y puede facilitar su representación decodificada. Para un envío, el campo `fee` se expresa con signo negativo; tu diferencia entre entradas y salidas se expresa como coste positivo.
- Conservar las transacciones de financiación simplifica recuperar las salidas previas. Las consultas de wallet sirven para nuestras transacciones; `getrawtransaction` no garantiza encontrar cualquier transacción histórica sin índice o bloque indicado. No necesitas indexar toda la cadena para este ejercicio.
- No uses la desaparición de una salida de `listunspent` como prueba única de que el pago ya está confirmado. Eso se investiga en la sesión siguiente.

</details>

## Referencias

- [Datos desde la wallet: gettransaction](https://bitcoincore.org/en/doc/30.0.0/rpc/wallet/gettransaction/).
- [Estructura decodificada: decoderawtransaction](https://bitcoincore.org/en/doc/30.0.0/rpc/rawtransactions/decoderawtransaction/).
- [Envío y parámetros: sendtoaddress](https://bitcoincore.org/en/doc/30.0.0/rpc/wallet/sendtoaddress/).

Usa la ayuda instalada para los parámetros exactos. Estas referencias corresponden a Core 30.0.
