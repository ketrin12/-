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
        /* Стилизация карточек женщин */
        .woman-card {
            background-color: #f4f7f4;
            padding: 25px;
            border-radius: 12px;
            border-left: 6px solid #246b34; /* Зеленая полоса слева */
            margin-bottom: 30px;
        }
        .woman-name {
            color: #bd1c1c !important;
            font-size: 2rem !important;
            font-weight: 700 !important;
            margin-bottom: 10px;
        }
        .woman-desc {
            font-size: 1.3rem !important;
            line-height: 1.5 !important;
            color: #333333;
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
    st.markdown("<h1 class='main-title'>Женщины Беларуси</h1>", unsafe_allow_html=True)
    
    st.markdown(
        "<p class='large-text'><b>Здравствуй, Пользователь!</b><br>"
        "В 2026 году в Республике Беларусь отмечается год Женщины. "
        "Не хотели бы вы прочитать информацию о женщинах Беларуси?</p>", 
        unsafe_allow_html=True
    )
    
    st.markdown("<h3 style='color: #246b34; margin-top: 40px;'>📋 Быстрый переход по разделам:</h3>", unsafe_allow_html=True)
    
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
    st.markdown("<h1 class='main-title'>🇧🇾 Выдающиеся женщины в истории Беларуси</h1>", unsafe_allow_html=True)
    st.markdown("<p class='large-text'>Узнайте о шести великих женщинах, чьи достижения и подвиги прославили белорусскую землю:</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Список из 6 женщин
    women_data = [
        {
            "name": "1. Евфросиния Полоцкая",
            "desc": "Святая покровительница Беларуси, просветительница и первая женщина-дипломат в Восточной Европе. Она открывала школы, основывала монастыри, собирала библиотеки и переписывала книги, заложив фундамент белорусской культуры и образования.",
            "img_placeholder": "photo_euphrosyne.jpg"
        },
        {
            "name": "2. Франциска Урсула Радзивилл",
            "desc": "Первая женщина-драматург в Беларуси и основательница знаменитого Несвижского театра. Писала пьесы, ставила масштабные спектакли и сделала Несвиж одним из главных культурных центров Европы XVIII века.",
            "img_placeholder": "photo_radziwill.jpg"
        },
        {
            "name": "3. Эмилия Плятер",
            "desc": "Белорусская Жанна д'Арк. Графиня и революционерка, которая в XIX веке возглавила собственный партизанский отряд и воевала наравне с мужчинами, став символом мужества, отваги и борьбы за свободу родного края.",
            "img_placeholder": "photo_plater.jpg"
        },
        {
            "name": "4. Софья Ковалевская",
            "desc": "Легендарный математик белорусского происхождения. Она стала первой в мире женщиной — профессором математики и совершила важнейшие открытия в механике и астрономии, доказав всему миру силу женского интеллекта.",
            "img_placeholder": "photo_kovalevskaya.jpg"
        },
        {
            "name": "5. Дарья Домрачева",
            "desc": "Легенда мирового спорта, четырёхкратная олимпийская чемпионка по биатлону и первая женщина, удостоенная высшего звания «Герой Беларуси». Её победы на Олимпийских играх прославили современную Беларусь на весь мир.",
            "img_placeholder": "photo_domracheva.jpg"
        },
        {
            "name": "6. Марина Василевская",
            "desc": "Первый космонавт в суверенной истории Беларуси. В 2024 году она совершила полет на Международную космическую станцию (МКС), открыв для белорусских женщин совершенно новую, космическую высоту.",
            "img_placeholder": "photo_vasilevskaya.jpg"
        }
    ]

    # Вывод карточек на экран
    for woman in women_data:
        # Разделяем экран на две колонки для каждой женщины: слева описание, справа будет фото
        col_text, col_img = st.columns([3, 1])
        
        with col_text:
            st.markdown(f"""
                <div class='woman-card'>
                    <div class='woman-name'>{woman['name']}</div>
                    <div class='woman-desc'>{woman['desc']}</div>
                </div>
            """, unsafe_allow_html=True)
            
        with col_img:
            # Пока фоток нет, выводим временную серую плашку. 
            # Когда фотки будут, мы заменим это на st.image(woman['img_placeholder'])
            st.info("Место для фото")

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("⬅️ Назад на главную", use_container_width=True):
        st.session_state.page = "main"
        st.rerun()

# --- СТРАНИЦА С ОБИДКОЙ (НЕТ) ---
elif st.session_state.page == "rejection":
    st.markdown("<h1 class='main-title'>😲 Ой...</h1>", unsafe_allow_html=True)
    st.error("ну ты и негодяй!!!!!")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("⬅️ Исправиться и вернуться", use_container_width=True):
        st.session_state.page = "main"
        st.rerun()
