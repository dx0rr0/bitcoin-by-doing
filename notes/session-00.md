# Sesión 0 — Entorno y primer nodo regtest

Fecha: 2026-09-25

## Entorno

- Windows, terminal PowerShell integrada en VS Code.
- Python usado por uv: 3.13.11.
- uv: 0.12.19.
- Git: 2.52.0.windows.1.
- Bitcoin Core: v31.1.0.
- Binarios de Bitcoin Core: %LOCALAPPDATA%\BitcoinCore\31.1\bitcoin-31.1\bin.
- Directorio de datos del laboratorio: .local\bitcoin-regtest, dentro del repo y excluido de Git.

## Predicción inicial

Pensé que llegarían transacciones y que después podría aprobar bloques. La consulta getblockchaininfo no comprobó directamente si habían llegado transacciones.

## Qué hice y observé

- Verifiqué el ZIP de Bitcoin Core comparando su SHA256 con SHA256SUMS.
- La firma de Michael Ford (fanquake) sobre SHA256SUMS.asc dio Good signature y su huella coincidió con la publicada. Las firmas de otros participantes no se comprobaron porque sus claves no estaban importadas.
- Arranqué bitcoind.exe con -regtest y el directorio de datos del laboratorio.
- bitcoin-cli.exe getblockchaininfo devolvió chain=regtest, blocks=0, headers=0 y bestblockhash=0f9188f13cb7b2c71f2a335e3a4fc328bf5beb436012afca590b1a11466e2206.
- Ejecuté uv run .\main.py. El script usa subprocess para invocar bitcoin-cli y mostró la misma respuesta.
- Al detener el nodo con bitcoin-cli stop, una nueva consulta no pudo conectar. Después de reiniciarlo con el mismo directorio de datos, chain, blocks y bestblockhash conservaron sus valores.
- Durante la sesión entendí que bitcoin-cli envía la consulta y bitcoind responde; blocks indica la altura actual y bestblockhash es el hash del bloque en esa altura.

## Ayuda y preguntas abiertas

- El tutor proporcionó el ejemplo inicial de subprocess en main.py.
- Queda por explorar cómo observar transacciones y producir bloques en regtest.

## Estado y siguiente paso

- La consulta Python, la parada y el reinicio del nodo se observaron correctamente.
- Siguiente paso: continuar con la sesión 1 usando el nodo regtest existente.
