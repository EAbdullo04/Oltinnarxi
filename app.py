import streamlit as st
import pandas as pd
import joblib

# Modelni yuklash
model = joblib.load("model.pkl")

# Foydalanuvchi interfeysi
st.title("Oltin narxini bashorat qilish ilovasi")
st.write("Oltinning parametrlarini kiriting:")

# Parametrlarni foydalanuvchidan olish
open_price = st.number_input("Ochilgan narx (Open)", value=1800.0)
high_price = st.number_input("Eng yuqori narx (High)", value=1820.0)
low_price = st.number_input("Eng past narx (Low)", value=1790.0)
volume = st.number_input("Hajm (Volume)", value=5000)

# Bashorat qilish uchun tayyorlash
if st.button("Bashorat qiling"):
    input_data = pd.DataFrame({
        'Open': [open_price],
        'High': [high_price],
        'Low': [low_price],
        'Volume': [volume]
    })
    prediction = model.predict(input_data)[0]
    st.success(f"Bashorat qilingan oltin narxi (Close): ${prediction:.2f}")




