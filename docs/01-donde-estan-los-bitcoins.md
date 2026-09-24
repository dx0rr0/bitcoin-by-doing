# Sesión 1 · ¿Dónde están los bitcoins?

[Anterior: sesión 0](00-empezar-juntos.md) · [Recorrido](README.md) · [Siguiente: sesión 2](02-seguir-un-pago.md)

**Pregunta:** cuando una wallet muestra un saldo, ¿qué datos permiten calcularlo?

**Punto de partida:** nodo regtest de la sesión 0, consulta desde Python funcionando y estado local conservado. No se presupone que haya wallets ni fondos.

**Lo que construirás:** una forma propia de listar las salidas disponibles de una wallet y calcular un total que puedas contrastar. Tú eliges el código y cómo presentar los datos.

## Predice antes de consultar

1. Si creas una wallet y después varias direcciones, ¿aparecerá algún bitcoin?
2. ¿Una wallet y una dirección representan lo mismo?
3. ¿Crees que el saldo es un número almacenado que aumenta y disminuye, o que puede reconstruirse a partir de otros datos?

Guarda tu respuesta inicial aunque luego cambie.

## Experimento guiado

1. Crear dos wallets de laboratorio, Alice y Bob, con ayuda de la documentación del nodo. Confirmar que las consultas van a la wallet que quieres observar.
2. Obtener direcciones y mirar el estado inicial. Conservar una observación antes de generar fondos.
3. Generar un bloque regtest con recompensa para Alice y observar las categorías del saldo.
4. Averiguar por qué ver una recompensa no implica poder gastarla inmediatamente. Generar los bloques necesarios y contrastar las categorías otra vez.
5. Identificar las salidas que la wallet ofrece como disponibles. Elegir una y describir los campos que permiten distinguirla de cualquier otra salida.
6. Decidir qué conjunto de salidas va a sumar tu programa: confirmaciones, posibilidad de gasto y otros filtros deben quedar claros.
7. Escribir el cálculo en Python y compararlo con una consulta de Bitcoin Core que mida lo mismo. Si los totales difieren, investigar el conjunto incluido antes de cambiar la aritmética.

Para este primer caso, el tutor ayudará a mantener wallets sencillas con claves locales de prueba. Watch-only, multifirma y fondos externos quedan para más adelante.

## Un poco de vocabulario, después de observar

Una **salida** fija una cantidad y unas condiciones de gasto. Una transacción posterior puede consumirla. Llamamos **UTXO** a una salida de transacción que sigue sin gastarse.

La wallet conoce claves, descriptores y transacciones relevantes para ella. Su saldo depende de qué salidas considera propias y de sus reglas para incluirlas. La lista de una wallet no es el conjunto de UTXO de toda la red.

La **coinbase** es la transacción especial que crea la recompensa de un bloque; aquí no nos referimos a una empresa. Tiene una regla de madurez. Su excepción no debe hacerte concluir que todos los pagos requieren esa espera.

## Una variación

Elige con el tutor una comprobación pequeña:

- Pedir otra dirección de Alice y predecir el efecto sobre el saldo.
- Comparar Alice y Bob y justificar la diferencia con salidas concretas.
- Cambiar el filtro de confirmaciones y explicar el nuevo total.

## Para cerrar

Usando la salida de tu propio programa, deberías poder:

- Identificar una salida por su transacción y posición dentro de ella.
- Explicar qué sumaste, en qué unidades y qué excluiste.
- Distinguir recompensa inmadura, fondos disponibles y saldo de otra wallet.
- Dibujar una wallet con varias direcciones y varias salidas, sin representarla como una única cuenta bancaria.

Guardar el código y una [nota breve](plantilla-sesion.md). Dejar el laboratorio intacto: Alice tendrá fondos para la sesión 2. Anotar altura, wallets utilizadas y filtros, sin exportar sus claves.

<details>
<summary>Pistas si te atascas</summary>

- La ayuda de RPC se puede buscar por wallet y por operaciones. `listunspent` y `getbalances` responden preguntas relacionadas, pero no siempre suman el mismo conjunto.
- Consulta la wallet explícitamente si tienes más de una cargada.
- Para arrancar desde una cadena nueva, generar 101 bloques es una receta habitual para disponer de recompensa madura en la wallet. Observa también cuántas recompensas siguen inmaduras; no extrapoles esta espera a un pago normal.
- Un listado vacío puede deberse a filtros o madurez. No demuestra por sí solo que la wallet haya perdido información.
- Evita convertir primero las cantidades a `float` y corregir el error después. Investiga una representación exacta desde que lees el dato.

</details>

## Referencias

- [Salidas de una wallet: listunspent](https://bitcoincore.org/en/doc/30.0.0/rpc/wallet/listunspent/).
- [Categorías de saldo: getbalances](https://bitcoincore.org/en/doc/30.0.0/rpc/wallet/getbalances/).
- [Recompensas y preparación de regtest](https://developer.bitcoin.org/examples/testing.html#regtest-mode).

Los nombres de RPC son referencias, no una interfaz impuesta para tu programa. Contrasta sus opciones con la ayuda de la versión instalada.
