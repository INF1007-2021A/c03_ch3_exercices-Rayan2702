#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    result = (a + b + c) / 3
    return result



def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_rad = (3.14159265358979323846264338/180)*angle_degs , (angle_mins * 3.14159265)/(60 * 180) , (angle_secs * 3.14159265)/(180 * 3600)

    return angle_rad


def to_degrees(angle_rads: float) -> tuple:

    angle_degs = (angle_rads * 180 / 3.1415926536)
    angle_mins = (angle_rads * (60 * 180)/3.1415926536)
    angle_secs = (angle_rads * (3600 * 180)/3.1415926536)
    return angle_degs , angle_mins, angle_secs


def to_celsius(temperature: float) -> float:
    temperature_far = (temperature - 32) * (5/9)
    return temperature_far


def to_farenheit(temperature: float) -> float:
    temperature_cel = (temperature * (9/5)) + 32
    return temperature_cel


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.3, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()

