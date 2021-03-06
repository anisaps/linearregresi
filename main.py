import csv
import streamlit as st
import pandas as pd
import os

st.title('Regresi Linear dan Kolerasi Pearson')
st.subheader('created by : 152017114 Anisa Putri Setyaningrum')


@st.cache(persist=True)
def exploredata(data):
    df = pd.read_csv(os.path.join(data))
    return df


def main(filepath):
    with open(filepath, "r+") as fin:
        fin.readline()
        totalX = sum(int(r[1]) for r in csv.reader(fin))
    print("Sigma X :: " + str(totalX))

    with open(filepath, "r+") as fin:
        fin.readline()
        totalY = sum(int(r[2]) for r in csv.reader(fin))
    print("Sigma Y :: " + str(totalY))

    with open(filepath, "r+") as fin:
        fin.readline()
        SigmaX2 = sum(int(r[1])**2 for r in csv.reader(fin))
    print("Sigma X^2 :: " + str(SigmaX2))

    with open(filepath, "r+") as fin:
        fin.readline()
        SigmaY2 = sum(int(r[2])**2 for r in csv.reader(fin))
    print("Sigma Y^2 :: " + str(SigmaY2))

    with open(filepath, "r+") as fin:
        fin.readline()
        SigmaXY = sum(int(r[1])*int(r[2]) for r in csv.reader(fin))
    print("Sigma XY :: " + str(SigmaXY))

    SigmaXKuadrat = totalX**2
    print("(Sigma X)^2:: " + str(SigmaXKuadrat))

    SigmaYKuadrat = totalY**2
    print("(Sigma X)^2:: " + str(SigmaYKuadrat))

    n = len(list(csv.reader(open(filepath))))-1
    print("n :: " + str(n))

    a = round((totalY*SigmaX2 - totalX * SigmaXY) /
              (n*SigmaX2 - SigmaXKuadrat), 5)
    b = round((n*SigmaXY - totalX*totalY)/(n*totalX - SigmaXKuadrat), 5)

    r = round(((n*SigmaXY - totalX*totalY)) / ((n*SigmaX2 -
                                                SigmaXKuadrat)*(n*SigmaY2 - SigmaYKuadrat))**0.5, 5)
    kd = round(((r**2) * 100), 5)
    varlain = 100 - kd

    interpretasikd = ("Besar kontribusi variabel X terhadap Y adalah " + str(kd) + " %" +
                      " dan sisanya yaitu sebesar " + str(varlain) + " %"+" dipengaruhi oleh variabel selain Y")

    if(b < 0):
        hasil = ("Y = " + str(a) + " - " + str(-b) + " X")
    else:
        hasil = ("Y = " + str(a) + " + " + str(b) + " X")

    if((r >= 0) and (r < 0.2)):
        r2 = ("Kekuatan hubungan (r) : Sangat Lemah")
    elif((r >= 0.2) and (r < 0.4)):
        r2 = ("Kekuatan hubungan (r) : Lemah")
    elif((r >= 0.4) and (r < 0.6)):
        r2 = ("Kekuatan hubungan (r) : Sedang")
    elif((r >= 0.6) and (r < 0.8)):
        r2 = ("Kekuatan hubungan (r) : Kuat")
    elif((r >= 0.8) and (r <= 1)):
        r2 = ("Kekuatan hubungan (r) : Sangat Kuat")

    if(r < 0):
        intrepretasikor = (
            "Nilai korelasi tersebut adalah negatif yang menyatakan bahwa perbandingannya adalah terbalik")
    else:
        intrepretasikor = (
            "Nilai korelasi tersebut adalah positif yang menyatakan bahwa perbandingannya adalah searah")

    values = a, b, totalX, totalY, SigmaX2, SigmaXKuadrat, SigmaXY, SigmaY2, n, hasil, SigmaYKuadrat, r, kd, r2, intrepretasikor, interpretasikd
    return values


try:
    data_file = st.file_uploader("Upload CSV", type=['csv'])
    data = exploredata(data_file.name)
    xa = main(data_file.name)
    st.write("Data yang digunakan")
    st.write(data)

    st.write("Nilai setiap variabel")

    if st.checkbox("n"):
        st.write(xa[8])
    if st.checkbox("ΣXi"):
        st.write(xa[2])
    if st.checkbox("ΣYi"):
        st.write(xa[3])
    if st.checkbox("ΣXiYi"):
        st.write(xa[6])
    if st.checkbox("ΣXi2"):
        st.write(xa[4])
    if st.checkbox("ΣYi2"):
        st.write(xa[7])
    if st.checkbox("(ΣXi)2"):
        st.write(xa[5])
    if st.checkbox("(ΣYi)2"):
        st.write(xa[10])

    st.write("Persamaan Linear Regresi")
    if st.checkbox("Konstanta a"):
        st.write(xa[0])
    if(st.checkbox("Koefisien b")):
        st.write(xa[1])
    if(st.checkbox("Y = a + bx")):
        st.success(xa[9])

    st.write("Nilai Korelasi")
    if(st.checkbox("r")):
        st.success(xa[11])
        st.write(xa[14])
        st.write(xa[13])
    if(st.checkbox("Koefisien Determinasi")):
        st.success(xa[12])
        st.write(xa[15])

except:
    st.write("Silahkan Pilih terlebih dahulu file data yang akan digunakan !")
