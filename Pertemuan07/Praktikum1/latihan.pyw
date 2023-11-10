import tkinter as tk
import socket

def nslookup():
    domain = domain_entry.get()
    try:
        ip_address = socket.gethostbyname(domain)
        result_label.config(text=f"Nama domain: {domain}\nAlamat IP: {ip_address}")
    except socket.gaierror:
        result_label.config(text=f"Tidak dapat menemukan alamat IP untuk domain: {domain}")

# Membuat jendela utama
root = tk.Tk()
root.title("Nslookup App")

# Menambahkan perintah untuk mengatur ukuran jendela
root.geometry("400x200")  # Ganti ukuran jendela sesuai kebutuhan (Lebar x tinggi)

# Label dan input domain
domain_label = tk.Label(root, text="Masukkan domain:")
domain_label.pack(pady=10)
domain_entry = tk.Entry(root)
domain_entry.pack()

# Tombol untuk melakukan nslookup
lookup_button = tk.Button(root, text="Nslookup", command=nslookup)
lookup_button.pack(pady=10)

# Label untuk hasil
result_label = tk.Label(root, text="", wraplength=300)
result_label.pack()

root.mainloop()
