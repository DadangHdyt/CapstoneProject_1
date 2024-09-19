# membuat data awal list pasien

listpasien = [
    {'id': 'PS01',
     'nama': 'Said',
     'umur': 30,
     'room': 'BR-1',
     'status': 'Dirawat'
     },
    {'id': 'PS02',
     'nama': 'Dadang',
     'umur': 27,
     'room': 'BR-2',
     'status': 'Dirawat'
     },
    {'id': 'PS03',
     'nama': 'Sempra',
     'umur': 27,
     'room': 'BR-3',
     'status': 'Dirawat'
     }
     ]

# history pasien
historypasien = []

# Fungsi untuk meminta konfirmasi pengguna sebelum melakukan aksi
def konfirmasi(data, aksi, pesan):
    check = input(f'Jika and ingin {pesan} data, ketik Y, jika tidak ketik N : ').upper()

    # Jika memilih tidak (N)
    if check == 'N':
        print(f'Data Tidak Jadi Di {pesan}')
        return 0
    
    # Jika memilih ya (Y), untuk aksi menambahkan data
    if aksi == 'input' and check == 'Y':
        print('===|>  Data Pasien Tersimpan  <|===')
        listpasien.append(data)
        return 1
    
    # Jika memilih ya (Y), untuk aksi update data
    if aksi == 'update' and check == 'Y':
        print('===|>  Data Pasien Telah Diupdate  <|===')
        listpasien.pop(data['index'])   # Hapus data lama dari daftar pasien
        listpasien.insert(data['index'], data['data'])  # Masukkan data yang telah diperbarui
        return 1
    
    # Jika tidak memilih Y atau N, ulangi permintaan konfirmasi
    konfirmasi(data, aksi, pesan)

# Fungsi untuk mencari index pasien berdasarkan id
def cariindex(databaru):
    for i in range(len(listpasien)):
        if listpasien[i]['id'] == databaru:
            return i    # mengembalikan index jika id ditemukan
    return -1   # mengembalikan -1 jika id tidak ditemukan

# Fungsi untuk mencetak daftar pasien yang telah check out
def pasien_check_out(data2):
    print('                 Daftar Pasien Check Out                 ')
    print("-" * 56)
    print(f"{'ID':<10}{'Nama':<20}{'Umur':<5}{'Room':<10}{'Status':<10}")
    print("-" * 56)
    for i in range(len(data2)):
        print(f"{data2[i]['id']:<10}{data2[i]['nama']:<20}{data2[i]['umur']:<5}{data2[i]['room']:<10}{data2[i]['status']:<10}")

# Fungsi untuk mencetak informasi pasien tertentu
def paster(data1):
    print(f"{'ID':<10}{'Nama':<20}{'Umur':<5}{'Room':<10}{'Status':<10}")
    print("-" * 56)
    print(f"{data1['id']:<10}{data1['nama']:<20}{data1['umur']:<5}{data1['room']:<10}{data1['status']:<10}")

# Fungsi untuk menampilkan daftar pasien
def daftarpasien():
    print('                     Daftar Pasien                     ')
    print("-" * 55)
    print(f"{'ID':<10}{'Nama':<20}{'Umur':<5}{'Room':<10}{'Status':<10}")
    print("-" * 55)
    for patient in listpasien:
        print(f"{patient['id']:<10}{patient['nama']:<20}{patient['umur']:<5}{patient['room']:<10}{patient['status']:<10}")

# Fungsi menampilkan daftar pasien dengan opsi menu
def view_pasien():
    while True:
        print('\n--- Opsi Menu Melihat Daftar Pasien ---')
        print('\n1. Melihat Daftar Seluruh Pasien')
        print('2. Melihat Nama Pasien melalui ID')
        print('3. Kembali ke Menu Utama\n')

        pilihan = input('Silahkan Pilih Nomor Opsi Menu : ')

        if pilihan == '1':
            if not listpasien:
                print("Tidak ada data pasien yang tersedia.")
            else:
                daftarpasien()
        
        elif pilihan == '2':
            patient_id = input("Masukkan ID Pasien: ").upper()
            patient_found = False
            for patient in listpasien:
                if patient['id'] == patient_id:
                    print('Data Pasien Yang DIcari : ')
                    print(f"\nID: {patient['id']}")
                    print(f"Nama: {patient['nama']}")
                    print(f"Umur: {patient['umur']}")
                    print(f"Room: {patient['room']}")
                    print(f"Status: {patient['status']}")
                    patient_found = True
                    break
            
            if not patient_found:
                print('\nPasien dengan ID ini tidak ditemukan.')
        
        elif pilihan == '3':
            break

        else:
            print('Pilihan tidak valid. Silakan coba lagi.')

# Fungsi untuk menambahkan pasien
def check_in_pasien():
    daftarpasien()
    while True:
        print(('\n--- Opsi Menu Check-In Pasien ---'))
        print('1. Check-In Pasien')
        print('2. Kembali Ke Menu Utama\n')
        
        pilcheckin = input('Silahkan Pilih Opsi Menu : ')

        if pilcheckin == '1':
            tambah_Id = (input('Masukkan ID Pasien: ')).upper()
            # Cek jika id sudah ada
            index = cariindex(tambah_Id)
            if index != -1:
                print('======> Pasien Yang Ingin Ditambahkan Sudah Ada <======')
                continue
            # jika belum ada maka lakukan inputan
            tambah_nama = input('Masukkan Nama Pasien : ').capitalize()
            tambah_umur = int(input('Masukkan Umur Pasien : '))
            tambah_ruangan = input('Masukkan Nama Ruangan (BR- ):').upper()
            tambah_status = input('Masukkan status Pasien (Dirawat/Rawat jalan) : ').capitalize()
            tabel = {
                'id': tambah_Id,
                'nama': tambah_nama,
                'umur': tambah_umur,
                'room': tambah_ruangan,
                'status': tambah_status
            }
            conf = konfirmasi(tabel, 'input', 'DITAMBAH')
            
            if conf:
                break

        if pilcheckin == '2':
            break

# Fungsi untuk mengedit data pasien yang sudah ada
def edit_pasien():
    daftarpasien()
    while True:
        print("\n--- Edit Data Pasien ---")
        print("1. Edit Nama")
        print("2. Edit Ruangan")
        print("3. Edit Umur")
        print("4. Edit Status")
        print("5. Keluar\n")

        choice = input("Silahkan Pilih Nomor Yang Mau Di Ubah : ")

        pilihan = {
            '1': 'nama',
            '2': 'room',
            '3': 'umur',
            '4': 'status'
        }
        if choice == '5':
            break
        databaru = str(input('Masukkan ID Pasien : ')).upper()
        index = cariindex(databaru)
        if index == -1:
            print('===> Data Yang Dicari Tidak Ada <===')
            continue
        ubahke = input(f'Mengubah {pilihan[choice]} Menjadi :').capitalize()
        #salin data lama pasien 
        datalama = {
            'index': index,
            'data': listpasien[index].copy()
        }
        # Ubah data sesuai pilihan
        datalama['data'][pilihan[choice]] = ubahke
        conf = konfirmasi(datalama, 'update', 'perbarui')
        if conf:
            daftarpasien()
            break

# Fungsi untuk menghapus data pasien
def hapus_data_pasien():
    daftarpasien()
    while True:
        print("\n--- Hapus Data Pasien ---")
        print('1. Hapus Data Pasien')
        print('2. Kembali Ke Menu Utama')

        pilih = input('Masukkan Nomor Opsi :')
        if pilih == '1':
            tambah_id = input('Masukkan ID Pasien : ').upper()
            index = cariindex(tambah_id)
            if index == -1:
                print('===> Pasien Yang Ingin Dihapus Tidak Ada <===')
                continue
            while True:
                check = str(input('Anda Yakin Ingin Menghapus? (Y/N) :')).upper()
                if check == 'Y':
                    print('Data Pasien Telah Dihapus')
                    print('-------------------------')
                    # Memindahkan pasien ke history pasien dan hapus dari daftar utama
                    historypasien.append(listpasien.pop(index))
                    break
                if check == 'N':
                    print('Data Tidak Jadi Dihapus')
                    print('-----------------------')
                    break
        elif pilih == '2':
            break

# Fungsi untuk menampilkan history pasien yang telah check-out
def view_history():
    print('Pasien Telah Pulang Dalam Keadaan Sehat')

    # Memperbarui Status Pasien yang telah Pulang
    stat = historypasien
    for i in range(len(stat)):
        stat[-1*i]['status'] = 'Check-out'

    # menampilkan daftar pasien yang telah check out atau pulang 
    pasien_check_out(stat)

# Menu utama program
while True:
        print("\nSelamat Datang DI RS Dunk")
        print()
        print('Pilihan Menu :')
        print("1. Melihat Daftar Pasien")
        print("2. Pasien Check In")
        print("3. Mengedit Data Pasien")
        print("4. Pasien Check Out")
        print("5. Cek History Pasien")
        print("6. Exit Program\n")

        pilihanmenu = input("Silahkan Pilih Nomor Menu: ")

        if pilihanmenu == '1':
            view_pasien()
        elif pilihanmenu == '2':
            check_in_pasien()
        elif pilihanmenu == '3':
            edit_pasien()
        elif pilihanmenu == '4':
            hapus_data_pasien()
        elif pilihanmenu == '5':
            view_history()
        elif pilihanmenu == '6':
            print('===> Selalu Jaga Kesehatan Anda <===')
            break
        else:
            print('Pilihan tidak Valid. Silahkan Coba Lagi')
