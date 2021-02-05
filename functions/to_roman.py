NUMERALS = {  # noqa: WPS407
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}


# BEGIN (write your solution here)
def to_roman(num):
    values = list(NUMERALS.values())
    keys = list(NUMERALS.keys())
    arab_num = num
    rom_num = ''
    for (index, v) in enumerate(values):
        if arab_num // v >= 1:
            rom_num = rom_num + keys[index] * (arab_num // v)
            arab_num = arab_num - v * (arab_num // v)
    return rom_num


def to_arabic(num):
    values = list(NUMERALS.values())
    keys = list(NUMERALS.keys())
    rom_num = num
    arab_num = 0
    for (index, k) in enumerate(keys):
        i = 0
        while rom_num.startswith(k) and i < 3:
            i += 1
            rom_num = rom_num.replace(k, '', 1)
        arab_num = arab_num + values[index] * i
    return arab_num if rom_num == '' else False
# END
