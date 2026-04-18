import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name =st.text_input("enter your name:")
age=st.slider("Select your age:",0,100,20)
st.write(f"your age is {age}.")

option=["Select","python","java","c++","js"]
choice=st.selectbox("choose your fav. language:",option)
st.write(f"you select {choice}.")

if name:
    st.write(f"Hlo, {name}")

data={
    "Name":["Nidhi","B","R","K"],
    "Age":[20,22,15,10],
    "City":["Banglore","Banglore","America","Newyork"]

    }
df=pd.DataFrame(data)
df.to_csv("sampledata.csv") #save as
st.write(df)

uploaded_file=st.file_uploader("choose a csv file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)

