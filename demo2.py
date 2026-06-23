import streamlit as st

st.title("Tính toán hàm luỹ thừa")

#tạo ra 2 cột để hiển thị cơ số và số mũ
col1 , col2 = st.columns(2)
with col1:
    base = st.number_input("Nhập cơ số (base):",value =1.0) 
#base : là nhập cơ số
with col2:
    exponent = st.number_input("Nhập số mũ (exponent):",value =0)
#exponent : là nhập số mũ

if st.button("Tính toán"):#nếu người dùng nhấn nút "Tính toán"
    result = base ** exponent
    st.latex(
        rf"({base})^{{{int(exponent)}}} = {result}"
        )#hiển thị kết quả tính toán dưới dạng công thức toán học


