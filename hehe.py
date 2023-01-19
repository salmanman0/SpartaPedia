from datetime import datetime

print("Selamat datang di Sistem kasir kop ijo kafe")
print("LIST MENU")
print("1. Lihat member")
print("2. Tambah Member Baru")
print("3. Kasir")
print("4. Lihat Menu")
print("5. keluar")
pilihan = int(input("Pilih Menu :"))
print(pilihan)

Menu = [
    {"jenis_menu":"minuman","nama_menu":"kopi susu","harga":18000},
    {"jenis_menu":"minuman","nama_menu":"banderek","harga":12500},
    {"jenis_menu":"makanan","nama_menu":"ayam geprek","harga":22500},
    {"jenis_menu":"minuman","nama_menu":"teh tarik","harga":15000},
    {"jenis_menu":"makanan","nama_menu":"pecel lele","harga":35000},
    {"jenis_menu":"makanan","nama_menu":"teh panas","harga":5000},
    {"jenis_menu":"minuman","nama_menu":"jus jeruk","harga":18000},
    {"jenis_menu":"makanan","nama_menu":"bakso beranak","harga":22500}
]

member = [
    {"id":"p00001","nama_member":"Kevin De Bruney","tgl_gabung":"13-09-2022"},
    {"id":"p00002","nama_member":"ronaldo alexsander","tgl_gabung":"22-09-2022"},
    {"id":"p00003","nama_member":"soleh setiawan","tgl_gabung":"30-09-2022"},
    {"id":"p00004","nama_member":"kafi lihandri","tgl_gabung":"15-09-2022"},
    {"id":"p00005","nama_member":"agustin setiawan","tgl_gabung":"12-09-2022"}  
]  
    
data_transaksi = []
temp_pesanan = []

def lihat_member():
    i = 0
    no = 1
    print("DAFTAR MEMBER")
    while i < len(member):
        print(f'{no},{member[i]["id"]}, nama :{member[i]["nama_member"]}, sejak{member[i]["tgl_gabung"]}')
        no += 1
        i += 1

if pilihan == 1:
    lihat_member()

def lihat_menu(jenis):
    i = 0
    no = 1
    if(jenis=="minuman"):
        print("DAFTAR MENU MINUMAN") 
        while i < len(Menu):
            if(Menu[i]["jenis_menu"]==jenis):
                print(f'{no}. {Menu[i]["nama_menu"]}, harga :{Menu[i]["harga"]} ')   
                no += 1
            i += 1 

    if(jenis=="makanan"):
        print("DAFTAR MENU MAKANAN") 
        while i < len(Menu):
            if(Menu[i]["jenis_menu"]==jenis):
                print(f'{no}. {Menu[i]["nama_menu"]}, harga :{Menu[i]["harga"]} ')   
                no += 1
            i += 1        

if pilihan  == 4:
     lihat_menu("minuman")

def tambah_member(id,nama):
    now = datetime.now()
    member.append({"id":id,"nama_member":nama,"tgl_gabung":now.strftime("%d-%n-%y")})
    print("DATA BERHASIL DITAMBAHKAN")

def cek_member(id_member):
    setatus = False
    nama_member = "";
    for m in member:
        if m["id"]  == id_member:
            setatus = True
            nama_member =m["nama_member"] 
    return{"setatus":setatus,"nama_member":nama_member}

def lihat_pesanan():
    no = 1
    for p in temp_pesanan:
        print(f'{no},{p["nama_menu"]}, jumlah:{p["jumlah"]}') 
        no += 1

def get_menu_by_jenisnomer(jenis,nomer):
    temp_info = "Data tidak ada";
    tamp_pilahan_menu = "";
    i = 0
    no = 1
    while i <len(Menu):
        if(Menu[i]["jenis_menu"]==jenis):
            if(no==nomer):
                temp_info = f'{no}. {Menu[i]["nama_menu"]}, harga: {Menu[i]["harga"]}'
                temp_pilhanan_menu = Menu[i]
            no += 1
        i += 1

def bayar_pesanan():
    no = 1
    total_harga = 0
    total_harga_final = 0
    member_setatus = False
    jumlah_bayar = 0
    kembalian = 0
    for p in temp_pesanan:
        print(f'{no}. {p["nama_menu"]}, jumlah:{p["jumlah"]}, total harga: {p["total_harga"]}')
        no += 1
        total_harga+=p["total_harga"]
    print(f"Total Bayar : {total_harga}")
    pilihan=input("Apakah konsumen terdaftar sebagai member? (y/n)")
    if(pilihan== "y"):
        id_member=input("input ID member :")
        if(cek_member(id_member)["setatus"]):
            member_setatus = (cek_member)["setatus"]
            print(f"Member ditemukan, a/n {cek_member(id_member)['nama_member']}")
        else:
            print("member tidak ditemukan ")
            member_setatus = False 
    else:
        member_setatus = False

    if(member_setatus): 
         total_harga_final = total_harga-(total_harga*0.1)
         print("Anda mendapatkan diskon 10% karna terdaftar sebagai member")
         print(f"Total harga (diskon 10%) :{total_harga_final}")
    else:
        total_harga_final = total_harga
        print("pembayaran normal : {total_harga_fianal}") 
    jumlah_bayar = int(input("masukan nominal uang : "))
    if (jumlah_bayar <= total_harga_final):
        print("==== maaf, uang anda kurang ===")
        bayar_pesanan()
    else:
        kembalian=jumlah_bayar-total_harga_final
        print(f"kembalian : {kembalian}")

        cetak_struk(member_setatus, total_harga, total_harga_final, jumlah_bayar, kembalian)
        temp_pesanan.clear()

def cetak_struk(setatus_member, total_harga, total_harga_final, jumlah_bayar, kembalian):
    print("=== STRUK KOPIJO KAFE ===")
    no = 1
    for p in temp_pesanan:
        print(f"{no}. {p['nama_menu']}, jumlah {p['jumlah']}, total_harga: {p[total_harga]}")
        no += 1
    print("=========================================================================")    
    if(setatus_member):
        print(f"== Total Harga : {total_harga}")
        print(f"== Total Harga (Discount 10%) : {total_harga_final}")
        print(f"== jumlah bayar : {jumlah_bayar}")
        print(f"== kembalian: {kembalian}")
        print("================== Terdaftar sebagai member disc 10% ==================")
    else: 
        print(f"== Total Harga : {total_harga}")
        print(f"== jumlah bayar : {jumlah_bayar}")
        print(f"== kembalian: {kembalian}")
        print("================== Terima Kasih ==================")

def kasir():
    setatus = ""
    while setatus != "end":
        print("pencatatan pesanan")
        print("1. pesanan makanan/minuman")
        print("2. lihat pesanan")
        print("3. bayar")
        print("4. kembali menu awal")
        pilihan=int(input("pilih sesuai nomer: "))
        if pilihan == 1:
            lihat_menu("makanan")
            lihat_menu("minuman")
            jawab = "y"
            while(jawab == "y"):
                print("1. makanan")
                print("2. minuman")
                jenis = int(input("pilih jenis"))
                if(jenis==1):
                    pilihan_menu =(input("menu nomer berapa? "))
                    print(get_menu_by_jenisnomer("makanan", pilihan_menu)["info"])
                    jumlah = int(input("jumlah pesanan : "))
                    total_harga = jumlah*get_menu_by_jenisnomer("makanan",pilihan_menu)["pilihan_menu"]["harga"]
                    pesanan = {
                       "nama_menu": get_menu_by_jenisnomer("makanan", pilihan_menu)["pilihan_menu"]["nama_menu"],
                       "harga": get_menu_by_jenisnomer("makanan", pilihan_menu)["pilihan_menu"]["harga"],
                       "jumlah": jumlah,
                       "total_harga": total_harga
                    }
                    temp_pesanan.append(pesanan)   
                elif(jenis==2):
                    pilihan_menu =(input("menu nomer berapa? "))
                    print(get_menu_by_jenisnomer("minuman", pilihan_menu)["info"])
                    jumlah = int(input("jumlah pesanan : "))
                    total_harga = jumlah*get_menu_by_jenisnomer("minuman",pilihan_menu)["pilihan_menu"]["harga"]
                    pesanan = {
                       "nama_menu": get_menu_by_jenisnomer("minuman", pilihan_menu)["pilihan_menu"]["nama_menu"],
                       "harga": get_menu_by_jenisnomer("minuman", pilihan_menu)["pilihan_menu"]["harga"],
                       "jumlah": jumlah,
                       "total_harga": total_harga
                    }
                    temp_pesanan.append(pesanan)
                else:
                    print("pilihan tidak tersedia")
                jawab = input("pesan lagi? (y/n)")
        elif pilihan == 2:
            lihat_pesanan()
        elif pilihan == 3:
            bayar_pesanan() 
        elif pilihan == 4: 
            print("kembali ke menu awal") 
            temp_pesanan.clear()
            setatus = "end" 
        else:
            print("error, pilihan tidak tersedia")    
                    
setatus = ""
while setatus != "end":
    print("Selamat datang di Sistem kasir kop ijo kafe")
    print("LIST MENU")
    print("1. Lihat member")
    print("2. Tambah Member Baru")
    print("3. Kasir")
    print("4. Lihat Menu")
    print("5. keluar")
    pilihan = int(input("Pilih Menu :"))
    print("Anda memilih : ", pilihan)

    if pilihan == 1:
        lihat_member()
    elif pilihan == 2:
        print("tambah member baru")
        id_member = input("input ID : ")
        while cek_member(id_member)["setatus"]:
            print("=== ID sudah ada ===")
            id_member=input("input ID : ")
        nama_member=input("input nama lengkap : ")
        tambah_member(id_member,nama_member)
    elif pilihan == 3:
        temp_pesanan.clear()
        kasir()
    elif pilihan == 4:
        lihat_menu("makanan")
        lihat_menu("minuman")
    elif pilihan == 5:
        print("Sisten Exit, Thankyou")
        setatus = "end"
    else:
       print("Error, pilihan tidak tersedia") 