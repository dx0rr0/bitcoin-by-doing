# Sesión 0 · Preparar el entorno juntos

[Recorrido](README.md) · [Método](metodo.md) · [Siguiente: sesión 1](01-donde-estan-los-bitcoins.md)

**Pregunta:** ¿qué necesito para experimentar con Bitcoin y cómo sé qué está ejecutándose?

Esta sesión se hace conversando con el tutor. El documento es una agenda, no una secuencia de instalación que debas adivinar. Al terminar tendrás un nodo local de pruebas y sabrás consultarlo, pararlo y volverlo a arrancar.

## Antes de instalar

Cuenta qué has llegado a hacer con *Programming Bitcoin*, qué te resulta familiar y dónde te perdiste. Después revisamos el entorno actual:

- Sistema operativo y terminal que quieres usar.
- Python y Git disponibles; versión y forma de ejecutarlos.
- Si ya tienes Bitcoin Core, Docker o WSL, y si los usas con comodidad.
- Dónde guardarás el repositorio y el estado del laboratorio.

No hace falta dominar Docker ni aprender Linux a la vez. Si trabajas en Windows, decidimos entre binarios nativos, WSL o contenedor según lo que tengas. Elegimos una sola ruta y escribimos las instrucciones reales después de comprobarla.

## Decisiones que tomaremos

| Decisión | Qué queremos resolver |
| --- | --- |
| Instalación | Obtener Bitcoin Core de su distribución oficial y comprobarla siguiendo sus instrucciones. Registrar la versión elegida. |
| Red | Usar regtest y poder demostrarlo consultando al nodo. |
| Datos | Usar un directorio exclusivo dentro de `.local/`, fuera de Git y separado de cualquier instalación personal. |
| Acceso | Mantener RPC local. Entender cómo se autentica la consulta sin copiar credenciales al código o a las notas. |
| Python | Elegir entorno y dependencias solo si hacen falta. Un proceso de terminal o una petición RPC son posibilidades; no hay un cliente prediseñado. |
| Organización | Elegir juntos dónde irá el primer experimento y cómo ejecutarlo. Sin diseñar ahora todas las sesiones. |

El tutor puede resolver problemas de instalación y explicar los comandos. Antes de una operación, tú debes saber qué componente cambia y cómo comprobar su resultado.

## Primer experimento

1. Arrancar el nodo con la configuración acordada.
2. Consultar su red y altura de cadena. Guardar solo los campos que entiendes y necesitas.
3. Identificar qué proceso responde y qué archivo o configuración ha determinado la red.
4. Hacer desde Python una consulta de lectura al mismo nodo. Decide cómo, con ayuda si la conexión se atasca.
5. Parar el nodo de forma ordenada e intentar consultar otra vez. Distinguir un fallo de conexión de un error devuelto por Bitcoin Core.
6. Volver a arrancarlo con el mismo directorio de datos y comprobar que responde.

Todavía no creamos un cliente genérico ni añadimos reintentos, clases o una API propia. La primera consulta puede ser un archivo muy pequeño.

## Explicación que buscamos

- ¿Qué diferencias hay entre Bitcoin Core, la herramienta de terminal, tu script y una wallet?
- ¿Por qué este nodo no necesita descargar la cadena pública?
- ¿Qué dato demuestra que estás en regtest?
- ¿Qué conserva el directorio de datos y qué perderías si lo borrases?
- ¿Qué cambiarías para repetir el laboratorio desde cero conservando el anterior?

No necesitas responder todas antes de empezar. Las resolvemos viendo los componentes en funcionamiento.

## Qué queda registrado

Una nota con versiones, ruta de instalación, ruta del estado local, forma comprobada de arrancar y parar y siguiente paso. Sustituye rutas personales por marcadores antes de publicar la nota si no quieres compartirlas. No incluyas cookies, contraseñas o archivos de wallet.

El código de la consulta lo escribes tú. Si el tutor tuvo que escribir una parte incidental, anota cuál y qué entiendes de ella.

**Para cerrar:** puedes volver a arrancar el nodo, demostrar la red y consultar desde Python sin que el tutor repita toda la secuencia por ti. El registro inicial del taller está pendiente hasta que hagas estas comprobaciones.

## Referencias para consultar juntos

- [Descarga oficial de Bitcoin Core](https://bitcoincore.org/en/download/).
- [Qué permite regtest](https://developer.bitcoin.org/examples/testing.html#regtest-mode). La página contiene ejemplos antiguos: los parámetros se contrastan con la ayuda instalada.
- [Información de la cadena, Core 30.0](https://bitcoincore.org/en/doc/30.0.0/rpc/blockchain/getblockchaininfo/).
- [Criterio para versiones y referencias](recursos.md).
