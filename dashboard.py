import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Streamlit app of vgu")
st.text("Welcome to our dashboard")
st.header("I am a header")
st.write("you can write",10+5)

name = st.text_input("Enter your name :")
age = st.number_input("enter the age")
st.write("Your age is : ",age )
st.selectbox("Enter your course : ", ["BCA", "BTECH", "MCA"])
if st.button("click me "):
    st.success(" Click Button")
file = st.file_uploader("Upload your file ")
if file :
    content = file.read()
    st.write("File Uploaded  Sucessfully !!")

data = {"Name" : ["Tom", "Jack", "roni", "sweety"], "marks" : [10,20,40,50]}
df = pd.DataFrame(data)

st.dataframe(df)

data = pd.DataFrame(
    {
        "Marks" : [10,20,40,50]
    }
)

st.line_chart(data)
st.bar_chart(data)

subject = ["python", "c++", "java"]
marks = [20,10,5]

fig, ax = plt.subplots()
ax.pie(marks, labels=subject, autopct='%1.1f%%')

st.pyplot(fig)


