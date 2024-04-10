import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from PIL import Image

im = Image.open("imgs/favicon.ico")
st.set_page_config(
    page_title="Champion Edge", page_icon=im, initial_sidebar_state="collapsed"
)

tab1, tab2, tab3 = st.tabs(["Intro", "Winning Prediction", "Champion Recommendation"])

st.markdown(
    """
    <style>
    .custom-text {
        color: #9c9d9f;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
champion_list = [
    "Ahri",
    "Akali",
    "Alistar",
    "Amumu",
    "Anivia",
    "Annie",
    "Ashe",
    "Azir,Akshan",
    "Aurelion sol",
    "Aphelios",
    "Aphelios",
    "Blitzcrank",
    "Brand",
    "Braum",
    "Bard",
    "Belveth",
    "Briar",
    "Caitlyn",
    "Cassiopeia",
    "Cho'Gath",
    "Corki",
    "Camille",
    "Darius",
    "Diana",
    "Dr. Mundo",
    "Draven",
    "Elise",
    "Evelynn",
    "Ekko",
    "Ezreal",
    "Fiddlesticks",
    "Fiora",
    "Fizz",
    "Galio",
    "Gangplank",
    "Garen",
    "Gnar",
    "Gragas",
    "Graves",
    "Gwen",
    "Hecarim",
    "Heimerdinger",
    "Hwei",
    "Irelia",
    "Illaoi",
    "Ivern",
    "Janna",
    "Jarvan IV",
    "Jax",
    "Jayce",
    "Jinx",
    "Jhin",
    "Kalista",
    "Karma",
    "Karthus",
    "Kassadin",
    "Katarina",
    "Kindred",
    "Kayle",
    "Kennen",
    "Kha'Zix",
    "Kog'Maw",
    "Kled",
    "Kayn",
    "Kai'sa",
    "K’Sante",
    "LeBlanc",
    "Lee Sin",
    "Leona",
    "Lissandra",
    "Lucian",
    "Lulu",
    "Lux",
    "Lillia",
    "Malphite",
    "Malzahar",
    "Maokai",
    "Master Yi",
    "Milio",
    "Miss Fortune",
    "Mordekaiser",
    "Morgana",
    "Naafiri",
    "Nami",
    "Nasus",
    "Nautilus",
    "Nidalee",
    "Nocturne",
    "Nunu",
    "Nilah",
    "Neeko",
    "Olaf",
    "Orianna",
    "Ornn",
    "Pantheon",
    "Poppy",
    "Pyke",
    "Quinn",
    "Qiyana",
    "Rammus",
    "Rek'Sai",
    "Renekton",
    "Rengar",
    "Riven",
    "Rumble",
    "Ryze",
    "Renata",
    "Rell",
    "Rakan",
    "Sejuani",
    "Shaco",
    "Shen",
    "Shyvana",
    "Singed",
    "Sion",
    "Sivir",
    "Skarner",
    "Sona",
    "Soraka",
    "Swain",
    "Syndra",
    "Senna",
    "Sett",
    "Samira",
    "Seraphine",
    "Smolder",
    "Sylas",
    "Talon",
    "Taric",
    "Teemo",
    "Thresh",
    "Tristana",
    "Trundle",
    "Tryndamere",
    "Twisted Fate",
    "Twitch",
    "Tahm kench",
    "Taliyah",
    "Udyr",
    "Urgot",
    "Varus",
    "Vayne",
    "Veigar",
    "Vel'Koz",
    "Vi",
    "Viktor",
    "Vladimir",
    "Volibear",
    "Vex",
    "Viego",
    "Warwick",
    "Wukong",
    "Xerath",
    "Xin Zhao",
    "Xayah",
    "Yasuo",
    "Yorick",
    "Yuumi",
    "Yone",
    "Zac",
    "Zed",
    "Ziggs",
    "Zilean",
    "Zyra",
    "Zeri",
    "Zoe",
]
with tab1:
    st.subheader("| Intro")
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image("imgs/lol_intro.png")
        st.caption("The Most Overpowered League of Legends Champions on Release")

    with col2:
        intro_text = """
        Welcome to ChampionEdge, League enthusiasts! Imagine stumbling upon a secret mushroom patch in Summoner’s Rift - that’s us, offering a clever way to pick champions. With our concoction of advanced machine learning, we’re here to predict victories and suggest champions tailored to your playstyle, giving you the edge before the battle even begins. 
        Strap in as we embark on a quest to outsmart the opposition, armed with data-driven insights and strategic recommendations. Whether you're climbing solo queue or teaming up for flex, ChampionEdge is your guide to making informed choices that turn the tide of battle in your favor. 
        Ready for a smarter way to play, combining strategy with a hint of Teemo’s cunning? ChampionEdge is here to lead the charge. Let’s dive into the Rift, champions - victory awaits with every smart pick!
        """
        st.markdown(f'<p class="custom-text">{intro_text}</p>', unsafe_allow_html=True)
        audio_file = open("audio/song.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")

    st.subheader("| Developer")
    st.markdown(
        '<p class="custom-text">Thanks to our amazing Pangolin team </p>',
        unsafe_allow_html=True,
    )

    st.subheader("| Github")
    st.markdown(
        '<p class="custom-text">This site is based on <a href="https://github.com/TomJohnH/streamlit-dungeon" style="color: #9c9d9f;">GitHub</a>. Edit your levels with <a href="https://dungeon-editor.streamlit.app/" style="color: #9c9d9f;">The Dungeon editor</a>.</p>',
        unsafe_allow_html=True,
    )


with tab2:
    st.subheader("| Winning Predictor")
    # Champion selection dropdown
    champion1 = st.selectbox("Choose your champion 1:", champion_list)
    champion2 = st.selectbox("Choose your champion 2:", champion_list)
    champion3 = st.selectbox("Choose your champion 3:", champion_list)
    champion4 = st.selectbox("Choose your champion 4:", champion_list)
    champion5 = st.selectbox("Choose your champion 5:", champion_list)
    champion_op_1 = st.selectbox("Choose your opponent's champion 1:", champion_list)
    champion_op_2 = st.selectbox("Choose your opponent's champion 2:", champion_list)
    champion_op_3 = st.selectbox("Choose your opponent's champion 3:", champion_list)
    champion_op_4 = st.selectbox("Choose your opponent's champion 4:", champion_list)
    champion_op_5 = st.selectbox("Choose your opponent's champion 5:", champion_list)

    # Predict button
    if st.button("Predict Winning Rate"):
        # Placeholder for the winning rate
        winning_rate = "60%"

        # Display the predicted winning rate within a chatbox style
        col1, col2 = st.columns([1, 5], gap="small")

        with col1:
            st.image("imgs/teemo.png", width=50)  # Adjust width as needed

        with col2:
            st.markdown(
                f"""
                <div style="background-color: #f0f2f6; padding: 10px; border-radius: 10px; color: #333333;">
                Your winning rate with is {winning_rate}
                </div>
                """,
                unsafe_allow_html=True,
            )


with tab3:
    st.subheader("| Champion Recommendation")
    # Champion selection dropdown
    team_champ2 = st.selectbox("Choose your team champion 1:", champion_list)
    team_champ3 = st.selectbox("Choose your team champion 2:", champion_list)
    team_champ4 = st.selectbox("Choose your team champion 3:", champion_list)
    team_champ5 = st.selectbox("Choose your team champion 4:", champion_list)
    oppo_champ1 = st.selectbox("Choose opponent's champion 1:", champion_list)
    oppo_champ2 = st.selectbox("Choose opponent's champion 2:", champion_list)
    oppo_champ3 = st.selectbox("Choose opponent's champion 3:", champion_list)
    oppo_champ4 = st.selectbox("Choose opponent's champion 4:", champion_list)
    oppo_champ5 = st.selectbox("Choose opponent's champion 5:", champion_list)

    # Predict button
    if st.button("Find your best champion"):
        # Placeholder for the winning rate
        winning_rate = "60%"

        # Display the predicted winning rate within a chatbox style
        col1, col2 = st.columns([1, 5], gap="small")

        with col1:
            st.image("imgs/teemo.png", width=50)  # Adjust width as needed

        with col2:
            st.markdown(
                f"""
                <div style="background-color: #f0f2f6; padding: 10px; border-radius: 10px; color: #333333;">
                Pick Teemo of course!
                </div>
                """,
                unsafe_allow_html=True,
            )
