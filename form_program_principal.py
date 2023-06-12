import tkinter as tk
from form_gestio_produit import FormGestionProduit
from form_gestion_habit import FormGestionHabit
from form_gestion_produit_electrique import FormGestionProduitElectrique
class FormProgramPrincipal:
    def __init__(self) :
        self.root=tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Formulaire principal")
        self.root.iconbitmap("tree.ico")
        self.lblWelcome=tk.Label(self.root,relief="raised",bd=15,text="Bienvenu dans l'application gestion des produits",bg="blue",fg="white",font="Arial 16 italic bold")
        self.lblWelcome.pack()
        self.btnQuitter=tk.Button(self.root,command=self.root.destroy,relief="raised",bd=15,text="Quitter",bg="red",fg="white",font="Arial 16 italic bold")
        self.btnQuitter.pack(side="bottom")
        
        self.frameButton=tk.Frame(self.root,bg="yellow",padx=10,pady=10)
        self.frameButton.pack(expand=1)

        self.btnGestionProduit=tk.Button(self.frameButton,command=self.openFormGestionProduit,relief="raised",bd=15,text="Gest. Produits",bg="blue",fg="white",font="Arial 16 italic bold")
        self.btnGestionProduit.pack(side="left")

        self.btnGestionHabit=tk.Button(self.frameButton,command=self.openFormGestionHabit,relief="raised",bd=15,text="Gest. Habits",bg="blue",fg="white",font="Arial 16 italic bold")
        self.btnGestionHabit.pack(side="left")

        self.btnGestionProduitElectrique=tk.Button(self.frameButton,command=self.openFormGestionProduitElectrique,relief="raised",bd=15,text="Gest. Produits Elec.",bg="blue",fg="white",font="Arial 16 italic bold")
        self.btnGestionProduitElectrique.pack(side="left")




        self.root.mainloop()

    def openFormGestionProduit(self)   :
        FormGestionProduit(self.root)

    def openFormGestionHabit(self)   :
        FormGestionHabit()

    def openFormGestionProduitElectrique(self)   :
        FormGestionProduitElectrique()
