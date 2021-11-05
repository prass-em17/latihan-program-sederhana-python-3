#time
from os import system
from platform import system as FungsiBersih   
from time import localtime
import time
import datetime
waktu = datetime.datetime.now()
#print(x.year)(x.month)(x.day)(x.hour)(x.minute)(x.microsecond)
#print(x.strftime("%H"))
kalen = waktu.strftime("\n[ D A T E : %D ]   [ T I M E : %H:%M:%S ]")
jam = int(waktu.strftime("%H"))
 
#clear system
if FungsiBersih() == "Windows":
    bersih = "cls"
elif FungsiBersih() == "Linux":
    bersih = "clear"
    
#database
user = {"uname":{0:"Yoongi",1:"Daniel"}, "pin":{0:"1803",1:"1212"},
        "umur":{0:{},1:{}}, "money":{0:3000000,1:2000000}, "star":{0:0,1:0}}
blnj = {"storage":{0:"Album BE",1:"Album MOTS 7",2:"Album WINGS",3:"Summer Vacation Photobook",
                   4:"Concert Special Photobook",5:"Behind The Scene Photobook"}}
kdvoucher = {"voucher":"HOT100", "diskon":"10%", "status":"Belum Digunakan",
             "kesempatan":1,"kondisi":True}
 
#bagian akun-login-buat-dll
def check_time(this_jam,that_menit): 
    jam_menuju_menit = this_jam * 60 
    pukul = jam_menuju_menit + that_menit
    return pukul

def main_menu():
    system(bersih)
    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
    print("                Selamat Datang di                ")
    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")  
    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
    pilihan = int(input("1.Sign Up\n2.Login\n3.Check Akun Terdaftar\n4.Keluar\n\n>> "))
    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
    if pilihan == 1:
        signup()
    elif pilihan == 2:
        login()
    elif pilihan == 3:
        cekdata()
    elif pilihan == 4:
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("         Terimakasih Telah Bertransaksi di ")
        print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        exit()
    else:
        quit()

def signup():
    system("cls")
    print("                 Silahkan Sign Up ")
    sign_nama = input(">> Masukkan Nama : ")
    user["uname"][len(user["uname"])] = sign_nama
    sign_pin = int(input(">> Masukkan Pin : "))
    user["pin"][len(user["pin"])] = sign_pin
    sign_topup = int(input(">> Masukkan Jumlah Top Up : "))
    user["money"][len(user["money"])] = sign_topup
    user["star"][len(user["star"])] = 0
    system("cls")
    print("\nSelamat! Akunmu Telah Terdaftar! \nSilahkan Lanjutkan Ke Menu Login!\n ")
    main_menu() 

def login():
    lagi = "ya"
    while (lagi == "ya"):
        system("cls")
        print(kalen)
        uname = str(input("\n >> Masukkan Usernamemu : "))
        #user["uname"][len(user["uname"])] = uname
        pin = str(input(" >> Masukkan PINmu : "))
        #user["pin"][len(user["pin"])] = pin
        for i in range(0,len(user["uname"])):
            if uname == user["uname"][i] and pin == user["pin"][i]:
                for j in range(0,3):
                    system("cls")
                    if (j % 2) == 1:
                        print("     loading bentar......<<<")
                    else:
                        print("     loading bentar......>>>")
                    time.sleep(0.5)
                system("cls")   
                print("            Ｋａｍｕ Ｂｅｒｈａｓｉｌ Ｌｏｇｉｎ")
                break
            elif i >= len(user["uname"]) and len(user["pin"]):
                system("cls")
                print("            Ｍａａｆ Ｐｉｎ Ｋａｍｕ Ｓａｌａｈ ")
                lagi = input("Apakah Kamu Ingin Melakukan Login Ulang? ya/tidak | ")
                if lagi == "ya":
                    continue
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
        umur = int(input(" >> Masukkan Umurmu : "))
        user["umur"][len(user["umur"])] = umur
        system(bersih)
        menu_login(umur,i)

def cekdata():
    system("cls")
    print("                  Hai Admin!")
    print("          Data Akun Telah Terdaftar di")
    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
    print("\nData Username ->",user["uname"])
    print("\nData Pin ->",user["pin"])
    print("\nData Uang ->",user["money"])
    print("\nData Star ->",user["star"])
    print("\n\ntekan enter untuk lanjut......")
    input()
    main_menu()

def panggilan(umur):
    if umur >= int(8) and umur <= int(18):
        level = "Dek"
    elif umur >= int(19) and umur <= int(25):
        level = "Kak"
    elif umur >= int(26) and umur <= int(60):
        level = "Pak/Bu"
    return level        

def menu_login(umur,i):
    lagi1 = "ya"
    while (lagi1 == "ya"):
        system("cls")
        level = panggilan(umur)
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        if jam >= int(00) and jam <= int(10):
            print("            Selamat Pagi", level, user["uname"][i])
        elif jam >= int(10) and jam <= int(14):
            print("            Selamat Siang", level, user["uname"][i])
        elif jam >= int(15) and jam <= int(18):
            print("            Selamat Sore", level, user["uname"][i])
        elif jam >= int(19) and jam <= int(24):
            print("            Selamat Malam", level, user["uname"][i])
        print("                 Halo",level,user["uname"][i]              )
        print("                Selamat Datang di                ")
        print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")  
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print(" >> Sisa Saldo Kamu = ","Rp.", user["money"][i])
        print(" >> Sisa Star Kamu  = ", user["star"][i])
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("     DAPATKAN DISKON 10% UNTUK PEMBELIAN STAR!!! ")
        print("         KODE VOUCHER NYA ADALAH HOT100 ")
        print(" HANYA BERLAKU 1X PEMAKAIAN DAN 10 MENIT SETELAH LOGIN\n ")
        print("  §.•´¨'°÷•..×   🎀  𝑀 𝐸 𝒩 𝒰  🎀   ×..•÷°'¨´•.§ ")
        print(" (1.) Edit Data ")
        print(" (2.) Beli Star ")
        print(" (3.) Beli Album ")
        print(" (4.) Beli Photobook ")
        print(" (5.) Keluar ")
        print("     §.•´¨'°÷•..×  §.•´¨'°÷•..×  §.•´¨'°÷•..× ")
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=\n")
        pilihan = input(" >> Masukkan Pilihanmu : ")
        if (pilihan == "1"):
            ubah_data(i)
            lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
            if lagi == "ya":
                pass
            elif lagi == "tidak":
                print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                print("         Terimakasih Telah Bertransaksi di ")
                print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                exit()
        elif (pilihan == "2"):
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
            print("     DAPATKAN DISKON 10% UNTUK PEMBELIAN STAR!!! ")
            print("         KODE VOUCHER NYA ADALAH HOT100 ")
            print(" HANYA BERLAKU 1X PEMAKAIAN DAN 10 MENIT SETELAH LOGIN ")
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
            print(" <<<<<<<<<<<<<<<<<<<    M E N U   >>>>>>>>>>>>>>>>>>>")
            print(" (1.) Beli 1000 Star Rp. 150.000 ")
            print(" (2.) Beli 3000 Star Rp. 400.000 ")
            print(" (3.) Beli 5000 Star Rp. 600.000 ")
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=\n")
            pilihan = input(" >> Masukkan Pilihanmu : ")
            if (pilihan == "1"):
                beli_star_1000(level,i)
                lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
                if lagi == "ya":
                    pass
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
            elif (pilihan == "2") :
                beli_star_3000(level,i)
                lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
                if lagi == "ya":
                    pass
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
            elif (pilihan == "3"):
                beli_star_5000(level,i)
                lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
                if lagi == "ya":
                    pass
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
            else :
                print("   Maaf Tidak Ada Pilihan Tersedia")
                lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
                if lagi == "ya":
                    pass
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
        elif (pilihan == "3"):
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
            print(" <<<<<<<<<<<<<<<<<<<    M E N U   >>>>>>>>>>>>>>>>>>>")
            print(" (1.) Beli Album BE 3000 Star")
            print(" (2.) Beli Album MOTS 7 2200 Star")
            print(" (3.) Beli Album WINGS 2000 Star")
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=\n")
            pilihan = input(" >> Masukkan Pilihanmu : ")
            if (pilihan == "1"):
                beli_album_BE(level,i)
                lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
                if lagi == "ya":
                    pass
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
            elif (pilihan == "2"):
                beli_album_MOTS(level,i)
                lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
                if lagi == "ya":
                    pass
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
            elif (pilihan == "3"):
                beli_album_WINGS(level,i)
                lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
                if lagi == "ya":
                    pass
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
            else :
                print("   Maaf Tidak Ada Pilihan Tersedia")
                lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
                if lagi == "ya":
                    pass
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
        elif (pilihan == "4"):
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
            print(" <<<<<<<<<<<<<<<<<<<    M E N U   >>>>>>>>>>>>>>>>>>>")
            print(" (1.) Beli Summer Vacation Photobook 1200 Star")
            print(" (2.) Beli Concert Special Photobook 1800 Star")
            print(" (3.) Beli Behind The Scene Photobook 1000 Star")
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=\n")
            pilihan = input(" >> Masukkan Pilihanmu : ")
            if (pilihan == "1"):
                beli_summer(level,i)
                lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
                if lagi == "ya":
                    pass
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
            elif (pilihan == "2"):
                beli_concert(level,i)
                lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
                if lagi == "ya":
                    pass
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
            elif (pilihan == "3"):
                beli_bts(level,i)
                lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
                if lagi == "ya":
                    pass
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
            else :
                print("   Maaf Tidak Ada Pilihan Tersedia")
                lagi = input(" Apakah Kamu Mau Coba Lagi? ya/tidak | ")
                if lagi == "ya":
                    pass
                elif lagi == "tidak":
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    print("         Terimakasih Telah Bertransaksi di ")
                    print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                    print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                    exit()
        elif (pilihan == "5"):
                print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                print("         Terimakasih Telah Bertransaksi di ")
                print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                exit()
        else :
            print("   Maaf Tidak Ada Pilihan Tersedia")
            lagi = input("Apakah Kamu Ingin Melakukan Transaksi Ulang? ya/tidak | ")
            if lagi == "ya":
                pass
            elif lagi == "tidak":
                print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                print("         Terimakasih Telah Bertransaksi di ")
                print("        :⋆  🎀  𝒮𝑒𝓇𝑒𝓃𝒹𝒾𝓅𝒾𝓉𝓎 𝒮𝓉🌞𝓇𝑒  🎀  ⋆: ")   
                print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
                exit() 

def ubah_data(i):
    user["uname"][i] = input(" >> Masukkan Namamu : ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("       Nama Kamu Telah Berubah Menjadi", user["uname"][i])
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    user["pin"][i] = input(" >> Masukkan PINmu : ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("       PIN Kamu Telah Berubah Menjadi", user["pin"][i])
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("tekan enter untuk melanjutkan")
    input()
    login()

#ini bagian belinya
def beli_star_1000(level,i):
    if int(user["money"][i] < 149999):
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("              Maaf Uang Kamu Enggak Cukup")
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
    else :
        batas_menit = 10
        batas_voucher = (localtime()[3]*60)+localtime()[4] + batas_menit
        input_voucher = str(input("Apa Kamu Punya Kode Voucher Discount? Jika Ya Masukkan Kode Voucher : "))
        if kdvoucher["kondisi"] == True and input_voucher == kdvoucher["voucher"] and check_time(localtime()[3],localtime()[4]) < batas_voucher and kdvoucher["kesempatan"] >= 1:
            system("cls")
            kdvoucher["kondisi"] == False
            print("Selamat! Kamu Mendapatkan Diskon 10% \n")
            print("Selamat Datang", level, user["uname"][i])
            print ("Catatan : Voucher hanya berlaku 10 Menit Setelah Anda Login")
            kdvoucher["Status"] = "Sudah Digunakan"
            kurang = kdvoucher["kesempatan"] - 1
            kdvoucher["kesempatan"] = kurang
            harga = 150000
            diskon = int(harga * (10/100))
            total_harga = harga - int(diskon)
            beli = int(user["money"][i])- int(total_harga)
            user["money"][i] = beli
            topup = int(user["star"][i])+1000
            user["star"][i] = topup
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
            print("          𝓢𝓮𝓵𝓪𝓶𝓪𝓽! 𝓣𝓻𝓪𝓷𝓼𝓪𝓴𝓼𝓲 𝓚𝓪𝓶𝓾 𝓑𝓮𝓻𝓱𝓪𝓼𝓲𝓵 ")
            print(" >> Sisa Saldo Kamu = ","Rp.",beli)
            print(" >> Sisa Star Kamu  = ", user["star"][i])
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")

        else :
            print ("\nMaaf Kode Voucher Tidak Dapat Digunakan/Telah Hangus")
            print("Selamat Datang", level, user["uname"][i])
            beli = int(user["money"][i])-150000
            user["money"][i] = beli
            topup = int(user["star"][i])+1000
            user["star"][i] = topup
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
            print("          𝓢𝓮𝓵𝓪𝓶𝓪𝓽! 𝓣𝓻𝓪𝓷𝓼𝓪𝓴𝓼𝓲 𝓚𝓪𝓶𝓾 𝓑𝓮𝓻𝓱𝓪𝓼𝓲𝓵 ")
            print(" >> Sisa Saldo Kamu = ","Rp.", user["money"][i])
            print(" >> Sisa Star Kamu  = ", user["star"][i])
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
 
def beli_star_3000(level,i):
    if int(user["money"][i] < 100000):
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("              Maaf Uang Kamu Enggak Cukup")
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
    else :
        batas_menit = 10
        batas_voucher = (localtime()[3]*60)+localtime()[4] + batas_menit
        input_voucher = str(input("Apa Kamu Punya Kode Voucher Discount? Jika Ya Masukkan Kode Voucher : "))
        if kdvoucher["kondisi"] == True and input_voucher == kdvoucher["voucher"] and check_time(localtime()[3],localtime()[4]) < batas_voucher and kdvoucher["kesempatan"] >= 1:
            system("cls")
            kdvoucher["kondisi"] == False
            print("\nSelamat! Kamu Mendapatkan Diskon 10%")
            print("Selamat Datang", level, user["uname"][i])
            print ("Catatan : Voucher hanya berlaku 10 Menit Setelah Anda Login")
            kdvoucher["Status"] = "Sudah Digunakan"
            kurang = kdvoucher["kesempatan"] - 1
            kdvoucher["kesempatan"] = kurang
            harga = 400000
            diskon = int(harga * (10/100))
            total_harga = harga - int(diskon)
            beli = int(user["money"][i])- int(total_harga)
            user["money"][i] = beli
            topup = int(user["star"][i])+3000
            user["star"][i] = topup
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
            print("          𝓢𝓮𝓵𝓪𝓶𝓪𝓽! 𝓣𝓻𝓪𝓷𝓼𝓪𝓴𝓼𝓲 𝓚𝓪𝓶𝓾 𝓑𝓮𝓻𝓱𝓪𝓼𝓲𝓵 ")
            print(" >> Sisa Saldo Kamu = ","Rp.",beli)
            print(" >> Sisa Star Kamu  = ", user["star"][i])
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        else :
            print ("\nMaaf Kode Voucher Tidak Dapat Digunakan/Telah Hangus")
            print("Selamat Datang", level, user["uname"][i])
            beli = int(user["money"][i])-400000
            user["money"][i] = beli
            topup = int(user["star"][i])+3000
            user["star"][i] = topup
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
            print("          𝓢𝓮𝓵𝓪𝓶𝓪𝓽! 𝓣𝓻𝓪𝓷𝓼𝓪𝓴𝓼𝓲 𝓚𝓪𝓶𝓾 𝓑𝓮𝓻𝓱𝓪𝓼𝓲𝓵 ")
            print(" >> Sisa Saldo Kamu = ","Rp.", user["money"][i])
            print(" >> Sisa Star Kamu  = ", user["star"][i])
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
 
def beli_star_5000(level,i):
    if int(user["money"][i] < 500000):
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("              Maaf Uang Kamu Enggak Cukup")
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
    else :
        batas_menit = 10
        batas_voucher = (localtime()[3]*60)+localtime()[4] + batas_menit
        input_voucher = str(input("Apa Kamu Punya Kode Voucher Discount? Jika Ya Masukkan Kode Voucher : "))
        if kdvoucher["kondisi"] == True and input_voucher == kdvoucher["voucher"] and check_time(localtime()[3],localtime()[4]) < batas_voucher and kdvoucher["kesempatan"] >= 1:
            system("cls")
            kdvoucher["kondisi"] == False
            print("\nSelamat! Kamu Mendapatkan Diskon 10%")
            print("Selamat Datang", level, user["uname"][i])
            print ("Catatan : Voucher hanya berlaku 10 Menit Setelah Anda Login")
            kdvoucher["Status"] = "Sudah Digunakan"
            kurang = kdvoucher["kesempatan"] - 1
            kdvoucher["kesempatan"] = kurang
            harga = 600000
            diskon = int(harga * (10/100))
            total_harga = harga - int(diskon)
            beli = int(user["money"][i])- int(total_harga)
            user["money"][i] = beli
            topup = int(user["star"][i])+5000
            user["star"][i] = topup
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
            print("          𝓢𝓮𝓵𝓪𝓶𝓪𝓽! 𝓣𝓻𝓪𝓷𝓼𝓪𝓴𝓼𝓲 𝓚𝓪𝓶𝓾 𝓑𝓮𝓻𝓱𝓪𝓼𝓲𝓵 ")
            print(" >> Sisa Saldo Kamu = ","Rp.",beli)
            print(" >> Sisa Star Kamu  = ", user["star"][i])
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        else :
            print ("\nMaaf Kode Voucher Tidak Dapat Digunakan/Telah Hangus")
            print("Selamat Datang", level, user["uname"][i])
            beli = int(user["money"][i])-600000
            user["money"][i] = beli
            topup = int(user["star"][i])+5000
            user["star"][i] = topup
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
            print("          𝓢𝓮𝓵𝓪𝓶𝓪𝓽! 𝓣𝓻𝓪𝓷𝓼𝓪𝓴𝓼𝓲 𝓚𝓪𝓶𝓾 𝓑𝓮𝓻𝓱𝓪𝓼𝓲𝓵 ")
            print(" >> Sisa Saldo Kamu = ","Rp.", user["money"][i])
            print(" >> Sisa Star Kamu  = ", user["star"][i])
            print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
 
def beli_album_BE(level,i):
    if int(user["star"][i] < 1999):
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("              Maaf Star Kamu Engga Cukup")
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
    else :
        print("Selamat Datang", level, user["uname"][i])
        beli = int(user["star"][i]) - 3000
        user["star"][i] = beli
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("      𝓢𝓮𝓵𝓪𝓶𝓪𝓽! 𝓚𝓪𝓶𝓾 𝓑𝓮𝓻𝓱𝓪𝓼𝓲𝓵 𝓜𝓮𝓶𝓫𝓮𝓵𝓲 𝓐𝓵𝓫𝓾𝓶 𝓑𝓔 ") 
        print(" >> Sisa Saldo Kamu = ","Rp.", user["money"][i])
        print(" >> Sisa Star Kamu  = ", user["star"][i])
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
 
def beli_album_MOTS(level,i):
    if int(user["star"][i] < 1999):
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("              Maaf Star Kamu Engga Cukup")
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
    else :
        print("Selamat Datang", level, user["uname"][i])
        beli = int(user["star"][i]) - 2200
        user["star"][i] = beli
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("   𝓢𝓮𝓵𝓪𝓶𝓪𝓽! 𝓚𝓪𝓶𝓾 𝓑𝓮𝓻𝓱𝓪𝓼𝓲𝓵 𝓜𝓮𝓶𝓫𝓮𝓵𝓲 𝓐𝓵𝓫𝓾𝓶 𝓜𝓞𝓣𝓢 7 ")  
        print(" >> Sisa Saldo Kamu = ","Rp.", user["money"][i])
        print(" >> Sisa Star Kamu  = ", user["star"][i])
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
 
def beli_album_WINGS(level,i):
    if int(user["star"][i] < 1999):
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("              Maaf Star Kamu Engga Cukup")
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
    else :
        print("Selamat Datang", level, user["uname"][i])
        beli = int(user["star"][i]) - 2000
        user["star"][i] = beli
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("    𝓢𝓮𝓵𝓪𝓶𝓪𝓽! 𝓚𝓪𝓶𝓾 𝓑𝓮𝓻𝓱𝓪𝓼𝓲𝓵 𝓜𝓮𝓶𝓫𝓮𝓵𝓲 𝓐𝓵𝓫𝓾𝓶 𝓦𝓘𝓝𝓖𝓢  ")
        print(" >> Sisa Saldo Kamu = ","Rp.", user["money"][i])
        print(" >> Sisa Star Kamu  = ", user["star"][i])
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
 
def beli_summer(level,i):
    if int(user["star"][i] < 999):
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("              Maaf Star Kamu Engga Cukup")
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
    else :
        print("Selamat Datang", level, user["uname"][i])
        beli = int(user["star"][i]) - 1200
        user["star"][i] = beli
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("   𝓢𝓮𝓵𝓪𝓶𝓪𝓽! 𝓚𝓪𝓶𝓾 𝓑𝓮𝓻𝓱𝓪𝓼𝓲𝓵 𝓜𝓮𝓶𝓫𝓮𝓵𝓲 𝓢𝓾𝓶𝓶𝓮𝓻 𝓥𝓪𝓬𝓪𝓽𝓲𝓸𝓷 𝓟𝓱𝓸𝓽𝓸𝓫𝓸𝓸𝓴 ")
        print(" >> Sisa Saldo Kamu = ","Rp.", user["money"][i])
        print(" >> Sisa Star Kamu  = ", user["star"][i])
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
 
def beli_concert(level,i):
    if int(user["star"][i] < 999):
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("              Maaf Star Kamu Engga Cukup")
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
    else :
        print("Selamat Datang", level, user["uname"][i])
        beli = int(user["star"][i]) - 1800
        user["star"][i] = beli
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("   𝓢𝓮𝓵𝓪𝓶𝓪𝓽! 𝓚𝓪𝓶𝓾 𝓑𝓮𝓻𝓱𝓪𝓼𝓲𝓵 𝓜𝓮𝓶𝓫𝓮𝓵𝓲 𝓒𝓸𝓷𝓬𝓮𝓻𝓽 𝓢𝓹𝓮𝓬𝓲𝓪𝓵 𝓟𝓱𝓸𝓽𝓸𝓫𝓸𝓸𝓴 ")
        print(" >> Sisa Saldo Kamu = ","Rp.", user["money"][i])
        print(" >> Sisa Star Kamu  = ", user["star"][i])
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
 
def beli_bts(level,i):
    if int(user["star"][i] < 999):
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("              Maaf Star Kamu Engga Cukup")
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
    else :
        print("Selamat Datang", level, user["uname"][i])
        beli = int(user["star"][i]) - 1000
        user["star"][i] = beli
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("   𝓢𝓮𝓵𝓪𝓶𝓪𝓽! 𝓚𝓪𝓶𝓾 𝓑𝓮𝓻𝓱𝓪𝓼𝓲𝓵 𝓜𝓮𝓶𝓫𝓮𝓵𝓲 𝓑𝓮𝓱𝓲𝓷𝓭 𝓣𝓱𝓮 𝓢𝓬𝓮𝓷𝓮 𝓟𝓱𝓸𝓽𝓸𝓫𝓸𝓸𝓴 ")
        print(" >> Sisa Saldo Kamu = ","Rp.", user["money"][i])
        print(" >> Sisa Star Kamu  = ", user["star"][i])
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")

#mainprogram
main_menu()
