import tkinter as tk

mapel = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
         "Biologi", "Ekonomi", "Sejarah", "Geografi", "Informatika"]

def prediksi():
    hasil.config(text="Teknologi Informasi")
    
root = tk.Tk()
root.title("Prediksi Prodi")
root.geometry("400x560")

judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14, "bold"))
judul.pack(pady=15)

frame = tk.Frame(root)
frame.pack()