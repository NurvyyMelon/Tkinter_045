import tkinter as tk

def hitung_prediksi():
    label_hasil.config(text="Hasil Prediksi: Teknologi Informasi")
    
top = tk.Tk()
top.title("Aplikasi Prediksi")  
top.geometry("380x550")

judul = tk.Label(top, text="Aplikasi prediksi Prodi Pilihan")
judul.grid(row=0, column=0, columnspan=2, pady=10)
