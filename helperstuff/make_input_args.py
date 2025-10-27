#!/usr/bin/env python3
import importlib.util
import os

YEAR = "2024"
OUTPUT_FILE = "input_args.txt"

def load_module_from_path(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

observables_path = "observables.py"
binning_path = "binning.py"

observables = load_module_from_path(observables_path, "observables")
binning = load_module_from_path(binning_path, "binning")

with open(OUTPUT_FILE, "w") as f:
    for var in observables.observables.keys():
        if var not in binning.BINS:
            print(f"Warning: {var} not defined in BINS, ommitting.")
            continue
        bins = binning.BINS[var]
        # Remover espacios por estética
        line = f"{var} {bins.strip()} {YEAR}\n"
        f.write(line)

print(f"File '{OUTPUT_FILE} created'.")
