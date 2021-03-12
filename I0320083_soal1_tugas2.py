from math import pi

print("------------------------------------------------------------------------")
print("APLIKASI HITUNG CEPAT")
print("------------------------------------------------------------------------")

print ("Apakah yang ingin anda hitung?")
print ("1. luas persegi panjang")
print ("2. luas lingkaran")
print ("3. luas permukaan kubus")
print ("4. konversi suhu celcius ke farenheit")
print ("5. konversi suhu reamur ke kelvin")

cetak = 0
choice = input("Masukkan pilihan anda (1/2/3/4/5): ")

if choice == "1":
    print("luas persegi panjang")
    p=float(input("masukan panjang"))
    l=float(input("masukan lebar"))
    rumusPP=p*l
    print("luas persegi panjang tersebut adalah ",rumusPP)

elif choice == "2":
    print("luas lingkaran")
    r=float(input("masukan jari-jari"))
    rumusL=pi*r**2
    print("luas lingkaran tersebut adalah ",rumusL)

elif choice == "3":
    print("luas permukaan kubus")
    s=float(input("panjang sisi"))
    rumusK=s*s*6
    print("luas kubus tersebut adalah ",rumusK)

elif choice == "4":
    print("konversi suhu celcius ke farenheit")
    sc=float(input("suhu celcius"))
    rumusCF=(sc*9/5)+32
    print("konversi suhu celcius ke farenheit tersebut adalah ",rumusCF)

elif choice == "5":
    print("konversi suhu reamur ke kelvin")
    sr=float(input("suhu reamur"))
    rumusRK=(sr*5/4)+273
    print("konversi suhu reamur ke kelvin tersebut adalah ",rumusRK)

else :
    print("input tidak ditemukan")

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")