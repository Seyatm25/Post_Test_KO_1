import streamlit as st

st.title("Penyusun Alkohol")

# Jumlah karbon
jumlah_c = st.number_input(
    "Jumlah karbon",
    min_value=1,
    max_value=20,
    value=4
)

opsi = [
    "CH3",
    "CH2",
    "CH",
    "C",
    "CH2(OH)",
    "CH(OH)",
    "C(OH)"
]

gugus = []

st.subheader("Pilih gugus")

for i in range(jumlah_c):

    pilihan = st.selectbox(
        f"Karbon {i+1}",
        opsi,
        key=i
    )

    gugus.append(pilihan)

if st.button("Buat Senyawa"):

    rumus = "".join(gugus)

    st.subheader("Rumus Struktur")

    st.code(rumus)

    # Identifikasi alkohol
    if "CH2(OH)" in rumus:

        jenis = "Primer"

    elif "CH(OH)" in rumus:

        jenis = "Sekunder"

    elif "C(OH)" in rumus:

        jenis = "Tersier"

    else:

        jenis = None

    if jenis is None:

        st.error("Senyawa bukan alkohol")

    else:

        st.success(f"Alkohol {jenis}")

        # Lucas
        produk_lucas = rumus.replace("OH", "Cl")

        st.subheader("Reaksi Lucas")

        st.code(
            f"{rumus} + HCl → {produk_lucas} + H2O"
        )