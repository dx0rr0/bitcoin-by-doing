from pathlib import Path
import os
import subprocess

repo = Path(__file__).resolve().parent

bitcoin_cli = (
    Path(os.environ["LOCALAPPDATA"])
    / "BitcoinCore"
    / "31.1"
    / "bitcoin-31.1"
    / "bin"
    / "bitcoin-cli.exe"
)
datadir = repo / ".local" / "bitcoin-regtest"

result = subprocess.run(
    [
        str(bitcoin_cli),
        "-regtest",
        f"-datadir={datadir}",
        "getblockchaininfo",
    ],
    capture_output=True,
    text=True,
    check=True,
)

print(result.stdout)