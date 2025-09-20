import argparse
import importlib.util
import inspect
import sys
from ast import literal_eval
from itertools import batched, islice
from pathlib import Path
from types import ModuleType


def interactive_mode(lines: list[str], module: ModuleType) -> None:
    for ops, args in batched(map(literal_eval, lines), 2):
        class_name = ops[0]
        cls = getattr(module, class_name, None)
        if cls is None or not inspect.isclass(cls):
            raise ImportError(f"No class named '{class_name}' found.")
        obj = cls(*args[0])
        for op, arg in islice(zip(ops, args), 1, None):
            if not hasattr(obj, op):
                raise AttributeError(f"'{class_name}' object has no attribute '{op}'")
            method = getattr(obj, op)
            if not callable(method):
                raise TypeError(f"'{op}' is not callable")
            print(method(*arg))
        print()


def normal_mode(lines: list[str], module: ModuleType) -> None:
    solution_class = getattr(module, "Solution", None)
    if not solution_class or not inspect.isclass(solution_class):
        raise ImportError(f"No class named 'Solution' found.")
    invoke_solution_method(lines, solution_class)


def invoke_solution_method(lines: list[str], solution_class: type) -> None:
    members = inspect.getmembers(solution_class, predicate=inspect.isfunction)
    for name, method in members:
        if name.startswith("_"):
            continue
        if not (parameters := list(inspect.signature(method).parameters.items())[1:]):
            continue
        if len(lines) % len(parameters) != 0:
            continue
        for arg_strs in batched(lines, len(parameters)):
            args = []
            for (name, param), arg_str in zip(parameters, arg_strs):
                print(f"{name}={arg_str[:100]}")
                args.append(literal_eval(arg_str))  # TODO: check type
            print(method(solution_class(), *args))  # TODO: check return type
            print()
        return
    raise ValueError("No suitable method found in the solution class.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run LeetCode Python code.")
    parser.add_argument("file", type=Path, help="Path to the Python file to run")
    parser.add_argument("input_file", type=Path, help="Optional input file to read input from")
    parser.add_argument("--interactive", action="store_true", help="Interactive problem")
    args = parser.parse_args()

    file: Path = args.file.resolve()
    input_file: Path = args.input_file.resolve()

    if file.suffix.lower() != ".py" or not file.is_file():
        raise FileNotFoundError(f"{file} is not a valid Python file.")
    if not input_file.is_file():
        raise FileNotFoundError(f"{input_file} is not a valid input file.")

    lines = list(map(str.strip, input_file.read_text(encoding="utf-8").strip().splitlines()))
    if not lines:
        raise ValueError(f"No input found in {input_file}.")

    # from file import Solution
    module_name = file.stem
    spec = importlib.util.spec_from_file_location(module_name, str(file))
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    if args.interactive:
        interactive_mode(lines, module)
    else:
        normal_mode(lines, module)


if __name__ == "__main__":
    main()
