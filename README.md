# Tugas 2 PAA

1.	Tugas kelompok maksimal 2 orang per kelompok
2.	Waktu pengerjaan 1 Minggu
3.	Bobot masing-masing soal berbanding terbalik dengan jumlah kelompok yang berhasil menyelesaikan soal-soal tersebut.
4.	Ada 6 soal, silahkan mengerjakan soal-soal yang bisa Anda kerjakan. Ke 6 soal tersebut adalah sebagai berikut:
    -	(Easy) best-time-to-buy-and-sell-stock [Link Soal 1](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=problem-list-v2&envId=dynamic-programming)
    -	(Easy) climbing-stairs [Link Soal 2](https://leetcode.com/problems/climbing-stairs/description/?envType=problem-list-v2&envId=dynamic-programming)
    -	(Medium) coin-change [Link Soal 3](https://leetcode.com/problems/coin-change/description/?envType=problem-list-v2&envId=dynamic-programming)
    -	(Medium) best-time-to-buy-and-sell-stock-with-cooldown [Link Soal 4](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/?envType=problem-list-v2&envId=dynamic-programming)
    -	(Hard) best-time-to-buy-and-sell-stock-iv [Link Soal 5](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/?envType=problem-list-v2&envId=dynamic-programming)
    -	(Hard) dungeon-game [Link Soal 6](https://leetcode.com/problems/dungeon-game/description/?envType=problem-list-v2&envId=dynamic-programming)
5.	Petunjuk:
    - Pilih soal yang bisa anda kerjakan (semakin banyak semakin bagus)
    - Buat laporan dalam bentuk ppt yang berisi:
        1.	Deskripsi soal
        2.	Abstraksi dari soal (Analisis soal sampai ketemu modelnya)
        3.	Penggambaran dari model ke pseudocode
        4.	Implementasi Anda
        5.	Halaman bukti (Screenshot) kalau pengerjaan Anda accepted

# Desain Pattern
Berikut adalah pola desain utama yang kami identifikasi dan terapkan dalam perangkat lunak PVT ini :<br>
**1. Singleton Pattern (Pola Singleton)**
<p align='justify'><b>Tujuan</b> : Memastikan sebuah kelas hanya memiliki satu instansi dan menyediakan titik akses global ke instansi tersebut. <br>
<b>Penerapan dalam PVT</b> : Pola Singleton digunakan pada kelas DatabaseUtil. Kelas ini bertanggung jawab untuk mengelola koneksi ke database. Dengan menerapkan Singleton, kami memastikan bahwa hanya ada satu objek DatabaseUtil yang dibuat selama masa pakai aplikasi. Ini mencegah duplikasi koneksi database yang tidak perlu dan mengelola sumber daya database secara efisien, karena koneksi database adalah sumber daya yang seringkali mahal dan unik dalam sebuah aplikasi.</p>
<br>

**2. Command Pattern (Pola Perintah)**
<p align='justify'><b>Tujuan</b> : Mengkapsulasi sebuah permintaan (request) sebagai sebuah objek. Ini memungkinkan klien untuk memparametrisasi permintaan yang berbeda, mengantrekan atau mencatat permintaan, dan mendukung operasi yang dapat di-undo.<br>
<b>Penerapan dalam PVT</b> : Konsep dari Command Pattern terdapat dalam cara kami mendesain controller. Setiap tindakan pengguna (seperti "Send Measurement", "View Observer Detail", "Add New Participant") dienkapsulasi dalam metode-metode spesifik di dalam kelas Controller yang relevan. Metode-metode ini menerima parameter yang diperlukan dan mengeksekusi serangkaian operasi untuk memenuhi permintaan tersebut. Ini mirip dengan sebuah "perintah" yang dikerjakan oleh controller.</p>

**3. Observer Pattern (Pola Observer)**
<p align='justify'><b>Tujuan : </b>Mendefinisikan dependensi satu-ke-banyak antar objek, sehingga ketika satu objek berubah keadaan, semua dependensinya diberitahu dan diperbarui secara otomatis. Pola ini sering digunakan dalam framework Model-View-Controller (MVC).<br>
<b>Penerapan dalam PVT :</b> Konsep inti dari Observer Pattern ada dalam cara kami memastikan konsistensi data di memori. Saat data di database diubah (misalnya, melalui Edit Data Observer atau Add New Participant), Controller yang melakukan perubahan tersebut akan secara aktif me-refresh List data di memori (observerList, participantList, measurementList) dengan memuat ulang data dari database. Ini mensimulasikan mekanisme pembaruan otomatis: perubahan pada "Subject" (database) memicu pembaruan pada "Observer" (list data di memori yang digunakan oleh controller).</p>

**4. Factory Pattern (Pola Pabrik)** 
<p align='justify'><b>Tujuan</b> : Membuat objek tanpa mengekspos logika pembuatannya kepada klien dan merujuk pada objek yang baru dibuat menggunakan interface umum. Ini termasuk dalam kategori pola kreasi (creational pattern).<br>
<b>Penerapan dalam PVT :</b> Konsep dasar Factory Pattern terwujud secara implisit dalam konstruksi objek Model (seperti Participant, Observer, Measurement) di dalam kelas Controller. Ketika Controller membaca ResultSet dari database, ia bertanggung jawab untuk "membuat" objek Model yang sesuai. Ini mengkapsulasi logika pembuatan objek dari "klien" (yaitu, bagian lain dari controller yang hanya menerima objek Model yang sudah jadi).<br></p>
    
**5. Builder Pattern (Pola Pembangun)**
<p align='justify'><b>Tujuan</b> : Membangun objek kompleks secara bertahap menggunakan objek sederhana dan pendekatan langkah demi langkah. <br>
<b>Penerapan dalam PVT :</b> Pola Builder tidak secara eksplisit diimplementasikan dalam struktur kelas terpisah. Namun, konsepnya tercermin dalam cara kami meminta input data dari pengguna untuk objek baru (seperti Observer atau Participant). Daripada meminta semua input sekaligus, kami meminta atribut satu per satu (username, password, nama, alamat, dll.), memvalidasinya, dan kemudian menggunakan data tersebut untuk "membangun" objek Model langkah demi langkah sebelum menyimpannya ke database. Ini adalah bentuk sederhana dari konstruksi bertahap. </p>

**6. Adapter Pattern (Pola Adaptor)**
<p align='justify'><b>Tujuan</b> : Bertindak sebagai penerjemah yang mengadaptasi interface server untuk klien.<br>
<b>Penerapan dalam PVT :</b> Pola Adapter terwujud dalam peran kelas DatabaseUtil. Kelas ini berfungsi sebagai adaptor antara kode Java kami (yang menggunakan API JDBC standar) dan sistem manajemen database PostgreSQL yang spesifik. Kode Java tidak berinteraksi langsung dengan detail koneksi atau driver PostgreSQL; ia hanya memanggil DatabaseUtil.getConnection(). DatabaseUtil kemudian "mengadaptasi" permintaan ini ke driver JDBC PostgreSQL.</p>
