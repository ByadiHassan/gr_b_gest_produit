from produit import Produit
class Habit(Produit):
    def __init__(self,design,prix,couleur,taille):
        super().__init__(design,prix)
        self.setCouleur(couleur)
        self.setTaille(taille)

    def getCouleur(self):
        return self.__couleur
    def setCouleur(self,couleur):
        if len(couleur)>0:
            self.__couleur=couleur
        else:
            raise Exception("Attention la couleur du produit ne doit pas  être vide !")
    def getTaille(self):
        return self.__taille
    def setTaille(self,taille):
        if len(taille)>0:
            self.__taille=taille
        else:
            raise Exception("Attention la taille du produit ne doit pas  être vide !")
    def __str__(self):
        return super().__str__() +'\t'+ self.__couleur+'\t'+self.__taille


if __name__=='__main__':
    h=Habit("Veste",200.50,"Rouge","XL")
    h.afficher()
