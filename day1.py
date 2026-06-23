import streamlit as st

#Tạo title,header,subheader streamlit
st.title("Day 1: Introduction to Streamlit")    
st.header("Header")
st.subheader("Subheader")

#caption sẽ nhỏ và nhạt hơn text
st.text("This is a text element")
st.caption("AIO KEEPTRACK")
#st.write giống với print nhưng print chỉ hiển thị
#trên console(terminal) còn st.write sẽ hiển thị trên giao diện web
st.write("This is a write element")
print("Hello print")


#phân tách code phía trên với phái dưới
st.divider()

# Markdown
st.markdown("# Heading 1")
st.markdown("## Heading 2")
#cách để tạo link trong markdown
st.markdown ("[AIVN] (https://aivietnam.edu.vn/)")
#Hiển thị công thức toán học với markdown
st.markdown("""
1. Machine learning
2. Deep learning
""")
st.markdown(r"$\sqrt{2x+1}$")
#Hiển thị công thức toán học với latex
#latex sẽ hiện ra giũa màn hình 
st.latex(r"\sqrt{2x+1}")
#ngoài ra có thể dùng st.write 
st.write("#### công thức toán:")
st.write(r"$\sqrt{2x+5}$")

st.divider()
#Hiển thị code và kết quả code
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
st.subheader("Input")
st.code(
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
""", language="python"
)
st.subheader("Output")
st.text(arr)
#st.echo vừa hiển thị vừa thực thi code
with st.echo():
    arr = np.array([1, 2, 3, 4, 5])
    arr
#không nhất thiết phải thêm language, streamlit sẽ tự nhận dạng ngôn ngữ
#tuy nhiên có language thì streamlit sẽ hiểu là ngôn ngữ gì và
#bật highlight syntax cho code đó(tô màu từ khoá, biến,hàm.....)

st.divider()
#Media
st.logo("Hoài Nam.jpeg")
st.image("Hoài Nam.jpeg", caption="Tôi là Hoài Nam")
st.audio("Hoài Nam.jpeg")
st.video("Hoài Nam.jpeg")






