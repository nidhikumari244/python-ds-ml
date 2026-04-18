import streamlit as st
import pandas as pd
import numpy as np

# title of the application 
st.title("Hlo streamlit")

#create a simple dataframe 

df= pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column': [10,20,30,40]

})
# st.write("here is the dataframe")
# st.write(df)

#chart 

st.write("here is the datframe")
st.write(df)

#line chart

chart_data=pd.DataFrame(
    np.random.random((20,3)),columns=['a','b','c']

)
st.write("here is the line chart:")
st.line_chart(chart_data)