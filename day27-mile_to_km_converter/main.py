import tkinter as tk

window = tk.Tk()
window.minsize(height=90, width=250)
window.title("Mile to Km Converter")

def convert():
    miles_value = float(miles_input.get())
    if miles_input is not None:
        value = round(1.6 * miles_value, 2)
        value_label.config(text=value)


miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0, row=1)

value_label = tk.Label(text="0")
value_label.grid(column=1, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

miles_input = tk.Entry(width=7)
miles_input.grid(column=1, row=0)

convert_button = tk.Button(text="Calculate", command=convert)
convert_button.grid(column=1, row=2)

window.mainloop()