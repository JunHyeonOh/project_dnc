import streamlit as st

st.set_page_config(
    page_title="뉴스 수집기",
    page_icon="./images/favicon.png"
)

st.title("News Collector")
st.text("Daum 뉴스를 수집합니다.")

with st.form(key="form"):
    category = st.text_input("수집하고 싶은 뉴스 카테고리를 선택하세요.").strip()
    submitted = st.form_submit_button("입력")

if submitted:
    st.write(category)