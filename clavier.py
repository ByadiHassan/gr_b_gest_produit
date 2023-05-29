from produit import Produit
from habit import Habit

class Clavier:
    @staticmethod
    def getString(msg):
        return input(msg)    
    @staticmethod
    def getInt(msg):
        error= True
        while error:
            try:
                return int(Clavier.getString(msg))                
            except Exception as ex:
                print(ex)
    @staticmethod      
    def getValue(f,msg):
        error= True
        while error:
            try:
                return f(Clavier.getString(msg))                
            except Exception as ex:
                print(ex)
    @staticmethod
    def getFloat(msg):
        error= True
        while error:
            try:
                return float(Clavier.getString(msg))               
            except Exception as ex:
                print(ex)        

    @staticmethod
    def getProduit():
        #id=Clavier.getInt("Tapez l'id du produit ? ")
        design=Clavier.getString("Tapez La désignation  du produit ? ")
        prix=Clavier.getValue(float,"Tapez le prix du produit ? ")
        p=Produit(design,prix)
        return p
        #return Produit(Clavier.getInt("Tapez l'id du produit ? "),
        # Clavier.getString("Tapez La désignation  du produit ? "),
        # Clavier.getFloat("Tapez le prix du produit ? "))
    @staticmethod
    def getHabit():
        return Habit(Clavier.getString("Tapez La désignation  du produit ? "),
        Clavier.getFloat("Tapez le prix du produit ? "),
        Clavier.getString("Tapez La couleur  du produit ? "),
        Clavier.getString("Tapez La taille  du produit ? "));