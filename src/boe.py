from bs4 import BeautifulSoup

import requests
import datetime
import csv

class Boe():

    def __init__(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

    def set_seccion(self, seccion):
        self.seccion = seccion

    def get_seccion(self):
        return self.seccion

    def set_departamento(self, departamento):
        self.departamento = departamento

    def get_departamento(self):
        return self.departamento

    def set_referencia(self, referencia):
        self.referencia = referencia

    def get_referencia(self):
        return self.referencia

    def set_texto(self, texto):
        self.texto = texto

    def get_texto(self):
        return self.texto

class Scraping():

    def get_html(self, url):
        now = datetime.datetime.now()
        date = now.strftime("%Y%m%d")
        # Download HTML
        #page = requests.get(url + '20200411')
        page = requests.get(url + date)

        if page.status_code == 200:
            print("Obtener Páginas del BOE del dia: " + date) 
            soup = BeautifulSoup(page.content, 'html.parser', from_encoding="utf-8")

            for link in soup.find_all('urlhtm'):
                self.__analyze_link (link.string)