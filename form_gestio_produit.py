import tkinter as tk
from magasin import Magasin
from produit import Produit
from tkinter import messagebox
class FormGestionProduit:
    def __init__(self,fenetre:tk.Tk):
        self.magasin=Magasin()
        self.fenetre= fenetre
        self.fenetre.iconify()
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Gestion des produits")
        self.btnFermer=tk.Button(self.root,command=self.fermer,relief="raised",bd=15,text="Fermer",bg="orange",fg="white",font="Arial 16 italic bold")
        self.btnFermer.pack(side="bottom")
        self.frameEntry=tk.LabelFrame(self.root,text='Info. Produit')
        self.frameEntry.pack(expand=1)
        self.lblId=tk.Label(self.frameEntry, text="Id",font="Arial 16 italic bold")
        self.lblId.grid(row=0,column=0,sticky=tk.W)
        self.entryId=tk.Entry(self.frameEntry,font="Arial 16 italic bold")
        self.entryId.grid(row=0,column=1)

        self.lblDesign=tk.Label(self.frameEntry, text="Designation",font="Arial 16 italic bold")
        self.lblDesign.grid(row=1,column=0,sticky=tk.W)
        self.entryDesign=tk.Entry(self.frameEntry,font="Arial 16 italic bold")
        self.entryDesign.grid(row=1,column=1)

        self.lblPrix=tk.Label(self.frameEntry, text="Prix",font="Arial 16 italic bold")
        self.lblPrix.grid(row=2,column=0,sticky=tk.W,)
        self.entryPrix=tk.Entry(self.frameEntry,font="Arial 16 italic bold")
        self.entryPrix.grid(row=2,column=1)

        self.frameButton=tk.LabelFrame(self.root,text="Actions")
        self.frameButton.pack(expand=tk.YES)

        self.btnAjouter=tk.Button(self.frameButton,command=self.ajouter,relief="raised",bd=15,text="Ajouter",bg="blue",fg="white",font="Arial 16 italic bold")
        self.btnAjouter.pack(side=tk.LEFT)

        self.btnSupprimer=tk.Button(self.frameButton,command=self.supprimer,relief="raised",bd=15,text="Supprimer",bg="blue",fg="white",font="Arial 16 italic bold")
        self.btnSupprimer.pack(side=tk.LEFT)
        
        self.btnAfficher=tk.Button(self.frameButton,command=self.afficher,relief="raised",bd=15,text="Afficher",bg="blue",fg="white",font="Arial 16 italic bold")
        self.btnAfficher.pack(side=tk.LEFT)


        
        
        self.root.mainloop()

    
    
    def fermer(self):
        self.fenetre.deiconify()
        self.root.destroy()
    def ajouter(self):
        try:
            self.magasin.ajouter(Produit(int(self.entryId.get()),self.entryDesign.get(),float(self.entryPrix.get())))
            self.effacerEntry()
            
        except Exception as ex:
            messagebox.showwarning(title="Ajout Produit",message=ex)



    def supprimer(self):
        self.entryDesign.insert(index=0,string='fsefsdf')

    def afficher(self):
        pass

    def effacerEntry(self):
        self.entryId.delete(first=0,last=len(self.entryId.get()))
        self.entryDesign.delete(first=0,last=len(self.entryDesign.get()))
        self.entryPrix.delete(first=0,last=len(self.entryPrix.get()))
        self.entryId.focus()
