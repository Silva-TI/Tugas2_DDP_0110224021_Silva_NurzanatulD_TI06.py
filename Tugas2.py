# Data pegawai
pegawai_data = [
    {"nama": "Budi", "jabatan": "Manager", "agama": "Islam", "status": "Menikah"},
    {"nama": "Siti", "jabatan": "Asisten Manager", "agama": "Islam", "status": "Menikah"},
    {"nama": "I Gede", "jabatan": "Supervisor", "agama": "Hindu", "status": "Menikah"},
    {"nama": "Joko", "jabatan": "Staff", "agama": "Islam", "status": "Belum Menikah"},
    {"nama": "Alex", "jabatan": "Staff", "agama": "Kristen Protestan", "status": "Belum Menikah"}
]

# Fungsi untuk menghitung gaji
def hitung_gaji(pegawai):
    # Gaji Pokok berdasarkan jabatan
    if pegawai["jabatan"] == "Manager":
        gaji_pokok = 15000000
    elif pegawai["jabatan"] == "Asisten Manager":
        gaji_pokok = 10000000
    elif pegawai["jabatan"] == "Supervisor":
        gaji_pokok = 7000000
    elif pegawai["jabatan"] == "Staff":
        gaji_pokok = 4000000
    else:
        gaji_pokok = 0

    # Tunjangan jabatan (30% dari gaji pokok)
    tunjangan_jabatan = 0.3 * gaji_pokok

    # BPJS (10% dari gaji pokok)
    bpjs = 0.1 * gaji_pokok

    # Tunjangan keluarga (untuk yang sudah menikah, 10% dari gaji pokok)
    tunjangan_keluarga = []
    if pegawai["status"] == "Menikah": 
        tunjangan_keluarga = [gaji_pokok * 0.1]
    else:
        tunjangan_keluarga = [0]

    # Gaji Kotor
    gaji_kotor = gaji_pokok + tunjangan_jabatan + sum(tunjangan_keluarga)

    # Zakat profesi (jika muslim dan gaji kotor >= 7 juta, 2.5% dari gaji kotor)
    zakat_profesi = 0
    if pegawai["agama"] == "Islam" and gaji_kotor >= 7000000:
        zakat_profesi = gaji_kotor* 0.025

    # Gaji Bersih
    gaji_bersih = gaji_kotor - zakat_profesi - bpjs

    return {
        "nama": pegawai["nama"],
        "jabatan": pegawai["jabatan"],
        "agama": pegawai["agama"],
        "status": pegawai["status"],
        "gaji_pokok": gaji_pokok,
        "tunjangan_jabatan": tunjangan_jabatan,
        "tunjangan_keluarga": tunjangan_keluarga,
        "gaji_kotor": gaji_kotor,
        "zakat_profesi": zakat_profesi,
        "bpjs": bpjs,
        "gaji_bersih": gaji_bersih
    }

# Cetak slip gaji untuk setiap pegawai
for pegawai in pegawai_data:
    hasil = hitung_gaji (pegawai)
    print(f'Slip Gaji Pegawai')
    print(f"  Nama              : {hasil['nama']}")
    print(f"  Jabatan           : {hasil['jabatan']}")
    print(f"  Agama             : {hasil['agama']}")
    print(f"  Status            : {hasil['status']}")
    print(f"  Gaji Pokok        : Rp {hasil['gaji_pokok']}")
    print(f"  Tunjangan Jabatan : Rp {hasil['tunjangan_jabatan']}")
    print(f"  Tunjangan Keluarga: Rp {hasil['tunjangan_keluarga']}")
    print(f"  Gaji Kotor        : Rp {hasil['gaji_kotor']}")
    print(f"  Zakat Profesi     : Rp {hasil['zakat_profesi']}")
    print(f"  BPJS              : Rp {hasil['bpjs']}")
    print(f"  Gaji Bersih       : Rp {hasil['gaji_bersih']}")
    print("=" * 30)
