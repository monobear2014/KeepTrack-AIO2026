import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt # type: ignore

st.title("Phân tích dữ liệu điểm số học sinh")

#tạo vùng upload file trên streamlit
upload_file = st.file_uploader("Chọn file excel",type =["xlsx"])

#hàm tính  điểm trung bình
def diem_trung_binh(scores):
    return sum(scores) / len(scores)
#hàm phân loại điểm số
def phan_loai_diem(scores):
    bins ={'9.0-10.0': 0, '8.0-8.9': 0, '7.0-7.9': 0, '5.0-6.9': 0, '0.0-4.9': 0}
    for score in scores:
        if score >=9.0:
            bins['9.0-10.0'] += 1
        elif score >=8.0:
            bins['8.0-8.9'] += 1
        elif score >=7.0:
            bins['7.0-7.9'] += 1
        elif score >=5.0:
            bins['5.0-6.9'] += 1
        else:
            bins['0.0-4.9'] += 1
    return bins
#nếu đã tải file lên => streamlit sẽ tiêp tục xử lí các bước tiếp theo
if upload_file:
#sau khi tải file lên, đọc dữ liệu từ file excel
    df = pd.read_excel(upload_file)
#xử lí danh sách điểm :
    scores = (
        df["Score"]
        .dropna()#bỏ qua giá trị NaN,none
        .astype(float)#chuyển đổi sang kiểu float
        .tolist()#chuyển đổi sang list
    )
#Dùng st.write để hiển thị chỉ số:
    st.write("Tổng số học sinh:", len(scores))
    st.write("Điểm trung bình:", round(diem_trung_binh(scores), 2))

#Tạo 1 dictionary bao gồm labels(key):danh sách tên nhóm
# và values(value):số lượng học sinh trong nhóm
    dict = phan_loai_diem(scores)
    labels = list(dict.keys())
    values = list(dict.values())

#Vẽ biểu đồ tròn
    fig, ax = plt.subplots(figsize = (3,3))
    #fig là lấy toàn bộ khu hình,ax là vùng hiển thị biển đồ trong đó
    #plt.subplots(figsize = (3,3)) là tạo ra 1 biểu đồ có kích thước 3x3 inch
    ax.pie(values,labels = labels, autopct='%1.1f%%', startangle=90)#vẽ biểu đồ tròn
    #.pie():  hàm vẽ biểu đồ tròn
    #autopct = '%1.1f%%' : hiển thị phần trăm trên biểu đồ
    ax.axis('equal')#đảm bảo biểu đồ tròn được vẽ đúng tỉ lệ
    st.pyplot(fig)#hiển thị biểu đồ trên streamlit
    st.markdown("Biểu đồ phân loại điểm số học sinh.")







