from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webage", page_icon="tada", layout="wide")

def load_lottieurl(url):
	r=requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()

def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

#insert animation
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_o6spyjnc.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

st.subheader("Hi, we are from Fantastic Four :wave:")
st.title("GoPay Zakat")
st.write("We are here to help for Zakat Calculation")

st.write("[Learn More link >]")

with st.container():
	st.write("-----")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("About Us")
		st.write("##")
		st.write(
			"""
			zakat is bla bla bla bla (introduction apps)
			"""
			)
	with right_column:
		st_lottie(lottie_coding, height=300, key="coding")

#insert colum gambar kat bawah

with st.container():
	st.write("---")
	st.header("My Projects")
	st.write("##")
	image_column, text_column = st.columns((1, 2))

	with image_column:
		st.image(img_contact_form)
		st.image(img_lottie_animation)
		#insert image
	with text_column:
		st.subheader("Integrate Lottie Animation Inside Your Streamlit App")
		st.write(
		"""
		Learn how to use Lottie Files in Streamlit!
		Animation make our web app more engaging and fun, and Lottie Files are the easiest way to do
		In this tutorial, I'll show you exactly how to do it
		"""
	)
	st.markdown("[Watch Video...](Link)")
with st.container():
	image_column, text_column=st.columns((1,2))
	with image_column:
		st.image(img_contact_form)
	with text_column:
		st.subheader("How to add a contact form to your streamlit app")
		st.write(
			"""
			Want to bla bla bla bla?
			in this video, im going
			"""
		)
		st.markdown("[Watch Video...](link)")

with st.container():
	st.write("---")
	st.header("Get in touch with me!")
	st.write("##")

	#contactform
	contact_form= """
<form action="https://formsubmit.co/gopayzakat@gmail.com" method="POST">
	 <input type="hidden" name="_captcha" value="false">
	 <input type="text" name="name" placeholder="Your name" required>
	 <input type="email" name="email" placeholder="Your email" required>
	 <textarea name="message" placeholder ="Your message here" required></textarea>
	 <button type="submit">Send</button>
</form>
"""

left_column, right_column=st.columns(2)
with left_column:
	st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
	st.empty()

