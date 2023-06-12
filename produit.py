class Produit:
    auto=0
    def __init__(self,id,design,prix) :
        Produit.auto+=1
        self.setId(id)
        self.setDesign(design)
        self.setPrix(prix)

    def getId(self):
        return self.__id        

    def setId(self,id):
        if id>0:
            self.__id=id
        else:
            ex=Exception("Attention l'id du produit doit être strictement positif !")
            raise ex

    def getDesign(self):
        return self.__design        

    def setDesign(self,design):
        if len(design)>0:
            self.__design=design
        else:
            raise Exception("Attention la designation du produit ne doit pas  être vide !")
           

    def getPrix(self):
        return self.__prix       

    def setPrix(self,prix):
        if prix>0:
            self.__prix=prix
        else:
            raise Exception("Attention le prix du produit doit être strictement positif !")
            
    def __str__(self) :
        return str(self.__id) +'\t'+ self.__design+'\t'+str(self.__prix)
    def afficher(self):
        print(self)