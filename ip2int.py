# Реализуйте и экспортируйте функции ip2int и int2ip,
# которые преобразовывают представление IP-адреса
# из десятичного формата с точками в 32-битное
# число в десятичной форме и обратно.
#
# Функция ip2int принимает на вход строку и должна
# возвращать число. А функция int2ip наоборот:
# принимает на вход число, а возвращает строку.
#
# Примеры
# >>> ip2int('128.32.10.1')
# 2149583361
# >>> ip2int('0.0.0.0')
# 0
# >>> ip2int('255.255.255.255')
# 4294967295
# >>>
# >>> int2ip(2149583361)
# '128.32.10.1'
# >>> int2ip(0)
# '0.0.0.0'
# >>> int2ip(4294967295)
# '255.255.255.255'
def ip2int(adress):
    hosts = list(map(int, adress.split('.')))
    return hosts[3] + 256 * (hosts[2] + 256 * (hosts[1] + 256 * hosts[0]))


def int2ip(number):
    quot3, rem3 = divmod(number, 256)
    quot2, rem2 = divmod(quot3, 256)
    quot1, rem1 = divmod(quot2, 256)
    return '.'.join(list(map(str, [quot1, rem1, rem2, rem3])))


if __name__ == '__main__':
    ZEROES = '0.0.0.0'  # noqa: S104
    assert ip2int(ZEROES) == 0
    assert ip2int('128.32.10.1') == 2149583361
    assert int2ip(0) == ZEROES
    assert int2ip(2149583361) == '128.32.10.1'
    assert int2ip(ip2int('192.168.1.32')) == '192.168.1.32'
    assert ip2int(int2ip(2149583361)) == 2149583361
