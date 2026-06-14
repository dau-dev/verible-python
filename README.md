# verible

Python wrapping/binding for verible

[![Build Status](https://github.com/dau-dev/verible-python/actions/workflows/build.yaml/badge.svg?branch=main&event=push)](https://github.com/dau-dev/verible-python/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/dau-dev/verible-python/branch/main/graph/badge.svg)](https://codecov.io/gh/dau-dev/verible-python)
[![License](https://img.shields.io/github/license/dau-dev/verible-python)](https://github.com/dau-dev/verible-python)
[![PyPI](https://img.shields.io/pypi/v/verible.svg)](https://pypi.python.org/pypi/verible)

## Overview

<<<<<<< before updating
Wrapper of [verible](https://github.com/chipsalliance/verible), distributed via PyPI. Verible is a suite of SystemVerilog developer tools including a parser, formatter, linter, and language server.

```bash
# Format SystemVerilog files
verible-cli verible-verilog-format --inplace my_design.sv

# Lint SystemVerilog files
verible-cli verible-verilog-lint my_design.sv

# Syntax check
verible-cli verible-verilog-syntax my_design.sv

# Language server
verible-cli verible-verilog-ls
```

## Available Tools

- `verible-verilog-syntax` — SystemVerilog parser/syntax checker
- `verible-verilog-format` — SystemVerilog formatter
- `verible-verilog-lint` — SystemVerilog linter
- `verible-verilog-kythe` — Kythe indexing for SystemVerilog
- `verible-verilog-ls` — Language server
- `verible-verilog-project` — Project tool
- `verible-verilog-objdump` — Pretty-printer

## License

This software is licensed under the Apache 2.0 license. See the [LICENSE](LICENSE) file for details.

Verible is Copyright 2019-2024 Google LLC, licensed under the Apache 2.0 license.

> [!NOTE]
> This library was generated using [copier](https://copier.readthedocs.io/en/stable/) from the [Base Python Project Template repository](https://github.com/python-project-templates/base).
