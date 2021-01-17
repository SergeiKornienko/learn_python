# Реализуйте абстракцию для работы с URL. Она должна
# извлекать и менять части адреса.
#
# Интерфейс:
#
    # make(url) - Конструктор. Создает URL.
    # get_scheme(data) - Селектор (геттер). Извлекает схему.
    # set_scheme(data, scheme) - Сеттер. Меняет схему.
    # get_host(data) - Геттер. Извлекает host.
    # set_host(data, host) - Сеттер. Меняет host.
    # get_path(data) - Геттер. Извлекает путь.
    # set_path(data, path) - Сеттер. Меняет путь.
    # get_query_param(data, param_name, default=None) - Геттер.
    # Извлекает значение для параметра запроса. Третьим параметром
    # функция принимает значение по умолчанию, которое возвращается
    # тогда, когда в запросе не было такого параметра
    # set_query_param(data, key, value) - Сеттер. Устанавливает
    # значение для параметра запроса. Если передано значение None,
    # то параметр отбрасывается.
    # to_string(data) - Геттер. Преобразует URL в строковой вид.
# Все сеттеры должны возвращать новый изменённый URL, а старый
# оставлять неизменным.
#
# Примеры
# >>> import url
# >>> u = url.make('https://hexlet.io/community?q=low')
# >>>
# >>> u = url.set_scheme(u, 'http')
# >>> url.to_string(u)
# 'http://hexlet.io/community?q=low'
# >>>
# >>> u = url.set_path(u, '/404')
# >>> url.to_string(u)
# 'http://hexlet.io/404?q=low'
# >>>
# >>> url.get_query_param(u, 'q')
# 'low'
# >>>
# >>> u = url.set_query_param(u, 'page', 5)
# >>> url.to_string(u)
# 'http://hexlet.io/404?q=low&page=5'
# >>>
# >>> u = url.set_query_param(u, 'q', 'high')
# >>> url.to_string(u)
# 'http://hexlet.io/404?q=high&page=5'
# >>>
# >>> u = url.set_query_param(u, 'q', None)
# >>> url.to_string(u)
# 'http://hexlet.io/404?page=5'


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


if __name__ == '__main__':
    u = make('https://domain.org/community?q=low')
    assert to_string(u) == 'https://domain.org/community?q=low'
    u = set_host(u, 'hexlet.io')
    assert get_host(u) == 'hexlet.io'
    assert to_string(u) == 'https://hexlet.io/community?q=low'
    u = set_scheme(u, 'http')
    assert get_scheme(u) == 'http'
    assert to_string(u) == 'http://hexlet.io/community?q=low'
    u = set_path(u, '/404')
    assert get_path(u) == '/404'
    assert to_string(u) == 'http://hexlet.io/404?q=low'
    u = set_query_param(u, 'page', 5)
    assert to_string(u) == 'http://hexlet.io/404?q=low&page=5'
    u = set_query_param(u, 'q', 'high')
    assert to_string(u) == 'http://hexlet.io/404?q=high&page=5'
    assert get_query_param(u, 'q') == 'high'
    assert get_query_param(u, 'user', 'guest') == 'guest'
    assert get_query_param(u, 'b') is None
    u = set_query_param(u, 'q', None)
    assert to_string(u) == 'http://hexlet.io/404?page=5'
    u = set_query_param(u, 'missed', None)
    assert to_string(u) == 'http://hexlet.io/404?page=5'
    u = make('https://hexlet.io/community')
    assert to_string(u) == 'https://hexlet.io/community'
    u = make('https://hexlet.io/?q=high&page=5')
    assert to_string(u) == 'https://hexlet.io/?q=high&page=5'
