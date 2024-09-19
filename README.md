# **README**
DIbawah ini adalah sebuah project membuat aplikasi mini dengan menggunakan fitur CRUD. Aplikasi ini dibuat menggunakan Bahasa permograman python. 

Aplikasi ini saya bikin dengan pengetahuan yang sudah saya pelajari dari materi yang saya pelajari dari moule 1 di purwadhika. 

Data yang Anda lihat di sini dikodekan di dalam file dan akan di-restart jika Anda menjalankan ulang aplikasi ini. Aplikasi ini tidak terhubung ke database apa pun. Data yang disertakan dalam aplikasi ini adalah data fiksi.

---

## **Introduction to the App**
Selamat Datang Aplikasi Rumah Sakit Dunk
Aplikasi yang memungkinkan anda dalam mengelola data pasien rumah sakit. Beberapa fitur yang disediakan dalam aplikasi ini adalah :
- Melihat Daftar Pasien
- Pasien Check In
- Mengedit Data Pasien
- Pasien Check Out
- Cek History Pasien

Dibawah ini adalah foto dari Menu Utama :

![mainmenu](https://github.com/user-attachments/assets/5c85697c-1f27-4a21-b40d-f604d6ce2d30)

---

## **Features**
Mari kita lihat satu per satu fiturnya.

### **1. Melihat Daftar Pasien**

![viewpatientdata](https://github.com/user-attachments/assets/310dd49f-fdf3-4332-b7b5-80490aa678e3)

Pada menu ini anda dapat melihat data pasien. Anda dapat melihat ID, nama, umur, ruangan dan status dari pasien tersebut. ID disini digunakan sebagai kunci untuk melakukan tindakan didalam aplikasi.

Anda dapat melihat data seluruh pasien atau sebagian data, artinya anda dapat mencari pasien tertentu berdasarkan ID nya. Kemampuan pencarian ini tidak menghiraukan apakah ID tersebut menggunakan huruf besar atau tidak.

#### **- Melihat Nama Pasien Melalui Id**

![viewfromID](https://github.com/user-attachments/assets/e8b6e61b-1848-4038-b048-ad2a70723129)


Pada menu ini anda dapat melihat data dari pasien tertentu, dengan mengetikkan ID dari pasien tersebut. Maka anda akan melihat ID, nama, umur, ruangan dan status pasien tersebut.

---

### **2. Pasien Check In**

![addpatient](https://github.com/user-attachments/assets/d5e08876-8c02-4580-b301-7f13998b41bc)


Pada menu ini, memungkinkan anda untuk melakukan check-in pasien atau menambah data pasien baru masuk.

Pertama anda diharuskan untuk mengecek ID, jika ID sudah terpakai maka anda diharuskan untuk menginput ID baru. 

Jika ID yang di input belum ada maka anda akan diarahkan untuk mengisi data pasien seperti nama, umur, ruangan yang kosong dan statusnya.

![dataafteradding](https://github.com/user-attachments/assets/c6b108dd-7358-4860-a8fd-e783b34cd89a)


---

### **3. Mengedit Data Pasien**

![updatepatientdata](https://github.com/user-attachments/assets/df3991f6-b6db-4890-b91b-2f589d5c7f1f)


Pada menu ini anda dapat merubah data dari pasien tertentu dengan memasukkan ID dari pasien yang ingin anda ubah. Dan anda dapat memilih data apa yang ingin anda ubah

Dengan menu ini anda dapat merubah semua data dari pasien seperti ID, nama, umur, ruangan dan status pasien.

---

### **4. Pasien Check Out**

![deletepatientdata](https://github.com/user-attachments/assets/3110c013-0446-48de-808c-8af070b7eca5)


Pada menu ini memungkinkan anda untuk mengahpus data dari pasien tertentu dengan memilih ID dari pasien yang ingin anda hapus.

Dengan begitu semua data dari pasien yang anda pilih akan terhapus atau dinyatakan pasien tersebut telah check-out

---

### **5. Cek History Pasien**

![historycheckout](https://github.com/user-attachments/assets/496b6b1f-47f1-44e5-92ff-957df7ae5ea8)


Pada menu ini anda dapat melihat pasien yang telah check-out atau data dari pasien yang dihapus akan otomatis masuk kedalam history pasien.
