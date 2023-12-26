from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import pandas as pd

class Application(Tk):
    def __init__(self,title,geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.configure(bg="#669bbc")
        self.frame()
        self.widgets()
    
    def frame(self):
        self.frame = Frame(self, bg="#fdf0d5", bd=1, highlightbackground="#003049",highlightthickness=1)
        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.95)

    def widgets(self):
        self.filename = Button(self.frame, text="Select a file", command=self.selectAfile)
        self.filename.place(relx=0.2, rely=0.3, relwidth=0.3, relheight=0.15)
        self.savefile = Button(self.frame, text="save file", command=self.saveFile)
        self.savefile.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.15)

    #func para selecionar caminho do arquivo json    
    def selectAfile(self):
        self.filetypes = [(".json", "*.json")] #extensão de arquivo permitido
        self.file = askopenfilename(title="Open a file", initialdir="/",filetypes=self.filetypes) # guarda caminho do arquivo
        self.res = pd.read_json(self.file) #lê o arquivo

    # converte arquivo e salva no caminho expecificado
    def saveFile(self):
        self.path = asksaveasfilename(title="Save file",filetypes=self.filetypes, initialdir="/") # guarda caminho do diretorio
        self.res.to_csv(self.path) #converte o arquivo json para csv, e é salvo no caminho expecificado

app = Application("converter","400x200")
app.mainloop()