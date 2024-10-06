import streamlit as st
import requests

st.set_page_config(page_title="Cidely", page_icon=":e_mail:", layout="wide")

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


# Header
with st.container():
    st.image("images/Cidely.png", caption="")
    st.title("Welcome to Cidely!")
    st.subheader("Cidely is the name of this website, which is where I show all my animation videos. "
                 "Don't ask me why its called 'Cidely'! ")

# what I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("About Me")
        st.write("##")
        st.write("""
        I did this because I want to show the world what I am capable of
        and I want to share my daily life. Unlike most animators that either 
        dropped out of school or don't like sports, I didn't drop out of school (cause I'm still in school) 
        and I like sports! SO what kind of sports do I like? Well I like playing football, running and also badminton!
        Even though alot of people might not like them I like them and that's what makes me me! I
        know that the animation you are seeing is a boy but I'm a girl! Let that sink in your head! 
        I hope you enjoy looking on this website.
        """)
    with right_column:
        st.empty()

# animations and drawings
with st.container():
    st.write("---")
    st.header("Introduction")
    st.write("##")
    video_column, text_column = st.columns((2, 1))
    with video_column:
        video_file = open("videos/for_web.mp4", "rb")
        video_bytes = video_file.read()

        st.video(video_bytes)
    with text_column:
        st.subheader("Introduction")
        st.write("""
        In this video you are going to learn how to: 
        - Use an animation editor
        - I am going to take you through the process (or boring process) of animating
        - In the next video is going to be about video editor.
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
        st.header("Socials!")
        st.write("Need prof that I'm real? I'm sure you don't but if you do click the link below.")

        url = "https://github.com/ori-kekere/"
        st.markdown("Need prof click here [social](%s)" % url)

with st.container():
    footer_html = """<div style='text-align: center;'>
      <p>Developed with ❤️ by Cidely</p>
    </div>"""
    st.markdown(footer_html, unsafe_allow_html=True)
