import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Load data
data = pd.read_csv('dashboard\main_data.csv')

# Tampilkan judul dashboard
st.title('Dashboard Data Penjualan')

# Sidebar
st.sidebar.title('Pengaturan')

# Pilihan untuk menampilkan data tabel
show_data_table = st.sidebar.checkbox('Tampilkan Data Penjualan', True)

# Pilihan untuk menampilkan ringkasan statistik
show_statistics = st.sidebar.checkbox('Tampilkan Ringkasan Statistik', True)

# Pilihan untuk menampilkan visualisasi data
show_visualizations = st.sidebar.checkbox('Tampilkan Visualisasi Data', True)

# Jika pengguna memilih untuk menampilkan data tabel
if show_data_table:
    # Tampilkan data dalam bentuk tabel
    st.subheader('Data Penjualan')
    st.write(data)

# Jika pengguna memilih untuk menampilkan ringkasan statistik
if show_statistics:
    # Tampilkan ringkasan statistik
    st.subheader('Ringkasan Statistik')
    st.write(data.describe())

# Jika pengguna memilih untuk menampilkan visualisasi data
if show_visualizations:
    # Visualisasi data

    top_products = data['product_id'].value_counts().head(5)

    # Tampilkan top 5 produk dalam bentuk visualisasi
    st.subheader('Top 5 Produk')
    fig, ax = plt.subplots()
    top_products.plot(kind='bar', ax=ax)
    plt.xlabel('Product ID')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    top_customers = data['customer_id'].value_counts().head(5)

    # Tampilkan 5 pelanggan teratas dalam bentuk visualisasi
    st.title('Top 5 Pelanggan')
    fig, ax = plt.subplots()
    top_customers.plot(kind='bar', ax=ax)
    plt.xlabel('Customer ID')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    st.pyplot(fig)


