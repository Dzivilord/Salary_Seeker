import streamlit as st 
import pandas as pd
import csv
import requests
st.title('💰 PREPARE FOR YOUR CAREER- HOW MUCH YOU GET PAID !!')

location_list = [
    # 63 tỉnh/thành
    "Hải Dương",
    "Long An",
    "Hà Nội",
    "Hồ Chí Minh",
    "Bình Dương",
    "Đồng Nai",
    "Quảng Ngãi",
    "Vĩnh Long",
    "Lâm Đồng",
    "Cần Thơ",
    "Bắc Ninh",
    "Đắk Lắk",
    "Gia Lai",
    "Bắc Giang",
    "Bình Thuận",
    "Tây Ninh",
    "Bà Rịa - Vũng Tàu",
    "Hà Nam",
    "Thái Bình",
    "Bạc Liêu",
    "Thanh Hóa",
    "Bình Định",
    "Trà Vinh",
    "Hòa Bình",
    "Đà Nẵng",
    "Hưng Yên",
    "Hải Phòng",
    "Kiên Giang",
    "Vĩnh Phúc",
    "Hà Giang",
    "Tuyên Quang",
    "Điện Biên",
    "Nam Định",
    "Lạng Sơn",
    "Nghệ An",
    "Quảng Trị",
    "Quảng Ninh",
    "Ninh Thuận",
    "Đồng Tháp",
    "Quảng Nam",
    "Thừa Thiên Huế",
    "Tiền Giang",
    "Khánh Hòa",
    "Phú Yên",
    "Quảng Bình",
    "Hậu Giang",
    "Bình Phước",
    "Phú Thọ",
    "Ninh Bình",
    "Thái Nguyên",
    "Bắc Kạn",
    "Sơn La",
    "Hà Tĩnh",
    "Yên Bái",
    "Cà Mau",
    "An Giang",
    "Bến Tre",
    "Lào Cai",
    "Sóc Trăng",
    "Cao Bằng",
    "Đắk Nông",
    "Kon Tum",
    "Lai Châu",
    'Nam Đinh'
    
    # Các vùng trong nước
    "Khu vực Đông Nam Bộ",
    "Khu vực Tây Nguyên",
    "Khu vực Nam Trung Bộ",
    "Khu vực Bắc Trung Bộ",
    "Đồng bằng Sông Cửu Long",
    "Toàn quốc",
    "Khác",
    "Không xác định",
    
    # Quốc tế
    "Svay Rieng",
    "Tokyo",
    "Xiangkhouang",
    "Champasak",
    "Yokohama",
    "Hokkaido",
    "Malaysia",
    "Attapeu",
    "Bangkok",
    "Kratie",
    "Phnom Penh",
    "Vientiane",
    "Kuala Lumpur",
    "Quốc tế",
    "Singapore",
    "Indonesia",
    "Kyrgyzstan",
    "Chicago",
    "Đồng bằng Sông Hồng",
    "Philippines"
]

   
industry_list = [
    'Bán hàng / Kinh doanh','Ngân hàng',
    'Dịch vụ khách hàng','Tiếp thị / Marketing',
    'Bán lẻ / Bán sỉ','Tài chính / Đầu tư','Kế toán / Kiểm toán',
    'Điện / Điện tử / Điện lạnh','Tư vấn',
    'Sản xuất / Vận hành sản xuất','Cơ khí / Ô tô / Tự động hóa',
    'Xây dựng','Hành chính / Thư ký',
    'Giáo dục / Đào tạo','CNTT - Phần mềm','Bất động sản', 'Nhân sự','Quản lý điều hành',
    'Y tế / Chăm sóc sức khỏe','Vận chuyển / Giao nhận /  Kho vận','Thực phẩm & Đồ uống',
    'Dệt may / Da giày / Thời trang','Bảo trì / Sửa chữa','Quản lý chất lượng (QA/QC)',
    'Tiếp thị trực tuyến','Xuất nhập khẩu',
    'Not Found','Quảng cáo / Đối ngoại / Truyền Thông',
    'Dược phẩm','Biên phiên dịch',
    'Nhà hàng / Khách sạn','Mỹ thuật / Nghệ thuật / Thiết kế','Kiến trúc',
    'Luật / Pháp lý','Bảo hiểm','Ngành khác','Thu mua / Vật tư','CNTT - Phần cứng / Mạng','Bưu chính viễn thông',
    'Nội ngoại thất','Mới tốt nghiệp / Thực tập','Du lịch','Truyền hình / Báo chí / Biên tập','Hóa học','Lao động phổ thông',
    'Công nghệ thực phẩm / Dinh dưỡng','Chứng khoán',
    'Môi trường','Hàng gia dụng / Chăm sóc cá nhân','Công nghệ sinh học','An toàn lao động',
    'Đồ gỗ','Tổ chức sự kiện','Nông nghiệp','Thống kê','In ấn / Xuất bản',
    'Giải trí','An Ninh / Bảo Vệ','Dầu khí','Hàng không','Hàng hải','Chăn nuôi / Thú y','Thủy sản / Hải sản',
    'Trắc địa / Địa Chất','Khoáng sản','Lâm Nghiệp','Phi chính phủ / Phi lợi nhuận',
    'Thủy lợi','Thư viện'
]
welfare_list = ['Chế độ thưởng','Chế độ bảo hiểm',
    'Đào tạo','Tăng lương','Chăm sóc sức khỏe',
    'Du Lịch','Nghỉ phép năm','Phụ cấp','Đồng phục',
    'Công tác phí','Laptop','Phụ cấp thâm niên',
    'CLB thể thao', 'Du lịch nước ngoài','Xe đưa đón',
    'Không xác định'
]


employment_type_list=['Thực Tập', 'Bán Thời Gian', 'Chính Thức', 'Thời Vụ/ Nghề Tự Do']
education_level_list=['Không Xác Định','Trung Học','Trung cấp','Đại Học','Sau Đại Học']
job_level_list=['Thực Tập Sinh','Nhân Viên','Trưởng Nhóm','Quản Lý','Phó Giám Đốc','Giám Đốc']
st.title("🔮 Dự đoán mức lương")
col1, col2 = st.columns(2)

import streamlit as st

st.set_page_config(page_title="Dự đoán mức lương", page_icon="💰", layout="wide")

# ---- HEADER ----
st.markdown(
    """
    <div style="background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
                padding: 20px; border-radius: 12px; text-align: center; color: white;">
        <h1>💰 Dự đoán mức lương</h1>
        <p style="font-size:18px;">Nhập thông tin nghề nghiệp của bạn và nhận dự đoán ngay 🔮</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")  # spacing

# ---- FORM SECTION ----
st.markdown("### 📝 Thông tin cá nhân & công việc")
col1, col2 = st.columns(2)

with col1:
    experience = st.number_input('⏳ Số năm kinh nghiệm', min_value=0, max_value=50, step=1, help="Nhập số năm bạn đã làm việc trong ngành")
    location = st.multiselect('📍 Địa điểm làm việc', location_list, help="Chọn nơi bạn muốn làm việc")
    employment_type = st.multiselect('💼 Hình thức việc làm', employment_type_list, help="Chọn loại hình công việc")
    education_level = st.selectbox('🎓 Trình độ học vấn', education_level_list, help="Chọn trình độ học vấn cao nhất của bạn")

with col2:
    job_level = st.selectbox('📊 Cấp bậc công việc', job_level_list, help="Chọn cấp bậc phù hợp với bạn")
    welfares = st.multiselect('🎁 Phúc lợi', welfare_list, help="Chọn các phúc lợi bạn mong muốn")
    industry = st.multiselect('🏢 Ngành nghề', industry_list, help="Chọn ngành nghề bạn quan tâm")
    second_language = st.selectbox('🌐 Ngoại ngữ', ['Có', 'Không yêu cầu'], help="Có yêu cầu ngoại ngữ không?")
    gender = st.selectbox('👤 Giới tính', ['Nam', 'Nữ', 'Không yêu cầu'], help="Chọn giới tính nếu có yêu cầu")

# ---- VALIDATION ----
required = {"📍 Địa điểm làm việc": location, "🎁 Phúc lợi": welfares, "🏢 Ngành nghề": industry}
missing = [k for k, v in required.items() if not v]
all_selected = len(missing) == 0

label = "🚀 Dự đoán mức lương" if all_selected else "⚠️ Chọn thêm: " + ", ".join(missing)
submit = st.button(label, disabled=not all_selected)

if not all_selected:
    st.info("🔎 Bạn cần nhập thêm: " + " • ".join(missing))

# ---- RESULT SECTION ----
if submit:
    # Gom dữ liệu thành JSON
    payload = {
        "experience": experience,
        "location": location,
        "employment_type": employment_type,
        "education_level": education_level,
        "job_level": job_level,
        "welfares": welfares,
        "industry": industry,
        "second_language": second_language,
        "gender": gender
    }

    # Gửi sang FastAPI (ví dụ: chạy ở localhost:8000)
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        # Hiển thị kết quả dự đoán mức lương với định dạng đẹp
        

        st.markdown(
            f"""
            <div style="background: linear-gradient(90deg, #43cea2 0%, #185a9d 100%);
                padding: 24px; border-radius: 16px; text-align: center; color: white;">
            <h2>💸 Mức lương dự đoán của bạn:</h2>
            <p style="font-size:32px; font-weight:bold;">
                {round(result.get('result')):,.0f} VNĐ/tháng
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )


        # Hiển thị lại thông tin đã nhập
        st.markdown("### 📝 Thông tin bạn đã nhập")
        st.markdown(
            f"""
            <ul>
            <li><b>Số năm kinh nghiệm:</b> {experience}</li>
            <li><b>Địa điểm làm việc:</b> {', '.join(location)}</li>
            <li><b>Hình thức việc làm:</b> {', '.join(employment_type)}</li>
            <li><b>Trình độ học vấn:</b> {education_level}</li>
            <li><b>Cấp bậc công việc:</b> {job_level}</li>
            <li><b>Phúc lợi:</b> {', '.join(welfares)}</li>
            <li><b>Ngành nghề:</b> {', '.join(industry)}</li>
            <li><b>Ngoại ngữ:</b> {second_language}</li>
            <li><b>Giới tính:</b> {gender}</li>
            </ul>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Có lỗi xảy ra khi gửi dữ liệu đến server.")