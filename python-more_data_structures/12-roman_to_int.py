#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0

    for i, ch in enumerate(roman_string):
        if i > 0 and rom_n[ch] > rom_n[roman_string[i - 1]]:
            num += rom_n[ch] - 2 * rom_n[roman_string[i - 1]]
        else:
            num += rom_n[ch]

    return num
