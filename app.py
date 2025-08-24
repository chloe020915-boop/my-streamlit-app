import streamlit as st
st.title("你是谁？")
user_name = st.text_input("请输入你的名字")
if user_name:
    if user_name == "范铱伦":
        st.success("原来你是范铱伦!")
    else:
        st.success("你为什么不是范铱伦？")
