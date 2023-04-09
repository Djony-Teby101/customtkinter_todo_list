import customtkinter as ctk

#fonction d'ajout des taches.
def add_todo():
    todo=entry.get()
    label=ctk.CTkLabel(scollable_frame, text=todo)
    label.pack()
    entry.delete(0, ctk.END)

# encapsuler l'app dans une variable.
ctk.set_appearance_mode("dark")

root=ctk.CTk()

#definir la taille de l'ecran & le titre de la fenetre.

root.geometry("750x450")
root.title("Todo App")

#creer le premier widget.
title_label=ctk.CTkLabel(root,text="Tache â faire:",font=ctk.CTkFont(size=25,weight="bold"))
title_label.pack(padx=10,pady=(40,20))
#scrolle barre.
scollable_frame=ctk.CTkScrollableFrame(root,width=500,height=200)
scollable_frame.pack()


#espace input & placeholder.
entry= ctk.CTkEntry(scollable_frame, placeholder_text="ajouter une tache")
entry.pack(fill="x")

#button d'ajout.
add_button=ctk.CTkButton(root, text='Ajouter', width=200,command=add_todo)
add_button.pack(padx=5,pady=3)


root.mainloop()

