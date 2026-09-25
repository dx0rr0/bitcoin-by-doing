# Sesión 1 — ¿Dónde están los bitcoins?

## Predicción
Crear una cartera o una dirección no debería darle bitcoins. Pensaba que el saldo se calcula sumando salidas no gastadas que pertenecen a la cartera.

## Lo que hice y observé
- Creé las carteras Alice y Bob en regtest.
- Miné 102 bloques con recompensas dirigidas a Alice.
- En la altura 102, Alice tenía 100 BTC en `trusted` y 5.000 BTC en `immature`; Bob tenía 0 BTC aunque había procesado el mismo bloque.
- `listunspent` mostró dos salidas maduras de Alice, de 50 BTC cada una.
- Mi programa sumó sus `amount` usando `Decimal` y obtuvo 100.00000000 BTC, igual que `getbalances.mine.trusted`.

## Mi explicación
Las salidas no pueden solo identificarse con txid porque una transacción puede tener varias salidas. Por eso se usa txid + vout. Solo 2 recompensas de Alice son gastables en este punto porque la norma es que tienen que haberse confirmado los bloques 100 veces para que su recompensa se pueda gastar. Alice ha minado 102 bloques, solo 2 de ellos se han confirmado al menos 100 veces y lo demás siguen apareciendo en 'immature'. Bob no ha minado ningún bloque ni ha recibido ninguna transacción, por tanto no tiene nada de BTC (poor bob).

## Siguiente paso
Usar los fondos de Alice para seguir un pago a Bob en la sesión 2.