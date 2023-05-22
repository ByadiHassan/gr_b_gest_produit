from magasin import Magasin
from produit import Produit
from clavier import Clavier
mag =Magasin()
choix=0
while choix!=5:
    choix=Clavier.getInt ("1. Ajouter\n2. Afficher\n3. Enregistrer\n4. Ouvrir\n5. Quitter\n4.Tapez votre choix ?")
    if choix==1:
        # id=int(input("Tapez l'id du produit ? "))
        # design=input("Tapez La désignation  du produit ? ")
        # prix=float(input("Tapez le prix du produit ? "))
        # p=Produit(id,design,prix)
        #mag.ajouter(p)
        mag.ajouter(Clavier.getProduit())
    elif choix==2:
        mag.afficher()
    elif choix==3:
        mag.Enregistrer()
    elif choix==4:
        mag.Charger()
        mag.afficher()












