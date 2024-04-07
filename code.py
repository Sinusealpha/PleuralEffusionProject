import tkinter as tk
from tkinter import ttk

# Function
def diagnose():
    test_values = {
        "PF/Serum Protein Ratio": float(test_1.get()),
        "PF/Serum LDH Ratio": float(test_2.get()),
        "PF LDH > 2/3 Upper Normal Serum Limit": float(test_3.get()),
        "Adenosine deaminase (ADA)": float(test_4.get()),
        "Cytology": str(test_5.get()),
        "Glucose": float(test_6.get()),
        "Red blood cell count": float(test_7.get()),
        "White blood cell count and differential": float(test_8.get()),
        "Lymphocytes": float(test_9.get()),
        "Neutrophils": float(test_10.get())
    }

    diagnosis = ""

    # conditions
    #1 #2 #3
    if test_values["PF/Serum Protein Ratio"] > 0.5 or test_values["PF/Serum LDH Ratio"] > 0.6 or test_values["PF LDH > 2/3 Upper Normal Serum Limit"] == "yes" or "Yes":
        diagnosis += "Your extracted fluid is Exudate\n"
    
    #4
    if test_values["Adenosine deaminase (ADA)"] > 40: # per U/L
        diagnosis += "Because of 'Adenosine deaminase (ADA)', suggested diagnoses are as follows:\n1- Tuberculosis (>90%)\n2- empyema (60%)\n3- complicated parapneumonic effusion (30%)\n4- malignancy (5%)\n5- rheumatoid arthritis\n\n"

    #5
    if test_values["Cytology"] == "Present" or "present":
        diagnosis += "Because of 'Cytology', suggested diagnose is as follows:\n1- Malignancy\n\n"

    #6
    if test_values["Glucose"] < 60: # per mg/dL
        diagnosis += "Because of 'Glucose', suggested diagnoses are as follows:\n1- Complicated parapneumonic effusion or empyema\n2- tuberculosis (20%)\n3- malignancy (<10%)\n4- rheumatoid arthritis\n\n"

    #7
    if test_values["Red blood cell count"] > 100000: # per mm**3
        diagnosis += "Because of 'Red blood cell count', suggested diagnoses are as follows:\n1- Malignancy\n2- trauma\n3- parapneumonic effusion\n4- pumonary embolism\n\n"

    #8
    if test_values["White blood cell count and differential"] > 10000: # per mm**3
        diagnosis += "Because of 'White blood cell count', suggested diagnoses are as follows:\n1- Empyema\n2- other exudates (uncommon)\n\n"

    #9
    if test_values["Lymphocytes"] > 50: # percent
        diagnosis += "Because of 'Lymphocytes', suggested diagnoses are as follows:\n1- Malignancy\n2- tuberculosis\n3- pulmonaryembolism\n4- coronary artery bypass surgery\n\n"

    #10
    if test_values["Neutrophils"] > 50: # percent
        diagnosis += "Because of 'Neutrophils', suggested diagnoses are as follows:\n1- Parapneumonic effusion\n2- pulmonaryembolism\n3- abdominal diseases\n\n"







    # Conditions
    
    
    
    
    
    
    
    # Add more conditions as needed
    result.set(diagnosis)

# main window
root = tk.Tk()
root.title("Pleural Effusion Diagnosis")

# StringVars for text fields
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

# labels and entry widgets for each test
tests = [
    "PF/Serum Protein Ratio",
    "PF/Serum LDH Ratio",
    "PF LDH > 2/3 Upper Normal Serum Limit",
    "Adenosine deaminase (ADA)",
    "Cytology",
    "Glucose",
    "Lactate dehydrogenase (LDH)",
    "Red blood cell count",
    "White blood cell count and differential",
    "Lymphocytes",
    "Neutrophils"
]
tk.Label(root, text="PF/Serum Protein Ratio").grid(row=1, column=0)
tk.Entry(root, textvariable=test_1).grid(row=1, column=1)

tk.Label(root, text="PF/Serum LDH Ratio").grid(row=2, column=0)
tk.Entry(root, textvariable=test_2).grid(row=2, column=1)

tk.Label(root, text="PF LDH > 2/3 Upper Normal Serum Limit").grid(row=3, column=0)
tk.Entry(root, textvariable=test_3).grid(row=3, column=1)

tk.Label(root, text="PF Glucose").grid(row=4, column=0)
tk.Entry(root, textvariable=test_4).grid(row=4, column=1)

tk.Label(root, text="PF Cytology").grid(row=5, column=0)
tk.Entry(root, textvariable=test_5).grid(row=5, column=1)

tk.Label(root, text="Adenosine deaminase (ADA)").grid(row=6, column=0)
tk.Entry(root, textvariable=test_6).grid(row=6, column=1)

tk.Label(root, text="Red blood cell count").grid(row=7, column=0)
tk.Entry(root, textvariable=test_7).grid(row=7, column=1)

tk.Label(root, text="White blood cell count").grid(row=8, column=0)
tk.Entry(root, textvariable=test_8).grid(row=8, column=1)

tk.Label(root, text="Lymphocytes' percent").grid(row=9, column=0)
tk.Entry(root, textvariable=test_9).grid(row=9, column=1)

tk.Label(root, text="Neutrophils' percent").grid(row=10, column=0)
tk.Entry(root, textvariable=test_10).grid(row=10, column=1)

# Buttons
tk.Button(root, text="Diagnose", command=diagnose).grid(row=len(tests), columnspan=4) # diagnose
ttk.Button(root, text="Quit", command=root.destroy).grid(column=2, row=(len(tests)+1)) # quit

# Display diagnosis result

tk.Label(root, text="Diagnosis Result:").grid(row=len(tests) + 1, column=0)
tk.Label(root, textvariable=result).grid(row=len(tests) + 1, column=1)

root.mainloop()

