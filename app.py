import streamlit as st
st.title("你是谁？")
user_name = st.text_input("请输入你的名字")
if user_name:
    if user_name == "曾灏":
        st.success("原来你是曾灏!")
    else:
        st.success("你为什么不是曾灏？")
