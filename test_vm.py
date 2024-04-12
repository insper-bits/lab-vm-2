#!/usr/bin/env python3

#!/usr/bin/env python3

from myhdl import bin
from bits import vm_test
import os.path

import pytest
import yaml

try:
    from telemetry import telemetryMark

    pytestmark = telemetryMark()
except ImportError as err:
    print("Telemetry não importado")


def source(name):
    dir = os.path.dirname(__file__)
    src_dir = os.path.join(dir, ".")
    return os.path.join(src_dir, name)


SP = 0
STACK = 256
TEMP = {0: 5, 1: 6, 2: 7, 3: 8, 4: 9, 5: 10, 6: 11, 7: 12}


def init_ram():
    ram = {0: STACK}
    return ram


@pytest.mark.telemetry_files(source("1a-add.vm"))
def test_1a_add():
    ram = init_ram()
    tst = {256: 123 + 23}
    assert vm_test("1a-add.vm", ram, tst)


@pytest.mark.telemetry_files(source("1b-calc.vm"))
def test_1b_calc():
    ram = init_ram()
    tst = {256: (14 + 2) - (123 - 1)}
    assert vm_test("1b-calc.vm", ram, tst)


@pytest.mark.telemetry_files(source("1c-loop.vm"))
def test_1c_loop():
    ram = init_ram()
    cnt = 0
    for i in range(55):
        cnt = cnt + 1

    tst = {SP: STACK, TEMP[3]: cnt}
    assert vm_test("1c-loop.vm", ram, tst)


@pytest.mark.telemetry_files(source("1d-div.vm"))
def test_1d_div_zero():
    ram = init_ram()
    a = 0
    b = 10
    ram[TEMP[0]] = a
    ram[TEMP[1]] = b
    tst = {SP: STACK, TEMP[3]: a / b}
    assert vm_test("1d-div.vm", ram, tst)


@pytest.mark.telemetry_files(source("1d-div.vm"))
def test_1d_div_noRest():
    ram = init_ram()
    a = 15
    b = 5
    ram[TEMP[0]] = a
    ram[TEMP[1]] = b
    tst = {SP: STACK, TEMP[3]: a / b}
    assert vm_test("1d-div.vm", ram, tst)


@pytest.mark.telemetry_files(source("1d-div.vm"))
def test_1d_div_rest():
    ram = init_ram()
    a = 15
    b = 7
    ram[TEMP[0]] = a
    ram[TEMP[1]] = b
    tst = {SP: STACK, TEMP[3]: a // b}
    assert vm_test("1d-div.vm", ram, tst)

@pytest.mark.telemetry_files(source("1e-mult.vm"))
def test_1e_mult():
    ram = init_ram()
    a = 2
    b = 2
    ram[TEMP[0]] = a
    ram[TEMP[1]] = b
    tst = {SP: STACK, TEMP[3]: a * b}
    assert vm_test("1e-mult.vm", ram, tst)


@pytest.mark.telemetry_files(source("2a-calculadora/mult.vm"))
def test_2a_calculadora():
    ram = init_ram()

    val = (14 + 2) * (8 - 1)
    tst = {SP: STACK, TEMP[1]: val}
    assert vm_test("2a-calculadora", ram, tst, 50000)


@pytest.mark.telemetry_files(source("2b-calculadora/div.vm"))
def test_2b_calculadora():
    ram = init_ram()

    val = 15 // 5
    tst = {SP: STACK, TEMP[1]: val}
    assert vm_test("2b-calculadora", ram, tst, 50000)


@pytest.mark.telemetry_files(source("2c-calculadora/pow.vm"))
def test_2c_calculadora():
    ram = init_ram()
    x = 2
    y = 1
    ram[TEMP[0]] = x
    ram[TEMP[1]] = y
    tst = {SP: STACK, TEMP[2]: x**y}
    assert vm_test("2c-calculadora", ram, tst, 500000)


@pytest.mark.telemetry_files(source("2c-calculadora/pow.vm"))
def test_2c_calculadora_zero():
    ram = init_ram()
    x = 5
    y = 0
    ram[TEMP[0]] = x
    ram[TEMP[1]] = y
    tst = {SP: STACK, TEMP[2]: x**y}
    assert vm_test("2c-calculadora", ram, tst, 100000)


@pytest.mark.telemetry_files(source("3a-lcd/circulo.vm"))
def test_3a_lcd():
    ram = init_ram()
    tst = {SP: STACK}
    assert vm_test("3a-lcd", ram, tst, 50000)
