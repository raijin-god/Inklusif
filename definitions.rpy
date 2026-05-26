# ==========================================
# DEKLARASI GAMBAR (WAJIB SESUAIKAN NAMA FILE)
# ==========================================
# Lu udah tau caranya, pastikan nama di dalam tanda kutip sesuai nama file lu di folder images.
image bg kamar = "bg kamar.png" 
image cg pemadam = "cg pemadam.png"
image bg black = "#000000"

# ==========================================
# DEFINISI KARAKTER & EFEK
# ==========================================
define l = Character("Ladesh")

# Efek Animasi Nimbul (Hover Zoom)
transform tombol_nimbul:
    on idle:
        linear 0.1 zoom 1.0
    on hover:
        linear 0.1 zoom 1.1

# ==========================================
# ANIMASI GETAR PAKSA (ANTI-GAGAL)
# ==========================================
transform getar_kiri_kanan:
    linear 0.05 xoffset -30
    linear 0.05 xoffset 30
    linear 0.05 xoffset -30
    linear 0.05 xoffset 30
    linear 0.05 xoffset 0

transform getar_atas_bawah:
    linear 0.05 yoffset -30
    linear 0.05 yoffset 30
    linear 0.05 yoffset -30
    linear 0.05 yoffset 30
    linear 0.05 yoffset 0

# ==========================================
# CUSTOM SCREENS (TOMBOL GAMBAR)
# ==========================================
screen pilihan_marah_tepuk():
    hbox:
        align (0.5, 0.6) 
        spacing 150      
        imagebutton:
            idle "icon_marah.png"
            at tombol_nimbul
            action Return("marah")
        imagebutton:
            idle "icon_tepuk.png"
            at tombol_nimbul
            action Return("tepuk")

screen cari_buku_gambar():
    imagebutton:
        idle "buku_gambar_item.png"
        xpos 0.75 ypos 0.5  
        at tombol_nimbul
        action Return("ketemu")

screen pilihan_nangis_buku():
    hbox:
        align (0.5, 0.6)
        spacing 150
        imagebutton:
            idle "icon_nangis.png"
            at tombol_nimbul
            action Return("nangis")
        imagebutton:
            idle "icon_buku.png"
            at tombol_nimbul
            action Return("buku")