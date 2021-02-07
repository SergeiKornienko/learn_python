import ipaddress


def is_valid_ipv6(ip):
    items = ip.split('::')
    if len(items) > 1:
        result = []
        for item in items:
            result.extend(item.split(':'))
        if len(result) > 6:
            return False
    try:
        ipaddress.IPv6Address(ip)
    except ipaddress.AddressValueError:
        return False
    return True



