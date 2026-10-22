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

entries = []
for i in range(len(mapel)):
     e = tk.Entry(frame, width=12)
     e.grid(row=i, column=1, pady=3)
     entries.append(e)
      
tombol = tk.Button(root, text="Hasil Prediksi", command=prediksi)
tombol.pack(pady=20)

hasil = tk.Label(root, text="-", font=("Arial", 13, "bold"), fg="#00C3FF")
hasil.pack()

root.mainloop()
