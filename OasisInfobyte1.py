def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    if height <= 0 or weight <= 0:
        result_label.config(text="Please enter valid weight and height.")
        return

    bmi = weight / (height ** 2)
    category = None

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    result_label.config(text=f"Your BMI is {bmi:.2f}. You are in the {category} category.")

# Create the graphical interface
import tkinter as tk

window = tk.Tk()
window.title("BMI Calculator")

weight_label = tk.Label(window, text="Weight (kg):")
weight_label.grid(row=0, column=0)
weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1)

height_label = tk.Label(window, text="Height (m):")
height_label.grid(row=1, column=0)
height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1)

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2)

window.mainloop()