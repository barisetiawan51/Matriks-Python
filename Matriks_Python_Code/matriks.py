#Nama   : Imam bari Setiawan
#NIM    : 2103040139
#Matkul : Komputasi Numerik 
#         (Program Matriks menggunakan python)

import numpy as np

def penjumlahan():
    print("===============================")
    print ("Hasil dari penjumlahan matriks Q+R adalah :")
    hasil_jumlah = []
    for i in range(ordo):
        jumlah = []
        for j in range(ordo):
            nilai = matriks1[i][j] + matriks2[i][j]
            jumlah.append(nilai)
        hasil_jumlah.append(jumlah)

    for baris in hasil_jumlah:
        print("|\t", end="")
        for kolom in baris:
            print(kolom, "\t", end="")
        print("|")
    print("\n")
def pengurangan():
    print("===============================")
    print("Hasil dari pengurangan matriks Q-R adalah:")
    hasil_kurang = []
    for i in range(ordo):
        kurang = []
        for j in range (ordo):
            nilai = matriks1[i][j] - matriks2[i][j]
            kurang.append(nilai)
        hasil_kurang.append(kurang)

    for baris in hasil_kurang:
        print("|\t", end="")
        for kolom in baris:
            print(kolom, "\t", end="")
        print("|")
    print("\n")
def perkalian(baris, kolom):
    print("Hasil dari perkalian matriks A.B adalah:")
    hasil_kali = []
    for i in range(len(baris)):
        kali = []
        for j in range (len(kolom)):
            total = 0
            for k in range(len(baris)):
                total += (baris[i][k]*kolom[k][j])
            kali.append(total)
        hasil_kali.append(kali)

    for baris in hasil_kali:
        print("|\t", end="")
        for kolom in baris:
            print(kolom,"\t", end="")
        print("|")
    print("\n")
def determinan():
    print("Nilai determinannya:")
    if ordo == 2:
        determinan = matriks[0][0]*matriks[1][1] - matriks[0][1]*matriks[1][0]
        print(determinan)
    elif ordo == 3:
        """Menggunakan cara sarus"""
        determinan = matriks[0][0]*matriks[1][1]*matriks[2][2]\
            + matriks[1][0]*matriks[2][1]*matriks[0][2]\
            + matriks[2][0]*matriks[0][1]*matriks[1][2]\
            - matriks[1][0]*matriks[0][1]*matriks[2][2]\
            - matriks[0][0]*matriks[2][1]*matriks[1][2]\
            - matriks[2][0]*matriks[1][1]*matriks[0][2]
        print(determinan)
    elif ordo == 4:
        print(def_4(matriks))
def determinan2(*variable):
    for x in variable :
        determinan = x[0][0]*x[1][1]*x[2][2]\
            + x[1][0]*x[2][1]*x[0][2]\
            + x[2][0]*x[0][1]*x[1][2]\
            - x[1][0]*x[0][1]*x[2][2]\
            - x[0][0]*x[2][1]*x[1][2]\
            - x[2][0]*x[1][1]*x[0][2]
        return determinan
def def_4(matriks):
    matriks_a = []
    matriks_b = []
    matriks_c = []
    matriks_d = []
    if len(matriks_a) != 3:
        for i in range (ordo):
            tampung = []
            if i != 0:
                for j in range (ordo):
                    if j != 0:
                        tampung.append(matriks[i][j])
                matriks_a.append(tampung)
    if len(matriks_b) != 3:
        for i in range (ordo):
            tampung = []
            if i != 0:
                for j in range (ordo):
                    if j != 1:
                        tampung.append(matriks[i][j])
                    matriks_b.append(tampung)
    if len(matriks_c) != 3:
        for i in range (ordo):
            tampung = []
            if i != 0:
                for j in range (ordo):
                    if j != 2:
                        tampung.append(matriks[i][j])
                    matriks_c.append(tampung)
    if len(matriks_d) != 3:
        for i in range (ordo):
            tampung = []
            if i != 0:
                for j in range (ordo):
                    if j != 3:
                        tampung.append(matriks[i][j])
                    matriks_d.append(tampung)
    a = determinan2(matriks_a)
    b = determinan2(matriks_b)
    c = determinan2(matriks_c)
    d = determinan2(matriks_d)
    determinan_total = matriks[0][0]*a - matriks[0][1]*b\
        + matriks[0][2]*c - matriks[0][3]*d
    return determinan_total
def invers():
    matriks_inv=np.linalg.inv(matriks)
    print("\nHasil Invers Matriks:")
    print(matriks_inv)

print("=======PROGRAM OPERASI MATRIKS=======")
print("------------JENIS PROGRAM------------")
print("1.Penjumlahan Matriks")
print("2.Pengurangan Matriks")
print("3.Perkalian Matriks")
print("4.Determinan Matriks")
print("5.Invers Matriks")
print("=====================================")
operasi = int(input("Pilih Program:"))
pilihan = operasi
print("-------------------------------------")
ordo = int(input("Masukan Ordo:"))
print(" ")

if operasi != 5:
    print("============MATRIKS 1============")
    print("====Masukkan Nilai Matriks 1=====")
    matriks1= []
    for i in range(ordo):
        baris = []
        for j in range(ordo):
            print("Baris",i+1,"Kolom",j+1)
            nilai = int(input())
            baris.append(nilai)
        matriks1.append(baris)
    print("Maka nilai matriks 1 adalah :")
    for baris in matriks1:
        print("|\t", end="")
        for kolom in baris:
            print(kolom,"\t", end="")
        print("|")
        print("\n")

    print("============MATRIKS 2============")
    print("====Masukkan Nilai Matriks 2=====")
    matriks2 = []
    for i in range (ordo):
        baris = []
        for j in range (ordo):
            print("Baris", i+1,"Kolom", j+1)
            nilai = int(input())
            baris.append(nilai)
        matriks2.append(baris)
    print("Maka nilai matriks 2 adalah :")
    for baris in matriks2:
        print("|\t", end="")
        for kolom in baris:
            print(kolom,"\t", end="")
        print("|")
        print("\n")

if pilihan == 1:
    penjumlahan()
elif pilihan == 2:
    pengurangan()
elif pilihan == 3:
    perkalian(matriks1, matriks2)
elif operasi == 4:
    print("=============MATRIKS=============")
    print("Masukkan Nilai Matriks")
    matriks = []
    for i in range(ordo):
        baris = []
        for j in range(ordo):
            print("Baris",i+1,"Kolom",j+1)
            nilai = int(input())
            baris.append(nilai)
        matriks.append(baris)
    print("Nilai Matriks:")
    for baris in matriks:
        print("|\t", end="")
        for kolom in baris:
            print(kolom,"\t", end="")
        print("|")
    determinan()
elif operasi == 5:
    print("=============MATRIKS=============")
    print("Masukkan Nilai Matriks")
    matriks = []
    for i in range(ordo):
        baris = []
        for j in range(ordo):
            print("Baris",i+1,"Kolom",j+1)
            nilai = int(input())
            baris.append(nilai)
        matriks.append(baris)
    print("Nilai Matriks:")
    for baris in matriks:
        print("|\t", end="")
        for kolom in baris:
            print(kolom,"\t", end="")
        print("|")
    invers()