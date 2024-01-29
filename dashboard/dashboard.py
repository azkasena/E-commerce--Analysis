import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="dark")


def create_top_city_df(df):
    top_city_df = (
        df.groupby(by="customer_city")
        .customer_id.nunique()
        .sort_values(ascending=False)
    )
    top_city_df = top_city_df.reset_index(name="customer_count")
    return top_city_df


def create_top_seller_df(df):
    top_seller_df = df.groupby("seller_id").size().reset_index(name="order_count")
    top_seller_df.sort_values(by="order_count", ascending=False)
    top_seller_df.reset_index(drop=True)
    return top_seller_df


total_seller_df = pd.read_csv("total_seller_data.csv")
most_city_df = pd.read_csv("most_city_data.csv")

top_seller_df = create_top_seller_df
top_city_df = create_top_city_df


st.header("HeySale! Analytics Dashboard")

st.subheader("Kota dengan pelanggan tertinggi")

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=most_city_df["customer_count"], y=most_city_df["customer_city"])
plt.xlabel("Customer Count")
plt.xlabel("Customer Count")
plt.ylabel("Kota Customer")
plt.title("Kota dengan pemesan tertinggi")
st.pyplot(fig)

st.subheader("Penjual dengan total pesanan tertinggi")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=most_city_df["customer_count"], y=most_city_df["customer_city"])
plt.xlabel("Customer Count")
plt.xlabel("Order Count")
plt.ylabel("Seller ID")
plt.title("Penjual dengan pemesan tertinggi")
st.pyplot(fig)

st.caption("Copyright (c) Azka Avicenna 2023")
