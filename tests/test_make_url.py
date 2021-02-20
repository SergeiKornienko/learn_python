from functions import make_url


def test_make_url():
    u = make_url.make('https://domain.org/community?q=low')
    assert make_url.to_string(u) == 'https://domain.org/community?q=low'

    u = make_url.set_host(u, 'hexlet.io')
    assert make_url.get_host(u) == 'hexlet.io'
    assert make_url.to_string(u) == 'https://hexlet.io/community?q=low'

    u = make_url.set_scheme(u, 'http')
    assert make_url.get_scheme(u) == 'http'
    assert make_url.to_string(u) == 'http://hexlet.io/community?q=low'

    u = make_url.set_path(u, '/404')
    assert make_url.get_path(u) == '/404'
    assert make_url.to_string(u) == 'http://hexlet.io/404?q=low'

    u = make_url.set_query_param(u, 'page', 5)
    assert make_url.to_string(u) == 'http://hexlet.io/404?q=low&page=5'

    u = make_url.set_query_param(u, 'q', 'high')
    assert make_url.to_string(u) == 'http://hexlet.io/404?q=high&page=5'
    assert make_url.get_query_param(u, 'q') == 'high'
    assert make_url.get_query_param(u, 'user', 'guest') == 'guest'
    assert make_url.get_query_param(u, 'b') is None

    u = make_url.set_query_param(u, 'q', None)
    assert make_url.to_string(u) == 'http://hexlet.io/404?page=5'

    u = make_url.set_query_param(u, 'missed', None)
    assert make_url.to_string(u) == 'http://hexlet.io/404?page=5'


def test_make_url_with_empty_params():
    u = make_url.make('https://hexlet.io/community')
    assert make_url.to_string(u) == 'https://hexlet.io/community'


def test_make_url_with_empty_path():
    u = make_url.make('https://hexlet.io/?q=high&page=5')
    assert make_url.to_string(u) == 'https://hexlet.io/?q=high&page=5'
