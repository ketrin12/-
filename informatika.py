import streamlit as st

# 1. Настройка страницы (Заголовок вкладки "Женщины Беларуси" и широкий формат экрана)
st.set_page_config(page_title="Женщины Беларуси", layout="wide")

# Кастомные CSS-стили для изменения цветов под стилистику Беларуси и масштабирования
st.markdown("""
    <style>
        /* Стиль для главного заголовка */
        .main-title {
            color: #bd1c1c !important; /* Глубокий красный */
            font-size: 3.5rem !important;
            font-weight: 800 !important;
            margin-bottom: 20px;
        }
        /* Стиль для обычного текста (крупнее на весь экран) */
        .large-text {
            font-size: 1.6rem !important;
            line-height: 1.6 !important;
            color: #2e3d30 !important; /* Темно-зеленый для лучшей читаемости */
        }
        /* Стилизация стандартных кнопок Streamlit */
        div.stButton > button {
            background-color: #246b34 !important; /* Белорусский зеленый */
            color: white !important;
            font-size: 1.4rem !important;
            padding: 15px 30px !important;
            border-radius: 8px !important;
            border: none !important;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color: #bd1c1c !important; /* Красный при наведении */
            box-shadow: 0 4px 12px rgba(189, 28, 28, 0.3);
        }
    </style>
""", unsafe_allow_html=True)

# Инициализируем состояние страниц, если его нет
if "page" not in st.session_state:
    st.session_state.page = "main"

# --- ГЛАВНАЯ СТРАНИЦА ---
if st.session_state.page == "main":
    # Крупный заголовок во весь экран
    st.markdown("<h1 class='main-title'>Женщины Беларуси</h1>", unsafe_allow_html=True)
    
    st.markdown(
        "<p class='large-text'><b>Здравствуй, Пользователь!</b><br>"
        "В 2026 году в Республике Беларусь отмечается год Женщины. "
        "Не хотели бы вы прочитать информацию о женщинах Беларуси?</p>", 
        unsafe_allow_html=True
    )
    
    st.markdown("<h3 style='color: #246b34; margin-top: 40px;'>📋 Быстрый переход по разделам:</h3>", unsafe_allow_html=True)
    
    # Создаем широкие колонки для кнопок во весь экран
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("ДА ХОЧУ", use_container_width=True):
            st.session_state.page = "info"
            st.rerun()

    with col2:
        if st.button("НЕТ НЕ ХОЧУ", use_container_width=True):
            st.session_state.page = "rejection"
            st.rerun()

# --- СТРАНИЦА С ИНФОРМАЦИЕЙ (ДА) ---
elif st.session_state.page == "info":
    st.markdown("<h1 class='main-title'>🇧🇾 Информация о женщинах Беларуси</h1>", unsafe_allow_html=True)
    
    st.markdown(
        "<div class='large-text'>"
        "Здесь будет располагаться масштабная и подробная информация о выдающихся женщинах, "
        "их достижениях в истории, науке, культуре и спорте Республики Беларусь. "
        "Текст теперь адаптирован под широкий формат экрана и легко читается."
        "</div>", 
        unsafe_allow_html=True
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("⬅️ Назад на главную", use_container_width=True):
        st.session_state.page = "main"
        st.rerun()

# --- СТРАНИЦА С ОБИДКОЙ (НЕТ) ---
elif st.session_state.page == "rejection":
    st.markdown("<h1 class='main-title'>😲 Ой...</h1>", unsafe_allow_html=True)
    
    # Красная плашка с крупным текстом ошибки
    st.error("ну ты и негодяй!!!!!")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("⬅️ Исправиться и вернуться", use_container_width=True):
        st.session_state.page = "main"
        st.rerun()
