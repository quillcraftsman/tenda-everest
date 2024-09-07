# TendaEverest

Python package to manage Tenda Everest router

You can find **Full Project Documentation** [here][documentation_path]

<hr>

#### Workflows
[![Tests](https://github.com/quillcraftsman/tenda-everest/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/quillcraftsman/tenda-everest/actions/workflows/run-tests.yml)
[![Pylint](https://github.com/quillcraftsman/tenda-everest/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/quillcraftsman/tenda-everest/actions/workflows/lint.yml)

#### Package
[![Version](https://img.shields.io/pypi/v/tenda-everest.svg)](https://pypi.python.org/pypi/tenda-everest/)
[![Development Status](https://img.shields.io/pypi/status/tenda-everest.svg)](https://pypi.python.org/pypi/tenda-everest)
[![Python version](https://img.shields.io/pypi/pyversions/tenda-everest.svg)](https://pypi.python.org/pypi/tenda-everest/)
[![License](https://img.shields.io/pypi/l/tenda-everest)](https://github.com/quillcraftsman/tenda-everestblob/main/LICENSE)
[![Wheel](https://img.shields.io/pypi/wheel/tenda-everest.svg)](https://pypi.python.org/pypi/tenda-everest/)

#### Support
[![Documentation](https://img.shields.io/badge/docs-0094FF.svg)][documentation_path]
[![Discussions](https://img.shields.io/badge/discussions-ff0068.svg)](https://github.com/quillcraftsman/tenda-everest/discussions/)
[![Issues](https://img.shields.io/badge/issues-11AE13.svg)](https://github.com/quillcraftsman/tenda-everest/issues/)

#### Downloads
[![Day Downloads](https://img.shields.io/pypi/dd/tenda-everest)](https://pepy.tech/project/tenda-everest)
[![Week Downloads](https://img.shields.io/pypi/dw/tenda-everest)](https://pepy.tech/project/tenda-everest)
[![Month Downloads](https://img.shields.io/pypi/dm/tenda-everest)](https://pepy.tech/project/tenda-everest)
[![All Downloads](https://img.shields.io/pepy/dt/tenda-everest)](https://pepy.tech/project/tenda-everest)

#### Languages
[![Languages](https://img.shields.io/github/languages/count/quillcraftsman/tenda-everest)](https://github.com/quillcraftsman/tenda-everest)
[![Top Language](https://img.shields.io/github/languages/top/quillcraftsman/tenda-everest)](https://github.com/quillcraftsman/tenda-everest)

#### Development
- [![Release date](https://img.shields.io/github/release-date/quillcraftsman/tenda-everest
)](https://github.com/quillcraftsman/tenda-everest/releases)
[![Last Commit](https://img.shields.io/github/last-commit/quillcraftsman/tenda-everest/main
)](https://github.com/quillcraftsman/tenda-everest)
- [![Issues](https://img.shields.io/github/issues/quillcraftsman/tenda-everest
)](https://github.com/quillcraftsman/tenda-everest/issues/)
[![Closed Issues](https://img.shields.io/github/issues-closed/quillcraftsman/tenda-everest
)](https://github.com/quillcraftsman/tenda-everest/issues/)
- [![Pull Requests](https://img.shields.io/github/issues-pr/quillcraftsman/tenda-everest
)](https://github.com/quillcraftsman/tenda-everest/pulls)
[![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed-raw/quillcraftsman/tenda-everest
)](https://github.com/quillcraftsman/tenda-everest/pulls)
- [![Discussions](https://img.shields.io/github/discussions/quillcraftsman/tenda-everest
)](https://github.com/quillcraftsman/tenda-everest/discussions/)

[//]: # (#### Repository Stats)

[//]: # ([![Stars]&#40;https://img.shields.io/github/stars/quillcraftsman/tenda-everest)

[//]: # (&#41;]&#40;https://github.com/quillcraftsman/tenda-everest&#41;)

[//]: # ([![Contributors]&#40;https://img.shields.io/github/contributors/quillcraftsman/tenda-everest)

[//]: # (&#41;]&#40;https://github.com/quillcraftsman/tenda-everestgraphs/contributors&#41;)

[//]: # ([![Forks]&#40;https://img.shields.io/github/forks/quillcraftsman/tenda-everest)

[//]: # (&#41;]&#40;https://github.com/quillcraftsman/tenda-everest&#41;)

<hr>

## Menu

- [Mission](#mission)
- [Open Source Project](#open-source-project)
- [Features](#features)
- [Requirements](#requirements)
- [Development Status](#development-status)
- [Install](#install)
- [Quickstart](#quickstart)
- [Contributing](#contributing)

## Mission

`tenda-everest` is python package to manage Tenda Everest router.
This package was tested on **EVEREST EWR-F303** Wireless Router with **Tenda** firmware **V02.03.01.125** 
(and similar). But this package may work on different routers with other firmwares.

![Everest ewr-f303 router picture](https://github.com/quillcraftsman/tenda-everest/blob/main/everest.jpeg)

## Open Source Project

This is the open source project with [MIT license](LICENSE). 
Be free to use, fork, clone and contribute.

## Features

- Connect to router by web interface (DONE)
- Get all information from router (like wi-fi settings, firmware, and all others) (DONE)
- Mange router (turn on wps, add port forwarding, ...) (PLAN)

## Requirements

- requests
- See more in [Full Documentation](https://tenda-everest.craftsman.lol/about.html#requirements)

## Development Status

- Package already available on [PyPi](https://pypi.org/project/tenda-everest/)
- See more in [Full Documentation](https://tenda-everest.craftsman.lol/about.html#development-status)

## Install

### with pip

```commandline
pip install tenda-everest
```

See more in [Full Documentation](https://tenda-everest.craftsman.lol/install.html)

## Quickstart

```python
from tenda_everest import info

print(info())
```

### More examples in [Full Documentation][documentation_path]

## Contributing

You are welcome! To easy start please check:
- [Full Documentation][documentation_path]
- [Contributing](CONTRIBUTING.md)
- [Developer Documentation](https://tenda-everest.craftsman.lol/dev_documentation.html)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Governance](GOVERNANCE.md)
- [Support](SUPPORT.md)

[documentation_path]: https://tenda-everest.craftsman.lol