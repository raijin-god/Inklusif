label scene_1:
    # Set layar hitam instan tanpa transisi, lalu fade in perlahan ke bg kamar
    scene black
    with None
    scene bg kamar with dissolve
    
    play music "bgm_ceria.ogg" loop
    
    "Bermain bersama Ladesh selalu menyenangkan. Kami sedang membuat mobil pemadam kebakaran yang sangat besar."
    "Tapi kadang, bermain dengan teman yang bisa mendengar... butuh sedikit kesabaran ekstra."
    "Reja melihat Ladesh bangkit dan membelakanginya."
    
    # Ladesh muncul dengan ekspresi biasa/normal
    show ladesh normal with dissolve
    
    "Ladesh membungkuk, mengubek-ngubek isi kotak mainan. Sambil membelakangi Reja, kepala Ladesh bergerak-gerak dan bahunya naik turun, tanda dia sedang berbicara dengan cepat."
    l "\"Wah, balok merahnya ke mana ya? Reja, kamu lihat nggak? Kalau nggak ada merah, mobil pemadamnya jadi aneh bentuknya...\""
    "Ladesh terus mengoceh sambil membelakangiku. Mataku tidak bisa melihat bibirnya sama sekali. Aku hanya melihat punggungnya."
    
    # EFEK GETAR PAKSA (MUKUL KARPET)
    show bg kamar at getar_kiri_kanan
    "Aku menepuk karpet dengan keras agar Ladesh menoleh."
    
    "Tapi Ladesh sedang asyik membongkar mainan plastik yang berisik. Dia tidak merasakan ketukanku."
    "Aku benci diabaikan. Aku merasa ditinggalkan sendirian."

label mekanik_1:
    "Ladesh tidak melihatmu dan asyik sendiri. Apa yang harus Reja lakukan?"
    
    # FIX: call screen tidak support "with", pakai renpy.transition() di baris sebelumnya
    $ renpy.transition(dissolve)
    call screen pilihan_marah_tepuk
    
    if _return == "marah":
        "Reja melempar balok birunya dengan kesal ke arah kotak mainan."
        
        # EFEK GETAR PAKSA (BALOK KENA PUNGGUNG)
        show bg kamar at getar_atas_bawah
        "Balok itu mengenai punggung Ladesh."
        
        # Ladesh kaget dan ganti ekspresi marah
        show ladesh marah
        "Ladesh kaget setengah mati. Dia berbalik dengan wajah marah, memegang punggungnya."
        
        l "\"Aduh! Kamu kenapa sih, Ja? Jahat banget!\""
        
        # Ladesh dihilangkan dari layar karena ceritanya dia kabur
        hide ladesh with dissolve
        "Ladesh marah dan keluar dari kamar. Melempar barang tidak membuat Ladesh mengerti. Mari coba cara yang lebih baik."
        
        scene black with dissolve
        scene bg kamar with dissolve
        
        # Ladesh normal dimunculkan lagi karena adegan mengulang
        show ladesh normal with dissolve
        jump mekanik_1 
        
    elif _return == "tepuk":
        "Reja berdiri, berjalan menghampiri Ladesh, lalu menepuk pundaknya dua kali."
        "Ladesh menoleh. Reja menatap mata Ladesh, menunjuk telinganya sendiri, lalu menyilangkan kedua tangan di depan dada."
        "Ladesh tersentak, wajahnya berubah menjadi rasa bersalah."
        
        l "\"Eh! Maaf, Ja. Aku lupa kalau ngomong harus hadap ke kamu.\""
        
        jump scene_2
