import os

from dotenv import load_dotenv
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from get_winery_and_product_data import get_winary_age, get_wines_from_file, get_correct_winery_age


def main():
    load_dotenv()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    filename = os.environ["WINE_FILENAME"]

    wine_data = get_wines_from_file(filename)
    winery_age = get_winary_age()
    correct_winery_age = get_correct_winery_age(winery_age)

    template = env.get_template('template.html')

    rendered_page = template.render(
        winery_age=correct_winery_age,
        wine_data=wine_data,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
