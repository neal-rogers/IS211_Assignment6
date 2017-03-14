#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program converts temperatures."""


def convertCelsiusToKelvin(temp_C):
    temp_K = float(temp_C + 273.15)
    return temp_K

def convertCelsiusToFahrenheit(temp_C):
    temp_F = float(temp_C * 1.8 + 32)
    return temp_F

def main():
    convertCelsiusToFahrenheit(50)


#if __name__ == '__main__':
    #main()