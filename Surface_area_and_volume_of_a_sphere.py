#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 6th Oct, 2026
# This program asks the radius of a sphere in cm
# it then calculates the Surface Area and Volume of the
# sphere and displays the results to the user with proper units.
import math


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the sphere (cm): "))

    # calculate the surface area and volume of a sphere
    surface_area = 4 * math.pi * radius**2
    volume = (4 / 3) * math.pi * radius**3

    # display the surface area and volume to the user with proper units
    print("The surface area is: {:.2f}cm²".format(surface_area))
    print("The volume is: {:.2f}cm³".format(volume))


if __name__ == "__main__":
    main()
