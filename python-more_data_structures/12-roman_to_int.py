#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    length = len(roman_string)

    for i in range(length):
        # Eger bu sonuncu herf deyilse ve bu herf sonrakindan kicikdirse
        if i < length - 1 and rom_n[roman_string[i]] < rom_n[roman_string[i + 1]]:
            result -= rom_n[roman_string[i]]
        else:
            result += rom_n[roman_string[i]]

    return result
