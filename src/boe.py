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
            lista_documentos = []
            for link in soup.find_all('urlhtm'):
                lista_documentos.append(self.__analyze_link (link.string))

            self.__export_to_csv(lista_documentos, date)

    def __analyze_link(self, link):
        page = requests.get('https://boe.es' + link)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser', from_encoding="utf-8")
            boe = Boe(soup.find('h3', class_="documento-tit").next)

            i = 0
            while i < len(soup.find_all('dd')):
                #if(soup.find_all('dt')[i].string == "Publicado en:"):
                    # print(soup.find_all('dd')[i].string)
                #elif(soup.find_all('dt')[i].string == "Sección:"):
                if(soup.find_all('dt')[i].string == "Sección:"):
                    boe.set_seccion(soup.find_all('dd')[i].string)
                elif(soup.find_all('dt')[i].string == "Departamento:"):
                    boe.set_departamento(soup.find_all('dd')[i].string)
                elif(soup.find_all('dt')[i].string == "Referencia:"):
                    boe.set_referencia(soup.find_all('dd')[i].string)
                
                i += 1
            
            str = ''
            for text in soup.find('div', id='DOdocText').find_all('p'):
                if (text.string is not None):
                    # Quitamos el pipe | para exportar correctamente los datos
                    str = str + text.string.replace("|", "") + '. '
            boe.set_texto(str)

            return boe

    def __export_to_csv(self, lista_documentos, date):   
        print("Exportar la información a CSV") 
        with open('boe_' + date + '.csv', mode='w', newline='', encoding="utf8") as documentos_file:
            writer = csv.writer(documentos_file, delimiter='|')
            writer.writerow(["Referencia","Departamento","Sección","Título","Texto"])
            for documento in lista_documentos:
                writer.writerow([documento.get_referencia(), documento.get_departamento(), documento.get_seccion(), documento.get_titulo(), documento.get_texto()])