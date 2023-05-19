import pickle
class Magasin:
    def __init__(self):
        self.__produits=list()
   
    def getProduits(self):
        return self.__produits
    def setProduits(self,produits):
        self.__produits=produits
    
    def ajouter(self,produit):
        self.__produits.append(produit)
    def supprimer(self,produit):
        self.__produits.remove(produit)

    def exists(self,id):
        existance=False
        for produit in self.__produits:
            if produit.getId()==id:
                existance=True
                break
        return existance    

    # def chercher(self,id):
    #     for produit in self.__produits:
    #         if produit.getId()==id:
    #            return produit
    def chercher(self,id):
        pr=None
        for produit in self.__produits:
            if produit.getId()==id:
                pr=produit
                break
        return pr    

    def afficher(self):
        for produit in self.__produits:
            produit.afficher()

    def Enregistrer(self):
        fichier=open("produit.bin","wb")
        pickle.dump(self.__produits,fichier)
        fichier.close()
    def Charger(self):
        fichier=open("produit.bin","rb")
        self.__produits=pickle.load(fichier)
        fichier.close()
