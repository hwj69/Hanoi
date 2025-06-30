import subprocess
import sys

import pytest

import importlib.util
import pathlib

spec = importlib.util.spec_from_file_location(
    "hanoi", pathlib.Path(__file__).resolve().parent.parent / "hanoi.py"
)
hanoi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hanoi)


def test_hanoi_valid_moves():
    moves = hanoi.hanoi(2)
    assert moves == [('A', 'B'), ('A', 'C'), ('B', 'C')]


def test_hanoi_zero_raises():
    with pytest.raises(ValueError):
        hanoi.hanoi(0)


def test_hanoi_negative_raises():
    with pytest.raises(ValueError):
        hanoi.hanoi(-1)


def run_cli(arg):
    return subprocess.run([sys.executable, 'hanoi.py', str(arg)], capture_output=True, text=True)


def test_cli_invalid():
    result = run_cli(0)
    assert result.returncode == 1
    assert "Error:" in result.stdout


def test_cli_valid():
    result = run_cli(2)
    assert result.returncode == 0
    assert "Move 3" in result.stdout

