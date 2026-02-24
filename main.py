import tkinter as tk

def klik(tekst):
    entry.insert(tk.END, tekst)

def wyczysc():
    entry.delete(0, tk.END)

def oblicz():
    try:
        dzialanie = entry.get().replace(",", ".")
        wynik = eval(dzialanie)

        if isinstance(wynik, float) and wynik.is_integer():
            wynik = int(wynik)

        entry.delete(0, tk.END)
        entry.insert(0, str(wynik))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Błąd")

okno = tk.Tk()
okno.title("Kalkulator")
okno.geometry("260x320")
okno.resizable(False, False)

entry = tk.Entry(okno, font=("Arial", 20), justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

ramka = tk.Frame(okno)
ramka.pack()

przyciski = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", "C", "=", "+"),
]

for wiersz in przyciski:
    r = tk.Frame(ramka)
    r.pack(expand=True, fill="both")
    for znak in wiersz:
        if znak == "=":
            cmd = oblicz
        elif znak == "C":
            cmd = wyczysc
        else:
            cmd = lambda x=znak: klik(x)

        b = tk.Button(
            r,
            text=znak,
            font=("Poppins", 16),
            command=cmd,
            height=2,
            width=5
        )
        b.pack(side="left", expand=True, fill="both")

okno.mainloop()