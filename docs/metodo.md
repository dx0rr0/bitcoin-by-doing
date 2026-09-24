# Cómo trabajaremos

[Recorrido](README.md)

Tú escribes el código y decides cómo organizarlo. El tutor ayuda a elegir un experimento, entender los datos y salir de los bloqueos. Si aparece una necesidad de reutilización, decidimos entonces qué merece una función o un módulo.

## Una sesión

1. **Retomar.** Mirar la última nota y comprobar el estado del nodo. Nada de asumir que el laboratorio está como ayer.
2. **Predecir.** Escribir dos o tres frases sobre lo que esperas observar. Equivocarse aquí es útil.
3. **Entender lo necesario.** Una explicación breve, una salida real o un dibujo. La teoría adicional queda a un clic, no como requisito previo.
4. **Experimentar.** Elegir qué consultar o cambiar y hacerlo en pasos pequeños. Primero entender un caso; después automatizarlo en Python.
5. **Variar.** Cambiar una condición y predecir el efecto antes de ejecutarlo.
6. **Explicar.** Contar qué pasó, qué dato lo demuestra y qué sigue abierto. Elegir juntos la siguiente acción.

## Ayuda gradual

Si te atascas, el tutor empieza por una pregunta sobre el dato o supuesto que falta. Después puede dar una pista conceptual, señalar una parte de la documentación o nombrar una operación. Un ejemplo mínimo llega cuando esas pistas no bastan o cuando lo pidas.

No hay que sufrir con la instalación ni memorizar parámetros de RPC. Consultar documentación es parte normal del trabajo. La ayuda con una ruta de Windows no debería resolver también el ejercicio de Bitcoin.

Los desplegables de las sesiones contienen pistas de diagnóstico, no implementaciones. Puedes ignorarlos hasta necesitarlos.

## Qué comparten los experimentos

- Un nodo en regtest, estado local separado y versiones registradas en la sesión 0.
- Cantidades con unidades explícitas: BTC, satoshis, bytes o vbytes según corresponda. Elegir una representación exacta para el dinero.
- Una predicción previa, observaciones reales y una comprobación independiente cuando sea posible.
- Código creado por el alumno en `experiments/`. No hay nombres de funciones, formato de salida o framework obligatorio.
- Una nota breve en `notes/`, usando la [plantilla](plantilla-sesion.md) si ayuda. Publicar solo extractos de laboratorio sin credenciales.

Las sesiones 1–3 mantienen el mismo laboratorio. Reiniciarlo no equivale a vaciarlo: el nodo debe conservar su estado. Para repetir desde cero se utilizará otro directorio de datos y se anotará el cambio.

## Cómo sabemos si podemos avanzar

La guía de cada sesión propone comprobaciones. No se aplican como casillas automáticas: tú explicas una salida real y respondes a una variante. Si algo solo sale al copiar una secuencia, hacemos otro ejemplo más pequeño.

Las sesiones distinguen **ejecución observada** de **concepto explicado** en [progreso](progreso.md). Las dudas pueden quedar abiertas y retomarse cuando tengan más contexto.

## Cómo pedir una sesión al tutor

> Quiero trabajar la sesión 0 de este repositorio. Lee AGENTS.md y mi progreso. Guíame paso a paso: déjame tomar decisiones y ejecutar. No hagas el recorrido completo ni me des las interfaces del código.

Para sesiones posteriores, cambia el número y añade qué probaste o qué error obtuviste. No hace falta pegar el historial entero si las notas registran el estado.
