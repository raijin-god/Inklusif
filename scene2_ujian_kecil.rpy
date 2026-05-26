label scene_2:
    "Ladesh sekarang duduk berhadapan lagi dengan Reja. Dia terlihat kebingungan mencari cara untuk menjelaskan soal balok merah yang hilang tadi."
    "Bantu Ladesh menjelaskan maksudnya! Temukan alat untuk bercerita di kamar ini."
    
    # FIX: call screen tidak support "with", pakai renpy.transition() di baris sebelumnya
    $ renpy.transition(dissolve)
    call screen cari_buku_gambar
    
    if _return == "ketemu":
        "Ladesh tersenyum lega mengambil buku gambar itu. Dia segera menggambar kotak berwarna merah dengan wajah sedih, lalu menunjukkannya ke Reja."
        "Aku tertawa. Aku mengerti sekarang. Ladesh sedang mencari balok merah yang habis."
        "Aku menunjuk kolong meja. Ada satu balok merah terselip di sana. Ladesh mengambilnya dengan gembira."
    
    scene black with fade
    scene bg kamar with fade
    "Kami melanjutkan membuat mobil pemadam. Kali ini, Ladesh tahu apa yang harus dilakukan."
    "Ladesh membutuhkan balok panjang warna kuning. Alih-alih langsung bicara sendiri seperti tadi, Ladesh berhenti."
    "Dia menatapku, lalu mengulurkan tangannya."
    "Ladesh menepuk pundak Reja pelan. Reja menoleh, membuat kontak mata. Ladesh bicara dengan pelan dan jelas sambil menunjuk tumpukan balok kuning di dekat kaki Reja."
    l "\"Reja, minta balok kuning.\""
    "Aku tersenyum. Aku bisa melihat bibirnya dengan sangat jelas, dan gerakan tangannya membantuku mengerti."
    "Reja mengangguk dan menyerahkan balok kuning itu. Ladesh mengacungkan jempolnya."
    
    "Bangunan mobil pemadam dari balok kami sudah hampir jadi dan terlihat tinggi."
    "Saat Reja mau memasang balok biru sebagai lampu sirine, tangannya tidak sengaja menyenggol ujung mobil pemadam itu."
    
    # EFEK GETAR PAKSA (BALOK JATUH)
    show bg kamar at getar_atas_bawah
    "Gawat! Tanganku menyenggolnya. Balok-balok itu jatuh berantakan."
    
    "Jantungku berdebar cepat. Aku takut Ladesh marah karena aku menghancurkan mainan kami."
label mekanik_2:
    "Reja merasa bersalah dan takut. Apa yang harus Reja lakukan?"
    
    # FIX: call screen tidak support "with", pakai renpy.transition() di baris sebelumnya
    $ renpy.transition(dissolve)
    call screen pilihan_nangis_buku
    
    if _return == "nangis":
        "Reja menutupi wajahnya dan mulai menangis. Ladesh ikut panik dan kebingungan melihat Reja menangis."
        "Menangis tidak menyelesaikan masalah. Mari cari cara memberi tahu Ladesh apa yang kurasakan."
        
        scene black with fade
        scene bg kamar with fade
        jump mekanik_2
        
    elif _return == "buku":
        "Reja menarik napas panjang. Dia mengambil buku gambar, menggambar wajah sedih, dan menulis kata 'Maaf' besar-besar."
        "Dia menunjukkannya pada Ladesh dengan tangan gemetar."
        "Ladesh melihat gambar itu. Dia tersenyum lebar dan menggelengkan kepalanya santai."
        
        l "\"Nggak apa-apa, Reja! Ayo kita bangun lagi sama-sama.\""
        
        jump scene_3
