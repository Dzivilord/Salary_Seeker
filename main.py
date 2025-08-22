from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import unicodedata
import joblib
import pandas as pd
app = FastAPI()

model_path = "salary_model.pkl"
model = joblib.load(model_path)

scaler_path="salary_scaler.pkl"
scaler=joblib.load(scaler_path)
columns = [
    "Experience", "Education_Levels", "Job_Level",
    "Employment_Type__Part-time", "Employment_Type__Internship",
    "Employment_Type__Freelance", "Employment_Type__Official",

    "Industry__Bán_Hàng_Kỹ_Thuật", "Industry__Not_specified", "Industry__Thương_mại_điện_tử",
    "Industry__accounting_auditing", "Industry__administrative_secretarial",
    "Industry__advertising_public_relations_media", "Industry__agriculture",
    "Industry__aquaculture_seafood", "Industry__architecture", "Industry__aviation",
    "Industry__banking", "Industry__biotechnology", "Industry__chemistry",
    "Industry__construction", "Industry__consulting", "Industry__customer_service",
    "Industry__education_training", "Industry__electricity_electronics_refrigeration_/_Điện_công_nghiệp",
    "Industry__entertainment", "Industry__environment", "Industry__event_organization",
    "Industry__executive_management", "Industry__finance_investment",
    "Industry__fine_arts_art_design", "Industry__food_beverages",
    "Industry__food_technology_nutrition", "Industry__forestry",
    "Industry__healthcare_medical_/_Thẩm_mỹ_/_Làm_đẹp",
    "Industry__household_goods_personal_care", "Industry__human_resources",
    "Industry__import_export", "Industry__insurance", "Industry__interior_exterior_design",
    "Industry__irrigation", "Industry__it_hardware_networking", "Industry__it_software",
    "Industry__law_legal", "Industry__library", "Industry__livestock_veterinary",
    "Industry__maintenance_repair", "Industry__manual_labor",
    "Industry__manufacturing_operations", "Industry__maritime", "Industry__marketing",
    "Industry__mechanical_automotive_automation", "Industry__minerals",
    "Industry__new_graduates_internship", "Industry__ngo_non_profit",
    "Industry__occupational_safety", "Industry__oil_gas", "Industry__online_marketing",
    "Industry__other_industries", "Industry__pharmaceuticals/_Hóa_Mỹ_Phẩm",
    "Industry__postal_telecommunications", "Industry__printing_publishing",
    "Industry__procurement_supplies", "Industry__quality_management_qaqc",
    "Industry__real_estate", "Industry__restaurant_hotel", "Industry__retail_wholesale",
    "Industry__sales_business", "Industry__securities", "Industry__security_protection",
    "Industry__statistics", "Industry__surveying_geology",
    "Industry__television_journalism_editing", "Industry__textile_leather_fashion",
    "Industry__tourism", "Industry__translation_interpretation",
    "Industry__transportation_logistics_warehouse", "Industry__wooden_goods",

    "Welfare__allowance", "Welfare__allowance_thâm_niên", "Welfare__annual_leave",
    "Welfare__bonus", "Welfare__business_trip_expenses", "Welfare__healthcare",
    "Welfare__insurance", "Welfare__laptop", "Welfare__not_specified",
    "Welfare__overseas_travel", "Welfare__salary_increase", "Welfare__shuttle_service",
    "Welfare__sports_club", "Welfare__training", "Welfare__travel", "Welfare__uniform",

    "Location_An_Giang", "Location_Attapeu", "Location_Ba_Ria_-_Vung_Tau",
    "Location_Bac_Can", "Location_Bac_Giang", "Location_Bac_Lieu", "Location_Bac_Ninh",
    "Location_Ben_Tre", "Location_Binh_Duong", "Location_Binh_Phuoc",
    "Location_Binh_Thuan", "Location_Binh_Đinh", "Location_Ca_Mau", "Location_Can_Tho",
    "Location_Cao_Bang", "Location_Chicago", "Location_Dak_Lak", "Location_Dak_Nong",
    "Location_Gia_Lai", "Location_Ha_Giang", "Location_Ha_Nam", "Location_Ha_Noi",
    "Location_Ha_Tinh", "Location_Hai_Duong", "Location_Hai_Phong", "Location_Hau_Giang",
    "Location_Ho_Chi_Minh", "Location_Hoa_Binh", "Location_Hung_Yen", "Location_Indonesia",
    "Location_Khac", "Location_Khanh_Hoa", "Location_Kien_Giang", "Location_Kon_Tum",
    "Location_Kratie", "Location_Kv_Bac_Trung_Bo", "Location_Kv_Nam_Trung_Bo",
    "Location_Kv_Tay_Nguyen", "Location_Kv_Đong_Nam_Bo", "Location_Kyrgyzstan",
    "Location_Lai_Chau", "Location_Lam_Đong", "Location_Lang_Son", "Location_Lao_Cai",
    "Location_Long_An", "Location_Nam_Đinh", "Location_Nghe_An", "Location_Ninh_Binh",
    "Location_Ninh_Thuan", "Location_Not_Specified", "Location_Paris",
    "Location_Philippines", "Location_Phnompenh", "Location_Phu_Tho", "Location_Phu_Yen",
    "Location_Quang_Binh", "Location_Quang_Nam", "Location_Quang_Ngai",
    "Location_Quang_Ninh", "Location_Quang_Tri", "Location_Quoc_Te", "Location_Singapore",
    "Location_Soc_Trang", "Location_Son_La", "Location_Tay_Ninh", "Location_Thai_Binh",
    "Location_Thai_Nguyen", "Location_Thanh_Hoa", "Location_Thua_Thien-_Hue",
    "Location_Tien_Giang", "Location_Toan_Quoc", "Location_Tokyo", "Location_Tra_Vinh",
    "Location_Tuyen_Quang", "Location_Vientiane", "Location_Vinh_Long",
    "Location_Vinh_Phuc", "Location_Yen_Bai", "Location_Đa_Nang", "Location_Đien_Bien",
    "Location_Đong_Bang_Song_Cuu_Long", "Location_Đong_Bang_Song_Hong",
    "Location_Đong_Nai", "Location_Đong_Thap",

    "Language_requirement",
    "Gender_requirement_both", "Gender_requirement_female", "Gender_requirement_male"
]

# Định nghĩa schema JSON
class JobInfo(BaseModel):
    experience: int
    location: list[str]
    employment_type: list[str]
    education_level: str
    job_level: str
    welfares: list[str]
    industry: list[str]
    second_language: str
    gender: str

# Location Transfer
def remove_diacritics(text):
    return ''.join(
        c.replace(" ","_") for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    
# Job Level Transfer
def job_level_transfer(job_level):
    job_level_list = {
        'mới tốt nghiệp': 1,
        'sinh viên/ thực tập sinh': 1,
        'nhân viên': 2,
        'trưởng nhóm': 3,
        'trưởng nhóm / giám sát': 3,
        'quản lý': 4,
        'phó giám đốc': 5,
        'giám đốc': 6,
        'tổng giám đốc': 7,
        'not specified': 0
    }
    return job_level_list.get(job_level.lower(), 0)

def education_transfer(education_level):
    education_levels_dict = {
    'trung học': 1,
    'trung cấp': 2,
    'cao đẳng': 3,
    'đại học': 4,
    'sau đại học': 5,
    }
    return education_levels_dict.get(education_level.lower(), 0)

def employment_type_transfer(employment_type_list):
    employmentType_translation_dict = {
        'thực tập': 'Internship',
        'bán thời gian': 'Part-time',
        'chính thức': 'Official',
        'thời vụ/ nghề tự do': 'Freelance',
    }
    result = []
    for et in employment_type_list:
        translated = employmentType_translation_dict.get(et.lower().strip(), None)
        if translated:
            result.append(translated)
    return result

def industry_transfer(industry):
    industry_translation_dict = {
    'Bán hàng / Kinh doanh': 'sales_business',
    'Ngân hàng': 'banking',
    'Dịch vụ khách hàng': 'customer_service',
    'Tiếp thị / Marketing': 'marketing',
    'Bán lẻ / Bán sỉ': 'retail_wholesale',
    'Tài chính / Đầu tư': 'finance_investment',
    'Kế toán / Kiểm toán': 'accounting_auditing',
    'Điện / Điện tử / Điện lạnh': 'electricity_electronics_refrigeration',
    'Tư vấn': 'consulting',
    'Sản xuất / Vận hành sản xuất': 'manufacturing_operations',
    'Cơ khí / Ô tô / Tự động hóa': 'mechanical_automotive_automation',
    'Xây dựng': 'construction',
    'Hành chính / Thư ký': 'administrative_secretarial',
    'Giáo dục / Đào tạo': 'education_training',
    'CNTT - Phần mềm': 'it_software',
    'Bất động sản': 'real_estate',
    'Nhân sự': 'human_resources',
    'Quản lý điều hành': 'executive_management',
    'Y tế / Chăm sóc sức khỏe': 'healthcare_medical',
    'Vận chuyển / Giao nhận /  Kho vận': 'transportation_logistics_warehouse',
    'Thực phẩm & Đồ uống': 'food_beverages',
    'Dệt may / Da giày / Thời trang': 'textile_leather_fashion',
    'Bảo trì / Sửa chữa': 'maintenance_repair',
    'Quản lý chất lượng (QA/QC)': 'quality_management_qaqc',
    'Tiếp thị trực tuyến': 'online_marketing',
    'Xuất nhập khẩu': 'import_export',
    'Not Found': 'not_found',
    'Quảng cáo / Đối ngoại / Truyền Thông': 'advertising_public_relations_media',
    'Dược phẩm': 'pharmaceuticals',
    'Biên phiên dịch': 'translation_interpretation',
    'Nhà hàng / Khách sạn': 'restaurant_hotel',
    'Mỹ thuật / Nghệ thuật / Thiết kế': 'fine_arts_art_design',
    'Kiến trúc': 'architecture',
    'Luật / Pháp lý': 'law_legal',
    'Bảo hiểm': 'insurance',
    'Ngành khác': 'other_industries',
    'Thu mua / Vật tư': 'procurement_supplies',
    'CNTT - Phần cứng / Mạng': 'it_hardware_networking',
    'Bưu chính viễn thông': 'postal_telecommunications',
    'Nội ngoại thất': 'interior_exterior_design',
    'Mới tốt nghiệp / Thực tập': 'new_graduates_internship',
    'Du lịch': 'tourism',
    'Truyền hình / Báo chí / Biên tập': 'television_journalism_editing',
    'Hóa học': 'chemistry',
    'Lao động phổ thông': 'manual_labor',
    'Công nghệ thực phẩm / Dinh dưỡng': 'food_technology_nutrition',
    'Chứng khoán': 'securities',
    'Môi trường': 'environment',
    'Hàng gia dụng / Chăm sóc cá nhân': 'household_goods_personal_care',
    'Công nghệ sinh học': 'biotechnology',
    'An toàn lao động': 'occupational_safety',
    'Đồ gỗ': 'wooden_goods',
    'Tổ chức sự kiện': 'event_organization',
    'Nông nghiệp': 'agriculture',
    'Thống kê': 'statistics',
    'In ấn / Xuất bản': 'printing_publishing',
    'Giải trí': 'entertainment',
    'An Ninh / Bảo Vệ': 'security_protection',
    'Dầu khí': 'oil_gas',
    'Hàng không': 'aviation',
    'Hàng hải': 'maritime',
    'Chăn nuôi / Thú y': 'livestock_veterinary',
    'Thủy sản / Hải sản': 'aquaculture_seafood',
    'Trắc địa / Địa Chất': 'surveying_geology',
    'Khoáng sản': 'minerals',
    'Lâm Nghiệp': 'forestry',
    'Phi chính phủ / Phi lợi nhuận': 'ngo_non_profit',
    'Thủy lợi': 'irrigation',
    'Thư viện': 'library'
    }
    result = []
    for et in industry:
        translated = industry_translation_dict.get(et, None)
        if translated:
            result.append(translated)
    return result


def welfares_transfer(welfares):
    welfare_translation_dict = {
    'Chế độ thưởng': 'bonus',
    'Chế độ bảo hiểm': 'insurance',
    'Đào tạo': 'training',
    'Tăng lương': 'salary_increase',
    'Chăm sóc sức khỏe': 'healthcare',
    'Du Lịch': 'travel',
    'Nghỉ phép năm': 'annual_leave',
    'Phụ cấp': 'allowance',
    'Đồng phục': 'uniform',
    'Công tác phí': 'business_trip_expenses',
    'Laptop': 'laptop',
    'Phụ cấp thâm niên': 'seniority_allowance',
    'CLB thể thao': 'sports_club',
    'Du lịch nước ngoài': 'overseas_travel',
    'Xe đưa đón': 'shuttle_service',
    'Not specified': 'not_specified'
    }
    result=[]
    for wel in welfares:
        translated_welfare=welfare_translation_dict.get(wel)
        if wel:
            result.append(translated_welfare)
    return result
@app.post("/predict")



def predict_salary(info: JobInfo):
    # with open("salary_model.pkl", "rb") as f:
    #     model = pickle.load(f)
    
    experience=info.experience
    location=info.location
    employment_type=info.employment_type
    education_level=info.education_level
    job_level=info.job_level
    welfares=info.welfares
    industry=info.industry
    second_language=info.second_language
    gender_requirement=info.gender
    
    experience_data=experience
    
    job_level_data=job_level_transfer(job_level)
    education_level_data=education_transfer(education_level)
    employment_type=employment_type_transfer(employment_type)
    
    employment_types_data = {
        'Employment_Type_Internship': 1 if any("Internship" in et for et in employment_type) else 0,
        'Employment_Type_Part-time': 1 if any("Part-time" in et for et in employment_type) else 0,
        'Employment_Type_Official': 1 if any("Official" in et for et in employment_type) else 0,
        'Employment_Type_Freelance': 1 if any("Freelance" in et for et in employment_type) else 0,
    }
    
    industries=industry_transfer(industry)
    industries_data = {
        col: 1 if (any(f"Industry__{indus}" == col for indus in industries)) else 0
        for col in columns if "Industry" in col
    }
    
    locations = [remove_diacritics(loc) for loc in location]
    locations_data = {
        col: 1 if (any(f"Location_{loc}" == col for loc in locations)) else 0
        for col in columns if "Location" in col
    }
    welfares=welfares_transfer(welfares)
    welfares_data = {
        col: 1 if (any(f"Welfare__{wel}" == col for wel in welfares)) else 0
        for col in columns if "Welfare" in col
    }
    
    input_data={
        'Experience':experience_data,
        'Education_Level': education_level_data,
        'Job_Level':job_level_data,
    }
    
    second_language_data= 1 if second_language=='Có' else 0
    
    gender_data = {
            'Gender_requirement_both': 1 if gender_requirement == 'Không yêu cầu' else 0,
            'Gender_requirement_female': 1 if gender_requirement == 'Nữ' else 0,
            'Gender_requirement_male': 1 if gender_requirement == 'Nam' else 0,
        }
    input_data.update(employment_types_data)
    input_data.update(industries_data)
    input_data.update(welfares_data)
    input_data.update(locations_data)
    
    
    input_data.update({'Language_requirement':second_language_data})
    
    input_df = pd.DataFrame([input_data])


        
    input_df = input_df.reindex(columns=columns, fill_value=0)
    prediction_scaled = model.predict(input_df)[0]
    prediction = scaler.inverse_transform([[prediction_scaled]])[0][0]
    return {
        "result": prediction
    }

