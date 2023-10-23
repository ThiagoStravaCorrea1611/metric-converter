from tkinter import *

# Create window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

#Input:
input = Entry(width=50)
input.grid(column=1, row=0)

# Label: "Miles"
label_02 = Label(text="Miles", font=("Arial", 24, "bold"))
label_02.grid(column=2, row=0)
label_02.config(padx=50, pady=50)

# Label: "is equal to"
label_03 = Label(text="is equal to", font=("Arial", 24, "bold"))
label_03.grid(column=0, row=1)
label_03.config(padx=50, pady=50)

# Output
output = Label(text="000", font=("Arial", 24, "bold"))
output.grid(column=1, row=1)
output.config(padx=50, pady=50)

# Label: "Km"
label_04 = Label(text="Km", font=("Arial", 24, "bold"))
label_04.grid(column=2, row=1)
label_04.config(padx=50, pady=50)

# Button
def button_clicked():
    miles_input = int(input.get())
    km_otput = str(1.609344*miles_input)
    output.config(text=km_otput)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=50, pady=50)


window.mainloop()