import requests
import streamlit as st
from streamlit_lottie import st_lottie


def loadAnimationLottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = loadAnimationLottie("https://assets2.lottiefiles.com/packages/lf20_tfb3estd.json")

st.set_page_config(page_title="Python Learning", page_icon=":tada:", layout="wide")

button = """<button class="btn">Ver alguns conteúdos</button>"""

def loadCss(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

loadCss("style.css")

with st.container():
    header, box = st.columns(2)
    with header:
        st.header("Seja bem vindo ao Python Learning")
        st.subheader("Aqui voce encontra conteúdos sobre python")
        st.markdown(button, unsafe_allow_html=True)
    with box:
        st_lottie(lottie_coding, height=600)
      