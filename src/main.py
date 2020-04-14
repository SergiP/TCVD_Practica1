from configuration import Configuration
from boe import Boe, Scraping

# pip install request
# pip install configparser
# pip install beautifulsoup4

config = Configuration('config.properties')
scraping = Scraping()
scraping.get_html(config.get_url())