import tkinter as tk

def hitung():
    try:
        sisi = float(entry_sisi.get())
        luas_permukaan = 6 * sisi**2
        volume = sisi**3

        label_hasil.config(text=f"Luas Permukaan: {luas_permukaan:.2f}\nVolume: {volume:.2f}")
    except ValueError:
        label_hasil.config(text="Masukan tidak valid. Pastikan Anda memasukkan angka.")


root = tk.Tk()
root.title("Kalkulator Kubus")


label_sisi = tk.Label(root, text="Masukkan Panjang Sisi Kubus:")
label_sisi.pack()
entry_sisi = tk.Entry(root)
entry_sisi.pack()


btn_hitung = tk.Button(root, text="Hitung", command=hitung)
btn_hitung.pack()


label_hasil = tk.Label(root, text="")
label_hasil.pack()

# Memulai loop GUI
root.mainloop()