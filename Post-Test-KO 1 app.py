import streamlit as st

st.title("Identifikasi Alkohol dan Uji Reaksi")

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

st.subheader("Susun Senyawa")

for i in range(jumlah_c):

    pilihan = st.selectbox(
        f"Karbon {i+1}",
        opsi,
        key=i
    )

    gugus.append(pilihan)

# Pilih pereaksi
pereaksi = st.selectbox(
    "Pilih Pereaksi",
    [
        "Lucas",
        "Jones",
        "Asam Kromat"
    ]
)

if st.button("Analisis"):

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

        # ======================
        # UJI LUCAS
        # ======================

        if pereaksi == "Lucas":

            produk = rumus.replace("OH", "Cl")

            st.subheader("Hasil Uji Lucas")

            st.code(
                f"{rumus} + HCl → {produk} + H2O"
            )

            if jenis == "Primer":

                st.info("Reaksi sangat lambat / tidak keruh")

            elif jenis == "Sekunder":

                st.info("Larutan keruh dalam beberapa menit")

            elif jenis == "Tersier":

                st.info("Larutan langsung keruh")

        # ======================
        # UJI JONES
        # ======================

        elif pereaksi == "Jones":

            st.subheader("Hasil Uji Jones")

            if jenis == "Primer":

                produk = rumus.replace(
                    "CH2(OH)",
                    "COOH"
                )

                st.code(
                    f"{rumus} + [O] → {produk}"
                )

                st.info(
                    "Warna oranye berubah menjadi hijau"
                )

            elif jenis == "Sekunder":

                produk = rumus.replace(
                    "CH(OH)",
                    "C=O"
                )

                st.code(
                    f"{rumus} + [O] → {produk}"
                )

                st.info(
                    "Warna oranye berubah menjadi hijau"
                )

            elif jenis == "Tersier":

                st.code(
                    "Tidak terjadi oksidasi"
                )

                st.info(
                    "Warna tetap oranye"
                )

        # ======================
        # ASAM KROMAT
        # ======================

        elif pereaksi == "Asam Kromat":

            st.subheader("Hasil Reaksi Asam Kromat")

            if jenis == "Primer":

                produk = rumus.replace(
                    "CH2(OH)",
                    "COOH"
                )

                st.code(
                    f"{rumus} + H2CrO4 → {produk}"
                )

                st.info(
                    "Alkohol primer teroksidasi menjadi asam karboksilat"
                )

            elif jenis == "Sekunder":

                produk = rumus.replace(
                    "CH(OH)",
                    "C=O"
                )

                st.code(
                    f"{rumus} + H2CrO4 → {produk}"
                )

                st.info(
                    "Alkohol sekunder teroksidasi menjadi keton"
                )

            elif jenis == "Tersier":

                st.code(
                    "Tidak bereaksi"
                )

                st.info(
                    "Alkohol tersier sulit dioksidasi"
                )
