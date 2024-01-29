## Menentukan Pertanyaan Bisnis

- Siapa penjual yang paling sering mendapatkan pesanan?
- Kota apa dengan pengguna terbanyak?

## Menyiapkan semua library yang dibutuhkan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""## Data Wrangling

### Gathering Data
"""

customer_df=pd.read_csv("customers_dataset.csv")
customer_df.head(10)

order_df=pd.read_csv("orders_dataset.csv")
order_df.head()

sellers_df=pd.read_csv("sellers_dataset.csv")
sellers_df.head()

order_items_df=pd.read_csv("order_items_dataset.csv")
order_items_df.head(10)

product_df=pd.read_csv("products_dataset.csv")
product_df.head(15)

order_items_df.info()

"""### Assessing Data"""

customer_df.isna().sum()

order_df.isna().sum()

sellers_df.isna().sum()

product_df.isna().sum()

order_items_df.isna().sum()

"""### Cleaning Data"""

print("Total duplikasi seller : ", sellers_df.duplicated().sum())
print("Total duplikasi order : ", order_df.duplicated().sum())
print("Total duplikasi order_item : ", order_items_df.duplicated().sum())
print("Total duplikasi product: ", product_df.duplicated().sum())
print("Total duplikasi customer : ", customer_df.duplicated().sum())

"""## Exploratory Data Analysis (EDA)

### Explore seller and order count
"""

sellers_df.describe(include="all")
order_items_df.describe(include="all")

seller_order_df = pd.merge(
    left=sellers_df,
    right=order_items_df,
    left_on="seller_id",
    right_on="seller_id")
seller_order_df.head()

total_seller_df = seller_order_df.groupby("seller_id").size().reset_index(name="order_count")

total_seller_df = total_seller_df.sort_values(by='order_count', ascending=False)

total_seller_df = total_seller_df.reset_index(drop=True)

total_seller_df

total_seller_df=total_seller_df.head(5)

"""### Explore Customer and order item"""

most_city_df=pd.merge(
    left=customer_df,
    right=order_df,
    left_on="customer_id",
    right_on="customer_id"
)
most_city_df.head()

most_city_df = most_city_df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False)

most_city_df = most_city_df.reset_index(name="customer_count")

most_city_df.head

most_city_df=most_city_df.head(5)

"""## Explore

## Visualization & Explanatory Analysis

### Pertanyaan 1:
"""

plt.figure(figsize=(10,6))
plt.barh(total_seller_df["seller_id"], total_seller_df['order_count'])
plt.xlabel('Order Count')
plt.ylabel('Seller ID')
plt.title('Penjual dengan pemesan tertinggi')

plt.show()

"""### Pertanyaan 2:"""

plt.figure(figsize=(10,6))
plt.barh(most_city_df["customer_city"], most_city_df['customer_count'])
plt.xlabel('Customer Count')
plt.ylabel('Kota Customer')
plt.title('Kota dengan pemesan tertinggi')

plt.show()

"""## Conclusion

- Kesimpulan penjual yang memiliki pesanan terbanyak adalah seller id : 6560211a19b47992c3666cc44a7e94c0 dengan total pesanan 2033. Dengan itu, seller tersebut layak mendapatkan penghargaan
- Kesimpulan dari pertanyaan nomor dua adalah kota dengan customer terbanyak yaitu Sao Paulo dengan jumlah customer 15540. Dengan itu, kota Sao Paulo perlu mendapatkan perhatian lebih dari aplikasi.
"""

most_city_df.to_csv("most_city_data.csv", index=False)

total_seller_df.to_csv("total_seller_data.csv", index=False)
