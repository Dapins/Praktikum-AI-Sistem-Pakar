"""
SISTEM PAKAR DIAGNOSA PENYAKIT GASTRO USUS
Versi GUI menggunakan Streamlit
"""

import streamlit as st

# ============================================================
# KNOWLEDGE BASE 
# ============================================================

Diagnosa = {
    33: ("Keracunan Staphylococcus aureus", {
        20: ("Mencret",          [1, 2, 4, 5]),
        21: ("Muntah",           [4, 5, 6]),
        22: ("Sakit perut",      [4, 7]),
        23: ("Darah rendah",     [4, 8, 9]),
        29: ("Makan daging",     [14, 15]),
    }),
    34: ("Keracunan jamur beracun", {
        20: ("Mencret",          [1, 2, 4, 5]),
        21: ("Muntah",           [4, 5, 6]),
        22: ("Sakit perut",      [4, 7]),
        24: ("Koma",             [8, 10]),
        30: ("Makan jamur",      [14, 16]),
    }),
    35: ("Keracunan Salmonellae", {
        20: ("Mencret",          [1, 2, 4, 5]),
        21: ("Muntah",           [4, 5, 6]),
        22: ("Sakit perut",      [4, 7]),
        25: ("Demam",            [4, 5, 9, 11]),
        26: ("Septicaemia",      [4, 8, 11, 12]),
        29: ("Makan daging",     [14, 15]),
    }),
    36: ("Keracunan Clostridium botulinum", {
        21: ("Muntah",           [4, 5, 6]),
        27: ("Lumpuh",           [4, 13]),
        31: ("Makan makanan kaleng", [14, 17]),
    }),
    37: ("Keracunan Campylobacter", {
        28: ("Mencret berdarah", [1, 2, 3, 4, 10]),
        22: ("Sakit perut",      [4, 7]),
        25: ("Demam",            [4, 5, 9, 11]),
        32: ("Minum susu",       [18, 19]),
    }),
}

Gejala = {
    1: "Buang air besar (>2 kali)",   2: "Berak encer",
    3: "Berak berdarah",              4: "Lesu dan tidak bergairah",
    5: "Tidak selera makan",          6: "Merasa mual dan sering muntah",
    7: "Merasa sakit di bagian perut",8: "Tekanan darah rendah",
    9: "Pusing",                      10: "Pingsan",
    11: "Suhu badan tinggi",          12: "Luka di bagian tertentu",
    13: "Tidak dapat menggerakkan anggota badan tertentu",
    14: "Memakan sesuatu",            15: "Memakan daging",
    16: "Memakan jamur",              17: "Memakan makanan kaleng",
    18: "Membeli susu",               19: "Meminum susu",
}

# ============================================================
# INFERENCE ENGINE 
# ============================================================

def hitung(gejala: set) -> list:
    hasil = []
    for kode, (nama_diagnosa, gejala_menengah) in Diagnosa.items():
        bobot_m = 100 / len(gejala_menengah)
        total = 0.0
        gm_dialami = []

        for kode_m, (nama_m, ga) in gejala_menengah.items():
            cocok = [g for g in ga if g in gejala]
            total += (len(cocok) / len(ga)) * bobot_m

            if cocok:
                gm_dialami.append(nama_m)

        hasil.append((kode, nama_diagnosa, round(total, 2), gm_dialami))

    return sorted(hasil, key=lambda x: x[2], reverse=True)

# ============================================================
# STREAMLIT GUI
# ============================================================

st.set_page_config(page_title="Sistem Pakar Gastro Usus", layout="wide")

st.title("🩺 Sistem Pakar Penyakit Gastro Usus")
st.markdown("Pilih gejala yang dialami pasien, lalu klik **Diagnosa**")

# =========================
# INPUT GEJALA
# =========================
st.subheader("📋 Pilih Gejala")

opsi = {f"[{k}] {v}": k for k, v in Gejala.items()}

selected = st.multiselect(
    "Gejala pasien:",
    options=list(opsi.keys())
)

# =========================
# PROSES
# =========================
if st.button("🔍 Diagnosa"):

    if not selected:
        st.warning("Pilih minimal satu gejala!")
    else:
        gejala_input = set(opsi[s] for s in selected)
        hasil = hitung(gejala_input)

        st.subheader("📊 Hasil Diagnosa")

        for i, (kode, nama, persen, gm_dialami) in enumerate(hasil):

            if i == 0:
                st.success(f"Diagnosa Utama: {nama}")

            st.write(f"**[{kode}] {nama}**")
            st.progress(int(persen))

            st.write(f"Persentase: {persen:.2f}%")
            st.write(f"Gejala menengah: {', '.join(gm_dialami) if gm_dialami else '-'}")
            st.markdown("---")