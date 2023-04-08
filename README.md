# circuits [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Classic circuit output simulators in Python

## Author 

Eduardo Vasconcelos (vasconcedu) 

## Description

### Contents 

This repository contains a whole bunch of circuit output simulators. They're all in Python and I'll be coding them progressively.

Each simulator takes command line arguments and outputs either a `matplotlib` chart and/or text describing the circuit's behavior. 

So far, only the following one is available: 

- `rc-series/`
    - `rc-series.py`: simulates the output of an RC (series) circuit (both charging and discharging).

### Setup 

Use `requirements.txt` to install the required dependencies via `pip3`: 

```bash
pip3 install -r requirements.txt
```

Then navigate to the folder where the desired simulator is and run it using `python3`, e.g.:

```bash
cd rc-series/
python3 rc-series.py -h
```

### Help 

All simulators accept command line arguments. Help is always accessible via `-h` or `--help`. A more detailed description of each simulator may also be available as code comments.
