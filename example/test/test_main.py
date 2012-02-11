import mock

# may want to give pydoubles a go, as that supports prettier
# assertions/stubs/spies

from example import main

class TestIsItChristmas(object):
    @mock.patch('example.main.BeautifulSoup')
    @mock.patch('example.main.requests.get')
    def test_should_make_request_and_scrape(self, get, BeautifulSoup):
        main.is_it_christmas()
        get.assert_called_once_with('http://isitchristmas.com/')
        BeautifulSoup.assert_called_once_with(get.return_value.content)
