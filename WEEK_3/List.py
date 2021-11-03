# Latihan List 
Mahasiswa = ["Abimanyu Luthfi Rizq Ramadhan", "2020071036", "Informatika", "Desain dan Analisis Algoritma", "21", "UPJ"]
print(Mahasiswa) #menampilkan seluruh data yang ada pada List Mahasiswa
print(Mahasiswa[1])#Mengambil dan mencetak data NIM
print(Mahasiswa[5])#Mengambil dan mencetak nama Universitas
print(Mahasiswa[1:3])#Mengambil dan mencetak NIM dan Prodi menggunakan list slicing
# Menambahkan kata UPJ menggunakan Iterasi
for aUniv in Mahasiswa:
    print("UPJ " + aUniv)
