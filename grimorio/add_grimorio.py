import pandas as pd 
import os 
import secrets
import string

class asignacion:
   # """
   #Esta clase asigna la afinidad magica, grimorio, portada y id
   #""""

    def __init__(self):
        pass

    def getPath(self,base,carpeta):
        cp_ob = os.listdir(base).index(carpeta)
        cp_f = os.listdir(base)[cp_ob]
        return   base+"\\"+cp_f
    
    def getId(self):
        letters = string.ascii_letters
        digits = string.digits
        alphabet = letters + digits 
        pwd_length= 10
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
        return pwd
    
    def getMagic(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        grimorio = self.getPath(BASE_DIR,"grimorio")
        static = self.getPath(grimorio,"static")
        path_read = static+"\\"+"Tipos_de_Magia.xlsx"
  
        df = pd.read_excel(path_read)

        affinity = df.sample(1)
        valAffinity =affinity.values[0][0]

        grimorio_dat = {"Sinceridad": "Trébol de 1 hoja.",
                        "Esperanza": "Trébol de 2 hojas.",
                        "Amor": "Trébol de 3 hojas.",
                        "Buena Fortuna": "Trébol de 4 hojas.",
                        "Desesperación": "Trébol de 5 hojas."}

        df2 = pd.DataFrame([[key, grimorio_dat[key]]
                        for key in grimorio_dat.keys()], columns=['Grimorio', 'Portada'])


        d = df2.sample(1)
    
        valGrimo =d.Grimorio.values[0]
        valPorta =d.Portada.values[0]
        
        return valGrimo, valPorta, valAffinity
    

if __name__ == "__main__":
    asig = asignacion()
    print(asig.getMagic())
    print(asig.getId())

