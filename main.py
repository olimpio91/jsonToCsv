from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showwarning
import pandas as pd

class Application(Tk):
    def __init__(self,title,geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.minsize(width=1000, height=400)
        self.configure(bg="#fdf0d5")
        self.frame()
        self.widgets()
    
    def frame(self):
        self.frame = Frame(self, bg="#fdf0d5")
        self.frame.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.99)

    def widgets(self):
        self.labeljson = Label(self.frame, text="JSON", font=("roboto", 10))
        self.labeljson.place(relx=0.1, rely=0.03, relwidth=0.1, relheight=0.06)
       
        self.labelcsv = Label(self.frame, text="CSV", font=("roboto", 10))
        self.labelcsv.place(relx=0.5, rely=0.03, relwidth=0.1, relheight=0.06)

        self.textAreaJson = Text(self.frame, state="normal")
        self.textAreaJson.place(relx=0.1, rely=0.1, relwidth=0.4, relheight=0.7)

        self.textAreaTocsv = Text(self.frame, state="normal")
        self.textAreaTocsv.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.7)

        self.select_a_file = Button(self.frame, text="SELECT A FILE", command=self.loadFile)
        self.select_a_file.place(relx=0.1, rely=0.81, relwidth=0.1, relheight=0.06)
        
        self.convert = Button(self.frame, text="CONVERTER", command=self.insertTextAreaCsv)
        self.convert.place(relx=0.2, rely=0.81, relwidth=0.1, relheight=0.06)
        
        self.savefile = Button(self.frame, text="SAVE FILE", command=self.saveFile)
        self.savefile.place(relx=0.3, rely=0.81, relwidth=0.1, relheight=0.06)

        self.buttonClear = Button(self.frame, text="CLEAR", command=self.clear)
        self.buttonClear.place(relx=0.4, rely=0.81, relwidth=0.1, relheight=0.06)


    def loadFile(self):
        self.filetype = [(".json", "*.json")]
        self.path = askopenfilename(filetypes=self.filetype, initialdir="/")
        with open(self.path , "r", encoding="utf8") as dt:
            self.textAreaJson.insert("1.0", dt.read())

    def insertTextAreaCsv(self):
        if self.textAreaJson.get("1.0",END).strip() == "":
            showwarning(title="Aviso!", message="Não foi possivel fazer a conversão")
        else:    
            self.dt_json = pd.read_json(self.path)
            self.file = self.dt_json.to_csv()
            self.textAreaTocsv.insert("1.0",self.file)

    def saveFile(self):
        if self.textAreaTocsv.get("1.0",END).strip() == "":
            showwarning(title="Aviso!", message="Não foi possivel salvar!")
            
        else:
            path = asksaveasfilename(initialdir="/")
            if not path.endswith(".csv"):
                path += ".csv"
            self.dt_json.to_csv(path)
    
    def clear(self):
        self.textAreaJson.delete("1.0", END)
        self.textAreaTocsv.delete("1.0",END)
app = Application("converter","1000x400")
app.mainloop()