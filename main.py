import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Cido", page_icon=":e_mail:", layout="wide")

def load_lottieul(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles/styles.css")

# load assets
lottie_coding = load_lottieul("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# Header
with st.container():
    st.title("Welcome to Cido!")
    st.subheader("Cido is the name of this website, which is where I show all my animation videos.")

# what I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Why I do this")
        st.write("##")
        st.write("""
        I did this because I want to show the world what I am capable of
        and I want to share my daily life. Unlike most animators that either 
        dropped out of school or don't like sports, I didn't drop out of school (cause I'm still in school) 
        and I like sports! SO what kind of sports do I like? Well I like playing football, running and also badminton!
        Even though alot of people might not like them I like them and that's what makes me me! I
        know that the animation you are seeing is a boy but I'm a girl! Let that sink in your head!
        """)
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# animations and drawings
with st.container():
    st.write("---")
    st.header("Wick Editor")
    st.write("##")
    video_column, text_column = st.columns((2, 1))
    with video_column:
        video_file = open("videos/avvop.mp4", "rb")
        video_bytes = video_file.read()

        st.video(video_bytes)
    with text_column:
        st.subheader("Wick Editor")
        st.write("""
        In this video you are going to learn how to: 
        - Use an animation editor
        - I am going to take you through the process (or boring process) of animating
        - In the next video is going to be about video editor.
        """)

with st.container():
    st.write("---")
    st.header("Clideo Editor")
    st.write("##")
    video_column, text_column = st.columns((2, 1))
    with video_column:
        video_file = open("videos/viedi.mp4", "rb")
        video_bytes = video_file.read()

        st.video(video_bytes)
    with text_column:
        st.subheader("Clideo Editor")
        st.write("""
        In this video you are going to learn how to: 
        - Use an video editor
        - I am going to take you through the process of video editing
        Hope you enjoyed!
        """)

# contact form
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/0e9c124384853139fdf1e91c4b6898de" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button>
     </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()