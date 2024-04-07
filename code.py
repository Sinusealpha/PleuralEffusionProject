import tkinter as tk
from tkinter import ttk

# Function to determine diagnosis
def diagnose():
    test_values = {
        "Adenosine deaminase (ADA)": float(test_1.get()),
        "Cytology": str(test_2.get()),
        "Glucose": float(test_3.get()),
        "Lactate dehydrogenase (LDH)": float(test_4.get()),
        "LDH fluid to serum ratio": float(test_5.get()),
        "Protein fluid to serum ratio": float(test_6.get()),
        "Red blood cell count": float(test_7.get()),
        "White blood cell count and differential": float(test_8.get()),
        "Lymphocytes": float(test_9.get()),
        "Neutrophils": float(test_10.get())
    }

    diagnosis = ""

    # Conditions based on the table
    if test_values["Adenosine deaminase (ADA)"] > 40: # per U/L
        diagnosis += "Because of 'Adenosine deaminase (ADA)', suggested diagnoses are as follows:\n1- Tuberculosis (>90%)\n2- empyema (60%)\n3- complicated parapneumonic effusion (30%)\n4- malignancy (5%)\n5- rheumatoid arthritis\n\n"

    if test_values["Cytology"] == "Present" or "present":
        diagnosis += "Because of 'Cytology', suggested diagnose is as follows:\n1- Malignancy\n\n"

    if test_values["Glucose"] < 60: # per mg/dL
        diagnosis += "Because of 'Glucose', suggested diagnoses are as follows:\n1- Complicated parapneumonic effusion or empyema\n2- tuberculosis (20%)\n3- malignancy (<10%)\n4- rheumatoid arthritis\n\n"

    if test_values["Lactate dehydrogenase (LDH)"] > 1000:
        diagnosis += "Because of 'Glucose', suggested diagnose is:\n1- Any condition causing an exudate!\n\n"

    if test_values["LDH fluid to serum ratio"] > 0.6:
        diagnosis += "Because of 'LDH fluid to serum ratio', suggested diagnose is:\n1- Any condition causing an exudate!\n\n"

    if test_values["Protein fluid to serum ratio"] > 0.5:
        diagnosis += "Because of 'Protein fluid to serum ratio', suggested diagnose is:\n1- Any condition causing an exudate!\n\n"

    if test_values["Red blood cell count"] > 100000: # per mm**3
        diagnosis += "Because of 'Red blood cell count', suggested diagnoses are as follows:\n1- Malignancy\n2- trauma\n3- parapneumonic effusion\n4- pumonary embolism\n\n"

    if test_values["White blood cell count and differential"] > 10000: # per mm**3
        diagnosis += "Because of 'White blood cell count', suggested diagnoses are as follows:\n1- Empyema\n2- other exudates (uncommon)\n\n"

    if test_values["Lymphocytes"] > 50: # percent
        diagnosis += "Because of 'Lymphocytes', suggested diagnoses are as follows:\n1- Malignancy\n2- tuberculosis\n3- pulmonaryembolism\n4- coronary artery bypass surgery\n\n"

    if test_values["Neutrophils"] > 50: # percent
        diagnosis += "Because of 'Neutrophils', suggested diagnoses are as follows:\n1- Parapneumonic effusion\n2- pulmonaryembolism\n3- abdominal diseases\n\n"

    # Add more conditions as needed
    result.set(diagnosis)

# Create main window
root = tk.Tk()
root.title("Pleural Effusion Diagnosis")

# Create StringVars for text fields
test_1 = tk.StringVar()
test_2 = tk.StringVar()
test_3 = tk.StringVar()
test_4 = tk.StringVar()
test_5 = tk.StringVar()
test_6 = tk.StringVar()
test_7 = tk.StringVar()
test_8 = tk.StringVar()
test_9 = tk.StringVar()
test_10 = tk.StringVar()

result = tk.StringVar()

# Create labels and entry widgets for each test
tests = [
    "amount of Adenosine deaminase (ADA)",
    "Cytology / present or absent",
    "amount of Glucose",
    "amount of Lactate dehydrogenase (LDH)",
    "amount of LDH fluid to serum ratio",
    "amount of Protein fluid to serum ratio",
    "amount of Red blood cell count",
    "amount of White blood cell count and differential",
    "precent of Lymphocytes",
    "percent of Neutrophils"
]

for i, test in enumerate(tests):
    tk.Label(root, text=test).grid(row=i, column=0)
    tk.Entry(root, textvariable=eval(f"test_{i+1}")).grid(row=i, column=1)

# Buttons
tk.Button(root, text="Diagnose", command=diagnose).grid(row=len(tests), columnspan=4) # diagnose
ttk.Button(root, text="Quit", command=root.destroy).grid(column=2, row=(len(tests)+1)) # quit

# Display diagnosis result

tk.Label(root, text="Diagnosis Result:").grid(row=len(tests) + 1, column=0)
tk.Label(root, textvariable=result).grid(row=len(tests) + 1, column=1)

root.mainloop()

