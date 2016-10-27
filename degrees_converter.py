#!/usr/bin/env python3

"""A simple script for converting between Decimal Degrees and Degrees Minutes Seconds, and vice versa."""

__author__ = "Patrick Guelcher"
__copyright__ = "(C) 2016 Patrick Guelcher"
__license__ = "MIT"
__version__ = "1.0"

def main():
    convert_from = input("Please input what you are converting from (DD or DMS): ")

    #Convert from Decimal Degrees (DD)
    if convert_from.upper() == "DD":
        user_entry = input("Enter the DD (XX.XXXX): ")
        dd = [int(i) for i in user_entry.split(".") ]

        decimal = "0." + str(dd[1]) #Convert the second number back into a decimal number
        d = int(dd[0])
        m = int((float(user_entry) - d) * 60)
        s = round((float(user_entry) - d - (int(m)/60)) * 3600, 2)

        print("The Degrees Minutes Seconds are: " + str(d) + "° " + str(abs(m)) + "' " + str(abs(s)) + "\"")

    #Convert from Degrees Minutes Seconds (DMS)
    if convert_from.upper() == "DMS":
        user_entry = input("Enter the DMS (XX XX XX): ")
        dms = [int(i) for i in user_entry.split(" ") ]

        d = dms[0]
        m = abs(dms[1]/60)
        s = abs(dms[2]/3600)
        new_decimal = m + s

        print("The Decimal Degrees are: " + str(d) + str(new_decimal)[1:])

    #Restart if not DD or DMS
    if convert_from.upper() != "DD" and convert_from.upper() != "DMS":
        print("Invalid entry. Please try again.")
        main()

if __name__ == "__main__":
    main()
