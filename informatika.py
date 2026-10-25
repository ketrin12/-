import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Эстетика релакса", layout="centered")

# Инициализируем переменную для отслеживания выбора пользователя, если её еще нет
if "page" not in st.session_state:
    st.session_state.page = "main"

# --- ГЛАВНАЯ СТРАНИЦА ---
if st.session_state.page == "main":
    st.markdown("<h4 style='color: #bc987e !important; text-transform: uppercase; letter-spacing: 2px;'>ЭСТЕТИКА РЕЛАКСА</h4>", unsafe_allow_html=True)
    st.title("Здравствуй Пользователь!")
    st.write("**В 2026 году в Республике Беларусь отмечается год Женщины.** Не хотели бы вы прочитать информацию о женщинах Беларуси?")
    
    st.markdown("### 📋 Быстрый переход по разделам:")
    
    # Создаем две кнопки рядом
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("ДА ХОЧУ", use_container_width=True):
            st.session_state.page = "info"
            st.rerun() # Перезапускает интерфейс, чтобы сразу показать новую страницу

    with col2:
        if st.button("НЕТ НЕ ХОЧУ", use_container_width=True):
            st.session_state.page = "rejection"
            st.rerun()

# --- СТРАНИЦА С ИНФОРМАЦИЕЙ (ЕСЛИ НАЖАЛИ ДА) ---
elif st.session_state.page == "info":
    st.title("🇧🇾 Информация о женщинах Беларуси")
    st.write("Здесь вы можете разместить любой ваш текст, факты и статистику о выдающихся женщинах Беларуси.")
    
    # Кнопка возврата назад
    if st.button("⬅️ Назад на главную", use_container_width=True):
        st.session_state.page = "main"
        st.rerun()

# --- СТРАНИЦА С ОБИДКОЙ (ЕСЛИ НАЖАЛИ НЕТ) ---
elif st.session_state.page == "rejection":
    st.title("😲 Ой...")
    st.error("ну ты и негодяй!!!!!")
    
    # Кнопка возврата назад, если пользователь одумается
    if st.button("⬅️ Исправиться и вернуться", use_container_width=True):
        st.session_state.page = "main"
        st.rerun()
