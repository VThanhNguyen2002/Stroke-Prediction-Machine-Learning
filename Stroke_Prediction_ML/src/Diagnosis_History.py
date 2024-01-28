import streamlit as st
import pandas as pd
import pyodbc # Thư viện pyodbc để làm các thao tác với cơ sở dữ liệu

def connect_to_database():
    # Kết nối đến cơ sở dữ liệu SQL Server
    connection_string = "DRIVER={SQL Server};SERVER=ADMIN-PC\SQLEXPRESS;DATABASE=dulieudotquy;UID=sa;PWD=123"
    conn = pyodbc.connect(connection_string)
    
    # Trả về kết nối
    return conn


def thongtinbenhnhan():
    conn = connect_to_database()
    query = "SELECT * FROM ThongTinKhamBenh"
    data = pd.read_sql(query, conn)
    conn.close()
    return data


# Hiển thị các phần tử của trang dữ liệu
def show_dulieu_page():
    st.markdown('<h1 class="title">LỊCH SỬ CHUẨN ĐOÁN BỆNH</h1>', unsafe_allow_html=True)
    conn = connect_to_database()
    data = thongtinbenhnhan()
    if st.button('Bấm vào đây! | Danh sách lịch sử chuẩn đoán bệnh'):
        if conn:
            st.success("Đã load danh sách lịch sử chuẩn đoán thành công!")
            st.write(data) # Hiển thị dữ liệu
        else:
            st.warning("Đã load danh sách lịch sử chuẩn đoán thất bại!")
    st.markdown(
        """
        <style>
        /* Thay đổi font và màu cho tiêu đề */
        .title {
            font-size: 40px;
            font-family: 'Time News Roman', sans-serif;
            color: #FF0000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    show_dulieu_page()

if __name__ == "__main__":
    main()
