import sys
from itertools import islice

insert = lambda _dict, obj, pos: {k: v for k, v in (list(_dict.items())[:pos] + list(obj.items()) + list(_dict.items())[pos:])}

menu = {
    "makanan" : {"nasi goreng" : 18000,"mie goreng" : 22000, "lontong sayur" : 17000},
    "minuman" : {"teh es" : 6000, "teh hangat" : 6000, "jeruk es" : 8000, "jeruk hangat" : 8000, "air mineral" : 5000}
}

def hapus_menu() :
    print ("|=======================================================|")
    print ("|Apakah anda ingin menghapus menu makanan atau minuman ?|")
    x = input("|ketik \"makanan\" atau \"minuman\" = ")
    while x != "keluar" :
        if x == "makanan" :
            print ("|=======================================================|")
            print ("|Berikut daftar makanan yang sekarang tersedia :")
            print ("=================================================================")
            print (*["|" + str(k) + " : " + str(v) for k,v in menu["makanan"].items()],sep= "\n")
            print ("=================================================================")
            print ("|Silahkan pilih dengan angka, menu apa yang ingin dihapus(conth : 1(untuk urutan pertama))|")
            while x1 != "keluar" :
                if x1 == 1 :
                    menu["makanan"].pop("nasi goreng")
                    print ("=================================================================")
                    print (*["|" + str(k) + " : " + str(v) for k,v in menu["makanan"].items()],sep= "\n")
                    print ("=================================================================")
                    print ("|Apakah anda ingin menghapus menu makanan lain? |")
                    x1 = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                    if x1 == "ya" :
                        hapus_menu()
                    elif x1 == "keluar" :
                        lihat_menu()
                elif x1 == 2 :
                    menu["makanan"].pop("mie goreng")
                    print ("=================================================================")
                    print (*["|" + str(k) + " : " + str(v) for k,v in menu["makanan"].items()],sep= "\n")
                    print ("=================================================================")
                    print ("|Apakah anda ingin menghapus menu makanan lain? |")
                    x1 = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                    if x1 == "ya" :
                        hapus_menu()
                    elif x1 == "keluar" :
                        lihat_menu()
                elif x1 == 3 :
                    menu["makanan"].pop("nasi goreng")
                    print ("=================================================================")
                    print (*["|" + str(k) + " : " + str(v) for k,v in menu["makanan"].items()],sep= "\n")
                    print ("=================================================================")
                    print ("|Apakah anda ingin menghapus menu makanan lain? |")
                    x1 = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                    if x1 == "ya" :
                        hapus_menu()
                    elif x1 == "keluar" :
                        lihat_menu()
                elif x1 == "keluar" or x1 == 4 :
                    lihat_menu()
                else :
                    print ("error, perintah yang anda masukkan tidak terdaftar, dimohon ketik sesuai dengan perintah di atas !|")
                    x1 = input("|Silahkan ketik ulang disini = ")
        elif x == "minuman" :
            print ("|=======================================================|")
            print ("|Berikut daftar minuman yang sekarang tersedia :")
            print ("=================================================================")
            print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
            print ("=================================================================")
            print ("|Silahkan pilih dengan angka, menu apa yang ingin dihapus(conth : 1(untuk urutan pertama))|")
            x1 = int(input("|Ketik pilihan anda disini = "))
            while x1 != "keluar" :
                if x1 == 1 :
                    menu["minuman"].pop("teh es")
                    print ("=================================================================")
                    print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
                    print ("=================================================================")
                    print ("|Apakah anda ingin menghapus menu minuman lain ? |")
                    x1 = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                    if x1 == "ya" :
                        hapus_menu()
                    elif x1 == "keluar" :
                        lihat_menu()
                elif x1 == 2 :
                    menu["minuman"].pop("teh hangat")
                    print ("=================================================================")
                    print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
                    print ("=================================================================")
                    print ("|Apakah anda ingin menghapus menu minuman lain ? |")
                    x1 = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                    if x1 == "ya" :
                        hapus_menu()
                    elif x1 == "keluar" :
                        lihat_menu()
                elif x1 == 3 :
                    menu["minuman"].pop("jeruk es")
                    print ("=================================================================")
                    print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
                    print ("=================================================================")
                    print ("|Apakah anda ingin menghapus menu minuman lain ? |")
                    x1 = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                    if x1 == "ya" :
                        hapus_menu()
                    elif x1 == "keluar" :
                        lihat_menu()
                elif x1 == 4 :
                    menu["minuman"].pop("jeruk hangat")
                    print ("=================================================================")
                    print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
                    print ("=================================================================")
                    print ("|Apakah anda ingin menghapus menu minuman lain ? |")
                    x1 = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                    if x1 == "ya" :
                        hapus_menu()
                    elif x1 == "keluar" :
                        lihat_menu
                elif x1 == 5 :
                    menu["minuman"].pop("air mineral")
                    print ("=================================================================")
                    print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
                    print ("=================================================================")
                    print ("|Apakah anda ingin menghapus menu minuman lain ? |")
                    x1 = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                    if x1 == "ya" :
                        hapus_menu()
                    elif x1 == "keluar" :
                        lihat_menu()
                elif x1 == 6 or x1 == "keluar" :
                    lihat_menu()
                else :
                    print ("error, perintah yang anda masukkan tidak terdaftar, dimohon ketik sesuai dengan perintah di atas !|")
                    x1 = input("|Silahkan ketik ulang disini = ")
        else :
            print ("error, perintah yang anda masukkan tidak terdaftar, dimohon ketik sesuai dengan perintah di atas !|")
            x = input("|Silahkan ketik ulang disini = ")

def tambah_menu() :
    print ("|=========================================================|")
    print ("|Apakah anda ingin menambahkan menu makanan atau minuman ?|")
    x = input("|ketik \"makanan\" atau \"minuman\" = ")
    while x != "keluar" :
        if x == "makanan" :
            print ("|=======================================================================|")
            x2 = input("|Silahkan ketik menu makanan yang anda ingin tambah disini = ")
            x3 = int(input("|Silahkan ketik harga menu makanan tersebut disini = "))
            menu["makanan"][x2] = x3
            print ("=================================================================")
            print (*["|" + str(k) + " : " + str(v) for k,v in menu["makanan"].items()],sep= "\n")
            print ("=================================================================")
            print ("|Apakah anda ingin menambah menu makanan lain? |")
            x = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
            if x == "ya" :
                tambah_menu()
            elif x == "keluar" :
                lihat_menu()
            else :
                print ("error, perintah yang anda masukkan tidak terdaftar, dimohon ketik sesuai dengan perintah di atas !|")
                x = input("|Silahkan ketik ulang disini = ")
        elif x == "minuman" :
            print ("|=======================================================================|")
            x2 = input("|Silahkan ketik menu minuman yang anda ingin tambah disini = ")
            x3 = int(input("|Silahkan ketik harga menu minuman tersebut disini = "))
            menu["minuman"][x2] = x3
            print ("=================================================================")
            print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
            print ("=================================================================")
            print ("|Apakah anda ingin menambah menu minuman lain? |")
            x = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
            if x == "ya" :
                tambah_menu()
            elif x == "keluar" :
                lihat_menu()
            else :
                print ("error, perintah yang anda masukkan tidak terdaftar, dimohon ketik sesuai dengan perintah di atas !|")
                x = input("|Silahkan ketik ulang disini = ")
        else :
            print ("|error, dimohon ketik sesuai dengan perintah ! |")
            x = input("|Silahkan ketik disini")

def ganti_menu() :
    print ("|=========================================================|")
    print ("|=Apakah anda ingin mengganti menu makanan atau minuman ?=|")
    x = input("|Silahkan ketik disini = ")
    if x == "makanan" :
        print ("|=======================================================|")
        print ("|Berikut daftar makanan yang sekarang tersedia :")
        print ("=================================================================")
        print (*["|" + str(k) + " : " + str(v) for k,v in menu["makanan"].items()],sep= "\n")
        print ("=================================================================")
        print ("|Silahkan pilih dengan angka, menu apa yang ingin diganti(conth : 1(untuk urutan pertama))|")
        x1 = int(input("|Silahkan ketik disini = "))
        while x1 != 0 :
            if x1 == 1 :
                print ("|=======================================================|")  
                x3 = input("|Silahkan ketik nama makanan yang akan menggantikan = ")
                x4 = input("|Silahkan ketik harga makanan yang menggantikan = ") 
                del menu["makanan"][next(islice(menu["makanan"],0,None))]
                menu["makanan"] = insert(menu["makanan"],{x3 : x4}, 0)
                print ("=================================================================")
                print (*["|" + str(k) + " : " + str(v) for k,v in menu["makanan"].items()],sep= "\n")
                print ("=================================================================")
                print ("|Apakah anda ingin mengganti menu makanan lain?")
                x = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                if x == "ya" :
                    ganti_menu()
                elif x == "keluar" :
                    lihat_menu()
            elif x1 == 2 :
                print ("|=======================================================|")  
                x3 = input("|Silahkan ketik nama makanan yang akan menggantikan = ")
                x4 = input("|Silahkan ketik harga makanan yang menggantikan = ")
                del menu["makanan"][next(islice(menu["makanan"],1,None))]
                menu["makanan"] = insert(menu["makanan"],{x3 : x4}, 1)
                print ("=================================================================")
                print (*["|" + str(k) + " : " + str(v) for k,v in menu["makanan"].items()],sep= "\n")
                print ("=================================================================")
                print ("|Apakah anda ingin mengganti menu makanan lain?")
                x = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                if x == "ya" :
                    ganti_menu()
                elif x == "keluar" :
                    lihat_menu()
            elif x1 == 3 :
                print ("|=======================================================|")  
                x3 = input("|Silahkan ketik nama makanan yang akan menggantikan = ")
                x4 = input("|Silahkan ketik harga makanan yang menggantikan = ")
                del menu["makanan"][next(islice(menu["makanan"],2,None))]
                menu["makanan"] = insert(menu["makanan"],{x3 : x4}, 2)
                print ("=================================================================")
                print (*["|" + str(k) + " : " + str(v) for k,v in menu["makanan"].items()],sep= "\n")
                print ("=================================================================")
                print ("|Apakah anda ingin mengganti menu makanan lain?")
                x = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                if x == "ya" :
                    ganti_menu()
                elif x == "keluar" :
                    lihat_menu()
            elif x1 == 4 :
                lihat_menu()
            else :
                print ("error, perintah yang anda masukkan tidak terdaftar, dimohon ketik sesuai dengan perintah di atas !|")
                x1 = input("|Silahkan ketik ulang disini = ")
    elif x == "minuman" :
        print ("|=======================================================|")
        print ("|Berikut daftar minuman yang sekarang tersedia :")
        print ("=================================================================")
        print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
        print ("=================================================================")
        print ("|Silahkan pilih dengan angka, menu apa yang ingin diganti(contoh : 1 (untuk urutan pertama))|")
        x1 = int(input("|Silahkan ketik disini = "))
        while x1 != 0 :
            if x1 == 1 :
                print ("|=======================================================|")  
                x3 = input("|Silahkan ketik nama minuman yang akan menggantikan = ")
                x4 = input("|Silahkan ketik harga minuman yang menggantikan = ") 
                menu["minuman"].pop("teh es")
                temp_dict = {}
                temp_dict.update({x3 : x4})
                menu["minuman"] = {**temp_dict,**menu["minuman"]}
                print ("=================================================================")
                print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
                print ("=================================================================")
                print ("|Apakah anda ingin mengganti menu minuman lain?")
                x = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                if x == "ya" :
                    ganti_menu()
                elif x == "keluar" :
                    lihat_menu()
            elif x1 == 2 :
                print ("|=======================================================|")  
                x3 = input("|Silahkan ketik nama minuman yang akan menggantikan = ")
                x4 = input("|Silahkan ketik harga minuman yang menggantikan = ")
                del menu["minuman"][next(islice(menu["minuman"],1,None))]
                menu["minuman"] = insert(menu["minuman"],{x3 : x4}, 1)
                print ("=================================================================")
                print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
                print ("=================================================================")
                print ("|Apakah anda ingin mengganti menu minuman lain?")
                x = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                if x == "ya" :
                    ganti_menu()
                elif x == "keluar" :
                    lihat_menu()
            elif x1 == 3 :
                print ("|=======================================================|")  
                x3 = input("|Silahkan ketik nama minuman yang akan menggantikan = ")
                x4 = input("|Silahkan ketik harga minuman yang menggantikan = ")
                del menu["minuman"][next(islice(menu["minuman"],2,None))]
                menu["minuman"] = insert(menu["minuman"],{x3 : x4}, 2)
                print ("=================================================================")
                print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
                print ("=================================================================")
                print ("|Apakah anda ingin mengganti menu minuman lain?")
                x = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                if x == "ya" :
                    ganti_menu()
                elif x == "keluar" :
                    lihat_menu()
            elif x1 == 4 :
                print ("|=======================================================|")  
                x3 = input("|Silahkan ketik nama minuman yang akan menggantikan = ")
                x4 = input("|Silahkan ketik harga minuman yang menggantikan = ")
                del menu["minuman"][next(islice(menu["minuman"],3,None))]
                menu["minuman"] = insert(menu["minuman"],{x3 : x4}, 3)
                print ("=================================================================")
                print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
                print ("=================================================================")
                print ("|Apakah anda ingin mengganti menu minuman lain?")
                x = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                if x == "ya" :
                    ganti_menu()
                elif x == "keluar" :
                    lihat_menu()
            elif x1 == 5 :
                print ("|=======================================================|")  
                x3 = input("|Silahkan ketik nama minuman yang akan menggantikan = ")
                x4 = input("|Silahkan ketik harga minuman yang menggantikan = ")
                del menu["minuman"][next(islice(menu["minuman"],4,None))]
                menu["minuman"] = insert(menu["minuman"],{x3 : x4}, 4)
                print ("=================================================================")
                print (*["|" + str(k) + " : " + str(v) for k,v in menu["minuman"].items()],sep= "\n")
                print ("=================================================================")
                print ("|Apakah anda ingin mengganti menu minuman lain?")
                x = input("|\"ya\" untuk lanjut atau \"keluar\" untuk kembali ke menu utama = ")
                if x == "ya" :
                    ganti_menu()
                elif x == "keluar" :
                    lihat_menu()
            elif x1 == 6 or x1 == "keluar" :
                lihat_menu()
            else :
                print ("error, perintah yang anda masukkan tidak terdaftar, dimohon ketik sesuai dengan perintah di atas !|")
                x1 = input("|Silahkan ketik ulang disini = ")
    else :
        print ("|error, dimohon ketik sesuai dengan perintah ! |")
        x = input("|Silahkan ketik disini = ")

def lihat_menu() :
    print ("|===============================================================================================================|")  
    for x in menu :
        print (*["|" + str(k) + " : " + str(v) for k,v in menu.items()],sep="\n")
        break
    print ("|===============================================================================================================|")
    print ("|Apa yang anda ingin lakukan = ?")
    print ("|a. \"tambah\" untuk menambahkan menu baru pada menu  |")
    print ("|b. \"hapus\" untuk menghapus menu makanan            |") 
    print ("|c. \"ganti\" untuk mengganti nama menu makanan       |")
    print ("|d. \"keluar\" untuk keluar dari program              |")
    x = input("|Silahkan ketik jawawban anda disini = ")
    while x != "ebuset" :
        if x == "tambah" :
            tambah_menu()
        elif x == "hapus" :
            hapus_menu()
        elif x == "ganti" :
            ganti_menu()
        elif x == "keluar" :
            print ("| Selamat tinggal, until we meet again :) |")
            sys.exit()
        else :
            print ("error, perintah yang anda masukkan tidak terdaftar, dimohon ketik sesuai dengan perintah di atas !|")
            x = input("|Silahkan ketik ulang disini = ")

def main_menu () :
    print("     ⠄⠄⠄⠄⠄⣀⣠⣤⣤⣤⣤⢤⣤⣄⣀⣀⣀⣀⡀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠉⠹⣾⣿⣛⣿⣿⣞⣿⣛⣺⣻⢾⣾⣿⣿⣿⣶⣶⣶⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠄⠠⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣆⠄⠄⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠄⠘⠛⠛⠛⠛⠋⠿⣷⣿⣿⡿⣿⢿⠟⠟⠟⠻⠻⣿⣿⣿⣿⡀⠄⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⢀        ⢛⣿⣁      ⣀⣰⣿⣿⣿⣿⡀⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠉⠛⠺⢶⣷⡶⠃⠄⠄⠨⣿⣿⡇⠄⡺⣾⣾⣾⣿⣿⣿⣿⣽⣿⣿⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠛⠁⠄⠄⠄⢀⣿⣿⣧⡀⠄⠹⣿⣿⣿⣿⣿⡿⣿⣻⣿⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠛⠟⠇⢀⢰⣿⣿⣿⣏⠉⢿⣽⢿⡏⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠤⣤⣴⣾⣿⣿⣾⣿⣿⣦⠄⢹⡿⠄⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠒⣳⣶⣤⣤⣄⣀⣀⡈⣀⢁⢁⢁⣈⣄⢐⠃⠄⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⣿⣛⣻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⠄⠄⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣬⣽⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢘⣿⣿⣻⣛⣿⡿⣟⣻⣿⣿⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠛⢛⢿⣿⣿⣿⣿⣿⣿⣷⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄")
    print("     ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠉⠉⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("|===================== 0.0 =====================|")
    print ("|-----------------------------------------------|")
    print ("|-----Halo, Selamat Datang di Program Menu------|")
    print ("|-------Made by Felix Christopher Afrian--------|")
    print ("|-----------------------------------------------|")
    print ("|------------Type \"mulai\" to enter--------------|")
    x = input("|ketik mulai = ")
    while x != "keluar" :
        if x == "mulai" or x == "Mulai" or x == "MULAI" :
            print ("|=======================================|")
            print ("|Silahkan pilih menu yang ingin di-akses|")
            print ("|a. lihat menu                          |")
            print ("|b. tambah menu                         |")
            print ("|c. hapus menu                          |")
            print ("|d. ganti menu                          |")
            print ("|e. keluar program                      |")
            x1 = input("|Ketik abjad disini(contoh : a) = ")
            while x1 != "aowkaowkak" :
                if x1 == "a" :
                    lihat_menu()
                elif x1 == "b" :
                    tambah_menu()
                elif x1 == "c" :
                    hapus_menu()
                elif x1 == "d" : 
                    ganti_menu()
                elif x1 == "e" :
                    print ("| Selamat tinggal, until we meet again :) |")
                    sys.exit()
                else :
                    print ("|error, perintah yang anda masukkan tidak terdaftar, dimohon ketik sesuai dengan perintah di atas !|")
                    x1 = input("|Silahkan ketik ulang disini = ")
                
        else :
            print ("|System error, please enter \"mulai\" to enter|")
            x = input("|Please type here = ")

main_menu()    
