import datetime
import pandas
import collections

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from get_winery_and_product_data import get_winary_age, get_wines_from_file


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

wine_data = get_wines_from_file()
winery_age = get_winary_age()

template = env.get_template('template.html')

rendered_page = template.render(
    winery_age=winery_age,
    wine_data=wine_data,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
