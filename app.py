import streamlit as st
import time
from datetime import datetime
import random

# Configurações da página
st.set_page_config(page_title="Para a Minha Chubiruba", page_icon="❤️")

# Estilização para deixar com cara de app
# Substitua o bloco st.markdown(""" <style> ... </style> """, unsafe_allow_html=True) por este:

st.markdown("""
    <style>
    /* Força o fundo da página */
    .stApp {
        background-color: #fff5f5 !important;
    }
    
    /* Força a cor de todos os textos, títulos e marcações para preto */
    h1, h2, h3, p, span, div, .stMarkdown {
        color: #000000 !important;
    }

    /* Estilização do botão para ele não sumir */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b4b !important;
        color: white !important;
        border: none;
        font-weight: bold;
    }
    
    /* Força a cor do texto dentro da área de mensagem final */
    textarea {
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("❤️ Nossa História em Código")
st.write("Demorei pra fazer isso aqui mais do que tu imagina, então espero que gosteee!")

# --- SEÇÃO 1: O Contador ---
st.header("Há quanto tempo você me faz feliz?")
data_inicio = datetime(2025, 8, 31)
hoje = datetime.now()
diferenca = hoje - data_inicio # Corrigido aqui!

st.info(f"Já se passaram {diferenca.days} dias desde que minha vida ficou mais colorida ao seu lado!")

# --- SEÇÃO 2: Botão de Surpresa ---
st.subheader("Clique para um motivo de eu te amar:")
motivos = [
    "O seu sorriso ilumina qualquer dia ruim.",
    "A forma como você leva a vida e as dificuldades.",
    "O seu jeito de ver o mundo.",
    "A nossa sintonia, mesmo em silêncio.",
    "O seu sorriso bobo toda vez que eu faço uma palhaçada."
]

if st.button("Gerar motivo ❤️"):
    with st.spinner('Pensando em um motivo...'):
        time.sleep(1)
        st.success(random.choice(motivos))
        st.balloons()

# --- SEÇÃO 3: Galeria ---
st.divider()
st.subheader("Nossos Momentos")

col1, col2 = st.columns(2)
with col1:
    st.image("olhos.png", caption="Amo seus olhos", use_container_width=True)
with col2:
    st.image("amor_meu.png", caption="Nossa última festa", use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    st.image("rlk.png", caption="Nossa rlk smp esqueceee", use_container_width=True)
with col4:
    st.image("eu_amo.png", caption="Eu te amo meu amor", use_container_width=True)

col5, col6 = st.columns(2)
with col5:
    st.image("beijo.png", caption="Beijo no coração", use_container_width=True)
with col6:
    st.image("linda.png", caption="SUA APETITOSA", use_container_width=True)

# --- SEÇÃO 4: Mensagem Final ---
st.divider()
st.subheader("Uma carta para você")
st.markdown(f"""
> **Para a garota que faz meu mundo florescer:**
> 
> Se eu tivesse que te explicar, eu começaria pelas flores. Porque você é tipo jardim depois da chuva — delicada, viva, cheia de cor, mas com raízes fortes que ninguém vê. 
>
> Se a vida fosse um episódio de **Grey's Anatomy**, eu toparia todos os dramas só pra no final ter você ao meu lado como a 'minha pessoa'. Você tem esse coração gigante, ama doce, ri fácil e protege o Miguel como se fosse metade sua.
>
> Talvez por isso você sonhe em ser policial. Você nasceu pra ser coragem, pra ser força. Você é flor e é armadura. E se um dia você vestir essa farda, eu estarei ali, orgulhoso, sabendo que o mundo ganhou uma heroína.
>
> Amar você é a melhor parte da minha história.
ps: eu te amo muito , vc é o melhor presente q eu posso ter minha chubiruba , espero q goste , foi mais dificil q imaginei
""")

feedback = st.text_area("Deixe uma mensagem para mim aqui se quiser:", "Te amo muito!")
if st.button("Enviar Mensagem"):

    st.write("Mensagem 'salva' no meu coração!")


