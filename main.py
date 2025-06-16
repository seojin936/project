import streamlit as st

# BMI 계산 함수
def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2

# 사용자 인터페이스 설정
st.title("BMI 계산기")

# 사용자 입력 받기
with st.form("bmi_form"):
    weight = st.number_input("체중 (kg)", min_value=1, max_value=200, step=0.1)
    height = st.number_input("키 (cm)", min_value=50, max_value=250, step=1)
    submitted = st.form_submit_button("계산")

# BMI 계산 및 결과 출력
if submitted:
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"당신의 BMI는 {bmi:.2f}입니다.")

        # BMI 범위에 따른 건강 상태 평가
        if bmi < 18.5:
            st.warning("저체중입니다.")
        elif 18.5 <= bmi < 23.0:
            st.success("정상 체중입니다.")
        elif 23.0 <= bmi < 25.0:
            st.warning("과체중입니다.")
        else:
            st.error("비만입니다.")
    else:
        st.error("체중과 키를 올바르게 입력해주세요.")
