import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO
import wikipedia
import requests
from bs4 import BeautifulSoup
wikipedia.set_lang("pt")

print('''

██████╗░██████╗░░█████╗░████████╗░░░░░██╗███████╗░█████╗░████████╗  ██╗░░░░█████╗░
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝░░░░░██║██╔════╝██╔══██╗╚══██╔══╝  ██║░░░██╔══██╗
██████╔╝██████╔╝██║░░██║░░░██║░░░░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░  ██║░░░███████║
██╔═══╝░██╔══██╗██║░░██║░░░██║░░░██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░  ██║░░░██╔══██║
██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝███████╗╚█████╔╝░░░██║░░░  ██║██╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░  ╚═╝╚═╝╚═╝░░╚═╝

''')

print("Bem vindo ao ProtJect I.A, aqui temos uma variação de buscadores, selecione o que deseja :)")



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", padding=6, font=("Helvetica", 14))
        
        # obter imagem da web
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/220px-Wikipedia-logo-v2.svg.png"
        with urllib.request.urlopen(url) as url_response:
            image_data = url_response.read()
        img = Image.open(BytesIO(image_data))

        # converter imagem em objeto PhotoImage do Tkinter
        self.wikipedia_img = ImageTk.PhotoImage(img)

        self.wiki_button = ttk.Button(self, image=self.wikipedia_img, compound="top")
        self.wiki_button["text"] = "Pesquisar na Wikipedia"
        self.wiki_button["command"] = self.search_wiki
        self.wiki_button.pack(side="top")
        
        # obter imagem da web
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/588px-Google_%22G%22_Logo.svg.png"
        with urllib.request.urlopen(url) as url_response:
            image_data = url_response.read()
        goglis = Image.open(BytesIO(image_data))

        self.google_img = ImageTk.PhotoImage(goglis)

        self.google_button = ttk.Button(self, image=self.google_img, compound="top")
        self.google_button = ttk.Button(self)
        self.google_button["text"] = "Pesquisar no Google"
        self.google_button["command"] = self.search_google
        self.google_button.pack(side="top")
        
        self.quit_button = ttk.Button(self, text="Sair", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

    def search_wiki(self):
        resultados = input("O que você quer pesquisar na Wikipedia?: ")
        try:
            resultados_paginas = wikipedia.search(resultados)
            if len(resultados_paginas) == 0:
                print("Não foram encontrados resultados para a sua pesquisa.")
            else:
                pagina = wikipedia.page(resultados_paginas[0])
                print(pagina.summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print("Há ambiguidade na sua pesquisa. Por favor, especifique melhor.")
    
    def search_google(self):
        resultados1 = input("O que você quer pesquisar no Google?: ")
        try:
            url = f"https://www.google.com/search?q={resultados1}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
            }
            response = requests.get(url, body=headers)
            soup = BeautifulSoup(response.content, "html.parser")
            results = soup.select(".tF2Cxc")
            if not results:
                print("Não foram encontrados resultados para a sua pesquisa.")
            else:
                title = results[0].select_one(".DKV0Md").text
                description = results[0].select_one(".VwiC3b").text
                print(title)
                print(description)
        except Exception as e:
            print("Ocorreu um erro durante a pesquisa:", e)

root = tk.Tk()
app = Application(master=root)
app.mainloop()

