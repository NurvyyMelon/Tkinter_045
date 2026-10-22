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

L3 = tk.Label(top, text="Nilai Mapel 3: ")
L3.grid(row=3, column=0, sticky="w", padx=20, pady=2)
E3 = tk.Entry(top, bd=3)
E3.grid(row=3, column=1, padx=20, pady=2)

L4 = tk.Label(top, text="Nilai Mapel 4: ")
L4.grid(row=4, column=0, sticky="w", padx=20, pady=2)
E4 = tk.Entry(top, bd=3)
E4.grid(row=4, column=1, padx=20, pady=2)

L5 = tk.Label(top, text="Nilai Mapel 5: ")
L5.grid(row=5, column=0, sticky="w", padx=20, pady=2)
E5 = tk.Entry(top, bd=3)
E5.grid(row=5, column=1, padx=20, pady=2)

L6 = tk.Label(top, text="Nilai Mapel 6: ")
L6.grid(row=6, column=0, sticky="w", padx=20, pady=2)
E6 = tk.Entry(top, bd=3)
E6.grid(row=6, column=1, padx=20, pady=2)

L7 = tk.Label(top, text="Nilai Mapel 7: ")
L7.grid(row=7, column=0, sticky="w", padx=20, pady=2)
E7 = tk.Entry(top, bd=3)
E7.grid(row=7, column=1, padx=20, pady=2)

L8 = tk.Label(top, text="Nilai Mapel 8: ")
L8.grid(row=8, column=0, sticky="w", padx=20, pady=2)
E8 = tk.Entry(top, bd=3)
E8.grid(row=8, column=1, padx=10, pady=2)

L9 = tk.Label(top, text="Nilai Mapel 9: ")
L9.grid(row=9, column=0, sticky="w", padx=20, pady=2)
E9 = tk.Entry(top, bd=3) 
E9.grid(row=9, column=1, padx=20, pady=2)

L10 = tk.Label(top, text="Nilai Mapel 10: ")
L10.grid(row=10, column=0, sticky="w", padx=20, pady=2)
E10 = tk.Entry(top, bd=3)
E10.grid(row=10, column=1, padx=20, pady=2)

btn_prediksi = tk.Button(top, text="Hasil Prediksi", command=hitung_prediksi)
btn_prediksi.grid(row=11, column=0, columnspan=2, pady=15)

label_hasil = tk.Label(top, text="Hasil Prediksi: -")
label_hasil.grid(row=12, column=0, columnspan=2, pady=5)

top.mainloop()