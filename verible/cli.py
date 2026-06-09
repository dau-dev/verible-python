from functools import lru_cache
from os import name
from pathlib import Path
from shutil import which
from subprocess import Popen
from sys import exit, stderr, stdout
from time import sleep


VERIBLE_TOOLS = [
    "verible-verilog-syntax",
    "verible-verilog-format",
    "verible-verilog-lint",
    "verible-verilog-kythe",
    "verible-verilog-ls",
    "verible-verilog-project",
    "verible-verilog-objdump",
]


@lru_cache(maxsize=1)
def _get_verible_tool(tool: str) -> str:
    exe = which(tool)
    if not exe:
        root = Path(__file__).parent.resolve()
        exe = str((root / "bin" / tool).resolve())
    return exe


def verible(tool: str, argv):
    build_cmd = [
        _get_verible_tool(tool),
        *argv,
    ]
    process = Popen(build_cmd, stderr=stderr, stdout=stdout)
    while process.poll() is None:
        sleep(0.1)
    if process.returncode != 0:
        exit(process.returncode)


def main():
    from sys import argv as _argv

    if len(_argv) < 2:
        print(f"Usage: verible-cli <tool> [args...]")
        print(f"Available tools: {', '.join(VERIBLE_TOOLS)}")
        exit(1)

    tool = _argv[1]
    if tool not in VERIBLE_TOOLS:
        print(f"Unknown tool: {tool}")
        print(f"Available tools: {', '.join(VERIBLE_TOOLS)}")
        exit(1)

    verible(tool, _argv[2:])
