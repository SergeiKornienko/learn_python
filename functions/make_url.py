# BEGIN (write your solution here)
from urllib import parse


def make(url):
    return parse.urlparse(url)


def get_scheme(data):
    return data.scheme


def set_scheme(data, scheme):
    return data._replace(scheme=scheme)


def get_host(data):
    return data.hostname


def set_host(data, host):
    return data._replace(netloc=host)


def get_path(data):
    return data.path


def set_path(data, path):
    return data._replace(path=path)


def to_string(data):
    return parse.urlunparse(data)


def get_query_param(data, param_name, default=None):
    query = parse.parse_qs(data.query)
    if param_name in query.keys():
        return query[param_name][0]
    return default


def set_query_param(data, key, value):
    query = parse.parse_qs(data.query)
    if value is None:
        if key in query.keys():
            query.pop(key)
    else:
        query[key] = value
    query = parse.urlencode(query, doseq=True)
    return data._replace(query=query)
# END
