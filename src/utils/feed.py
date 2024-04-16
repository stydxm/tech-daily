import requests
from rss_parser import RSSParser, AtomParser
from rss_parser.models import XMLBaseModel


def parse_rss(url: str) -> XMLBaseModel:
    response = requests.get(url)
    rss = RSSParser.parse(response.text)
    return rss


def parse_atom(url: str) -> XMLBaseModel:
    response = requests.get(url)
    atom = AtomParser.parse(response.text)
    return atom
