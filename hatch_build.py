from os import environ
from pathlib import Path
from sys import platform
from platform import machine
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomHook(BuildHookInterface):
    def initialize(self, version, build_data):
        build_data["pure_python"] = False
        arch = environ.get("AUDITWHEEL_ARCH", machine())
        if "darwin" in platform:
            if "arm" in arch:
                build_data["tag"] = "py3-none-macosx_11_0_arm64"
            else:
                build_data["tag"] = "py3-none-macosx_11_0_x86_64"
        elif "linux" in platform:
            if "arm" in arch or "aarch" in arch:
                build_data["tag"] = "py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64"
            else:
                build_data["tag"] = "py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64"
        else:
            build_data["tag"] = "py3-none-win_amd64"

        # Include native verible binaries as scripts so they land in $PREFIX/bin
        bins_dir = Path(self.root) / "verible" / "bin"
        if bins_dir.is_dir():
            shared = build_data.setdefault("shared_data", {})
            for f in bins_dir.iterdir():
                if f.is_file():
                    shared[str(f.relative_to(self.root))] = f"scripts/{f.name}"
