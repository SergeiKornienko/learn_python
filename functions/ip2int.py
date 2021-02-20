def ip2int(adress):
    hosts = list(map(int, adress.split('.')))
    return hosts[3] + 256 * (hosts[2] + 256 * (hosts[1] + 256 * hosts[0]))


def int2ip(number):
    quot3, rem3 = divmod(number, 256)
    quot2, rem2 = divmod(quot3, 256)
    quot1, rem1 = divmod(quot2, 256)
    return '.'.join(list(map(str, [quot1, rem1, rem2, rem3])))
