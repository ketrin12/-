import streamlit as st

st.set_page_config(
    page_title="Галерея | Ketrin Plase",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Жестко скрываем меню и красим фон в темный
st.markdown("""
<style>
    [data-testid="stSidebar"], 
    [data-testid="collapsedControl"], 
    [data-testid="stHeader"] {
        display: none !important;
    }
    .stApp, .main, [data-testid="stAppViewContainer"] {
        background-color: #140f0d !important;
    }
    h1, h2, h3, h4, p, span, div { 
        color: #f5ebe6 !important; 
        font-family: 'Georgia', serif !important; 
    }
    .stButton > button {
        background-color: #2d2320 !important;
        color: #bc987e !important;
        border: 1px solid #bc987e !important;
    }
</style>
""", unsafe_allow_html=True)

# Кнопка возврата на главную
if st.button("⬅️ Вернуться на главную", use_container_width=True):
    st.switch_page("app.py")

# Наш красивый заголовок
st.markdown("<h2 style='text-align: center; color: #dfba9d;'>🌸 Галерея нашего салона</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Создаем 3 колонки: боковые для отступов, средняя для фото
# Числа [1, 2, 1] значат, что фотка по центру займет половину экрана, а бока — по четверти
gal_col1 = st.columns([1, 2, 1])

with gal_col1:
    # Переносим нашу картинку в центральную колонку
    st.image(
        "images/bg.jpg.webp", 
        caption="Ну ты и негодяй!!!!!!!!!", 
        use_container_width=True
    )