import tkinter as tk
import math

def hitung():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())
        
        luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
        volume = math.pi * jari_jari**2 * tinggi

        label_hasil.config(text=f"Luas Permukaan: {luas_permukaan:.2f}\nVolume: {volume:.2f}")
    except ValueError:
        label_hasil.config(text="Masukan tidak valid. Pastikan Anda memasukkan angka.")


root = tk.Tk()
root.title("Kalkulator Tabung")


label_jari_jari = tk.Label(root, text="Jari-Jari:")
label_jari_jari.pack()
entry_jari_jari = tk.Entry(root)
entry_jari_jari.pack()

label_tinggi = tk.Label(root, text="Tinggi:")
label_tinggi.pack()
entry_tinggi = tk.Entry(root)
entry_tinggi.pack()

btn_hitung = tk.Button(root, text="Hitung", command=hitung)
btn_hitung.pack()

label_hasil = tk.Label(root, text="")
label_hasil.pack()

root.mainloop()