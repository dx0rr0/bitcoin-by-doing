# Recorrido y profundidad

[Inicio](../README.md) · [Método](metodo.md) · [Progreso](progreso.md)

El objetivo es poder seguir un pago, explicar las reglas relevantes y diseñar experimentos para comprobarlas. Las matemáticas de las curvas elípticas no son un requisito de entrada.

## Mapa de sesiones

| Bloque | Sesión | Pregunta | Resultado que buscaremos |
| --- | --- | --- | --- |
| Preparación | [0. Empezar juntos](00-empezar-juntos.md) | ¿Qué necesito para experimentar? | Entorno elegido y comprobado, arranque y parada entendidos, primera consulta de lectura. |
| Observar | [1. Dónde están los bitcoins](01-donde-estan-los-bitcoins.md) | ¿De dónde sale el saldo? | Inventario propio de UTXO y explicación de las categorías del saldo. |
| Observar | [2. Seguir un pago](02-seguir-un-pago.md) | ¿Qué se consume y qué se crea? | Reconstrucción de una transacción y su comisión a partir de sus datos. |
| Observar | [3. De pendiente a confirmado](03-de-pendiente-a-confirmado.md) | ¿Qué cambia al entrar en un bloque? | Registro antes/después y seguimiento desde Python. |
| Poner a prueba | 4. Gastos en conflicto | ¿Qué impide gastar dos veces? | Experimento con dos gastos del mismo UTXO; separar política de mempool y reglas de consenso. |
| Poner a prueba | 5. Firmas y condiciones de gasto | ¿Qué autoriza una firma? | Firmar usando herramientas existentes y observar una modificación que invalida la autorización. Script y witness a nivel funcional. |
| Implementar | 6. Bytes y transacciones | ¿Qué viaja por la red? | Parser propio para un formato acotado; comparación con Core. Límites explícitos respecto a SegWit y otros formatos. |
| Implementar | 7. Cabeceras y trabajo | ¿Qué significa minar? | Parsear una cabecera y verificar su hash frente al objetivo. Experimento sencillo de búsqueda de nonce. |
| Conectar | 8. Nodos y ramas | ¿Cómo convergen historias distintas? | Dos nodos regtest, ramas controladas y observación de una reorganización según trabajo acumulado. |

Las sesiones 0–3 están desarrolladas. Las sesiones 4–8 son objetivos de trabajo; sus guías se prepararán a partir de las dudas que aparezcan. No hay enlaces a lecciones que todavía no existen.

## Qué profundidad tendrá

Al terminar el recorrido buscaremos que puedas:

- Explicar wallet, clave, dirección, UTXO, transacción, mempool, bloque y nodo sin tratarlos como equivalentes.
- Consultar y controlar nodos locales desde Python, leer errores y repetir un experimento.
- Seguir los importes de una transacción hasta las salidas anteriores que gasta.
- Entender para qué sirven firmas, condiciones de gasto y hashes, usando implementaciones existentes para la criptografía.
- Implementar algunas piezas pequeñas de serialización y verificación, declarando qué formatos soportan.
- Distinguir reglas de consenso, política de un nodo y decisiones de una wallet.
- Leer un test funcional sencillo y proponer una variación que compruebe un comportamiento.

La demostración matemática de la seguridad criptográfica, una implementación completa de consenso, Taproot en profundidad, Lightning, privacidad avanzada y seguridad de wallets quedan fuera de estas ocho sesiones. Se pueden añadir después como recorridos separados.

## Ritmo y cierre

Una sesión es una unidad de aprendizaje, no una obligación de terminar en una tarde. Reservar 60–90 minutos sirve para empezar; instalación, depuración o curiosidad pueden alargarla. Se puede partir una sesión en varios encuentros.

Para avanzar hacen falta una observación reproducible y una explicación propia. Terminar de leer un archivo o ver que un script funciona no basta. El [método compartido](metodo.md) concreta cómo comprobarlo sin convertirlo en un examen.

Después habrá un [puente a open source](hacia-open-source.md): aprender a compilar y probar un repositorio real, leer su código y aportar una reproducción o un test pequeño. Completar el taller no garantiza que una contribución sea aceptada.
