import tkinter as tk
import Recipies
import tkinter.font as font

window = tk.Tk(screenName='Recipes')
window.title('Recipies by K-Ruoka')
#Save recipe buttons in here
buttons = []


#Canvases and containers

recipeContainer = tk.Frame(window)
ingredientContainer = tk.Frame(window)
canvas = tk.Canvas(recipeContainer)
canvas2 = tk.Canvas(ingredientContainer, width=100, height=300,)
ingredientFrame = tk.Frame(canvas2, bg="blue")


#Making a Scrollable Frame
scrollbar = tk.Scrollbar(recipeContainer, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

#Creating buttons into frame
rec = Recipies.names
for i in range(len(rec)):
    b = tk.Button(scrollable_frame, text= rec[i], height=5, width=50, command=lambda i=i: onClick(i),
                  bg="blue",fg="white")
    b.pack()
    buttons.append(b)

#Packing the Recipies
recipeContainer.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#Button Functionality
def onClick(i):
    ingredientContainer.pack()
    l = ingredientFrame.pack_slaves()                        #Remove existing ingredients
    ingredients = Recipies.searchIngredients(i)
    for i in range(len(l)):
        l[i].destroy()

    for x in range(len(ingredients)):                          #Add new pressed ingredients
        tk.Label(ingredientFrame, text=ingredients[x], bg='blue', fg='black').pack()
    ingredientFrame.pack()

#Pack the 2nd half up
canvas2.pack(expand=False)
#Display
window.mainloop()