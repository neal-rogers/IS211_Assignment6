#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program does stuff."""


def convertCelsiusToKelvin(temp_C):
    temp_K = temp_C + 273.15
    return float(temp_K)

def convertCelsiusToFahrenheit(temp_C):
    temp_F = temp_C * 1.8 + 32
    return float(temp_F)

def main():
    convertCelsiusToFahrenheit(50)


if __name__ == '__main__':
    main()