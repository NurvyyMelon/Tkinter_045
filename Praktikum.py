import tkinter as tk

def hitung_prediksi():
    label_hasil.config(text="Hasil Prediksi: Teknologi Informasi")
    
top = tk.Tk()
top.title("Aplikasi Prediksi")  
top.geometry("380x550")

judul = tk.Label(top, text="Aplikasi prediksi Prodi Pilihan")
judul.grid(row=0, column=0, columnspan=2, pady=10)

L1 = tk.Label(top, text="Nilai Mapel 1: ")
L1.grid(row=1, column=0, sticky="w", padx=20, pady=2)
E1 = tk.Entry(top, bd=3)
E1.grid(row=1, column=1, padx=20, pady=2)

L2 = tk.Label(top, text="Nilai Mapel 2: ")
L2.grid(row=2, column=0, sticky="w", padx=20, pady=2)
E2 = tk.Entry(top, bd=3)
E2.grid(row=2, column=1, padx=20, pady=2)