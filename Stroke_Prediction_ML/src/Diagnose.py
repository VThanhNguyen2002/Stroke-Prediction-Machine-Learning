import streamlit as st
import pandas as pd
import joblib
import pyodbc # Thư viện pyodbc để làm các thao tác với cơ sở dữ liệu
import tensorflow as tf
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Hàm để chọn mô hình
def chon_mo_hinh():
    uploaded_file = st.file_uploader("Chọn mô hình (file .pkl)", type=["pkl"])
    if uploaded_file is not None:
        loaded_model = joblib.load(uploaded_file)
        st.success("Mô hình đã được chọn!")
        return loaded_model
    return None

# Gọi hàm chon_mo_hinh để chọn mô hình
loaded_model = chon_mo_hinh()
#loaded_model = joblib.load('D:/Cachocphan/HK7/DoAnChuyenNganh/DoAnChuyenNganh_DeTai160/model/knn_model.pkl')

# Load dữ liệu huấn luyện
training_data = pd.read_csv("D:/Cachocphan/HK7/DoAnChuyenNganh/DoAnChuyenNganh_DeTai160/data/data_pre_process_2.csv")

data_cleaned = training_data.dropna()

# Hàm label_encoder được viết để thực hiện quá trình mã hóa các nhãn (labels) thành các số nguyên duy nhất.
def label_encoder(labels):
    # unique_labels = list(set(labels)): Hàm này tạo ra một danh sách các giá trị duy nhất trong danh sách nhãn 
    # đầu vào bằng cách sử dụng set để loại bỏ các giá trị trùng lặp, 
    # sau đó chuyển đổi nó thành danh sách bằng list.
    unique_labels = list(set(labels))  # Tìm các giá trị duy nhất trong danh sách nhãn
    
    # Khởi tạo một từ điển rỗng có tên label_map. Đây là nơi chúng ta sẽ lưu trữ ánh xạ giữa giá trị nhãn và số.
    label_map = {}  # Tạo bản đồ ánh xạ giữa giá trị nhãn và số
    for i, label in enumerate(unique_labels):
        # label_map[label] = i: Trong mỗi lần lặp, hàm này thêm một cặp khóa-giá trị vào từ điển label_map, 
        # trong đó khóa là giá trị nhãn và giá trị tương ứng là chỉ số của nó trong danh sách các giá trị duy nhất.
        label_map[label] = i
    
    # Cuối cùng, hàm trả về từ điển label_map, trong đó chứa ánh xạ giữa giá trị nhãn và số tương ứng.
    return label_map

ever_married_encoder = label_encoder(data_cleaned['ever_married'])
gender_encoder = label_encoder(data_cleaned['gender'])
work_type_encoder = label_encoder(data_cleaned['work_type'])
residence_type_encoder = label_encoder(data_cleaned['Residence_type'])
smoking_status_encoder = label_encoder(data_cleaned['smoking_status'])

# Hàm predict_stroke() được sử dụng để dự đoán nguy cơ bị đột quỵ dựa trên thông tin bệnh nhân đầu vào.
def predict_stroke(data):
    # Xử lý dữ liệu giống như khi huấn luyện mô hình
    gender = gender_encoder[data['gender']]
    ever_married = ever_married_encoder[data['ever_married']]
    work_type = work_type_encoder[data['work_type']]
    residence_type = residence_type_encoder[data['Residence_type']]
    smoking_status = smoking_status_encoder[data['smoking_status']]
    age = float(data['age'])  # Chuyển đổi sang kiểu dữ liệu float
    bmi = float(data['bmi'])   # Chuyển đổi sang kiểu dữ liệu float
    avg_glucose_level = float(data['avg_glucose_level'])  # Chuyển đổi sang kiểu dữ liệu float
    hypertension = int(data['hypertension'])
    heart_disease = int(data['heart_disease'])

    # Thông tin bệnh nhân được chuyển đổi sang các giá trị mã hoá tương ứng và được đặt vào danh sách X
    # X được chuyển đổi thành một tensor và được đưa vào mô hình để dự đoán.
    X = [[gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status]]

    # Dự đoán kết quả
    X_tensor = tf.convert_to_tensor(X, dtype=tf.float32)
    prediction = loaded_model.predict(X_tensor)
    # In giá trị dự đoán để kiểm tra
    print(prediction)

    # Dự đoán được chuyển đổi thành nhãn "Có Bệnh" hoặc "Không Bệnh" dựa trên một ngưỡng xác định.
    if prediction[0] == 1:
        result = 'Khả Năng Có Bệnh'
    else:
        result = 'Khả Năng Không Bệnh'

    return result


def connect_to_database():
    # Kết nối đến cơ sở dữ liệu SQL Server
    connection_string = "DRIVER={SQL Server};SERVER=ADMIN-PC\SQLEXPRESS;DATABASE=dulieudotquy;UID=sa;PWD=123"
    conn = pyodbc.connect(connection_string)
    
    # Trả về kết nối
    return conn

def query_data():
    # Kết nối đến cơ sở dữ liệu
    conn = connect_to_database()
    
    # Tạo câu truy vấn SELECT
    query = "SELECT * FROM ThongTinKhamBenh_BN"
    
    # Thực thi câu truy vấn và lấy dữ liệu
    data = pd.read_sql(query, conn)
    
    # Đóng kết nối
    conn.close()
    
    # Trả về dữ liệu
    return data

def save_prediction_to_table(conn, data):
    query = "INSERT INTO ThongTinKhamBenh (Gender, Age, Hypertension, HeartDisease, EverMarried, WorkType, ResidenceType, AvgGlucoseLevel, BMI, SmokingStatus, Result) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()


# Hiển thị các phần tử của trang dự đoán
def show_chandoan_page():

    st.markdown('<h1 class="noidung">Nhập thông tin bệnh nhân để dự đoán xem có nguy cơ bị đột quỵ hay không?</h1>', unsafe_allow_html=True)
    st.markdown(
    """
    <style>
    /* Căn giữa tiêu đề */
    .noidung {
        font-size: 20px;
        font-family: 'Times New Roman', sans-serif;
        color: #009966;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    # Tạo các trường đầu vào cho người dùng nhập thông tin
    gender = st.selectbox('Giới tính', list(gender_encoder.keys()))
    age = st.number_input('Tuổi', min_value=0, max_value=120, value=30)
    hypertension = st.selectbox('Có bị tăng huyết áp không?', [1, 0])
    heart_disease = st.selectbox('Có bị bệnh tim không?', [1, 0])
    ever_married = st.selectbox('Đã kết hôn chưa?', list(ever_married_encoder.keys()))
    work_type = st.selectbox('Loại công việc', list(work_type_encoder.keys()))
    residence_type = st.selectbox('Loại nơi ở', list(residence_type_encoder.keys()))
    avg_glucose_level = st.number_input('Mức đường huyết trung bình', min_value=0.0, max_value=300.0, value=100.0)
    bmi = st.number_input('Chỉ số khối cơ thể (BMI)', min_value=0.0, max_value=100.0, value=25.0)
    smoking_status = st.selectbox('Tình trạng hút thuốc',  list(smoking_status_encoder.keys()))

    # Xử lý dự đoán khi người dùng nhấp vào nút "Dự đoán"
    if st.button('Dự đoán'):
        data = {
            'gender': gender,
            'age': age,
            'hypertension': hypertension,
            'heart_disease': heart_disease,
            'ever_married': ever_married,
            'work_type': work_type,
            'Residence_type': residence_type,
            'avg_glucose_level': avg_glucose_level,
            'bmi': bmi,
            'smoking_status': smoking_status,
        }
        result = predict_stroke(data)
        st.write("Kết quả dự đoán: ", result)
        conn = connect_to_database()
        data = (gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status, result)
        save_prediction_to_table(conn, data)
        conn.close()
        # Hiển thị thông báo thành công
        st.success("Dữ liệu đã được lưu vào cơ sở dữ liệu SQL Server!")

def main():
    if loaded_model is not None:
        show_chandoan_page()

if __name__ == '__main__':
    main()

