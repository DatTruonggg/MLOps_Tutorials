import streamlit as st

#streamlit run main.py
st.title("Streamlit Demo Dat Truong")

st.header("First Heading")

st.subheader("2nd Heading")

st.text("This is an example text")

st.success("Success")
st.warning("Warning")
st.info("info")
st.error("Error")


if st.checkbox("Select/Unselect"):
    st.text("User ticked")
else:
    st.text("Not ticked")

state = st.radio("What is ur fav color??", ("red", "green", "yellow"))

if state == "green":
    st.success("That's my fav color as well")

occupation = st.selectbox("What do you do?", ("student", "vlogger", "engineer"))

st.text(f"selected option is {occupation}")

if st.button("Example button"):
    st.error("U clicked")
else: 
    st.error("Nice")

st.sidebar.header("Heading of side bar")
st.sidebar.text("Create by Dat")