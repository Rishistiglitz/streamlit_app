import streamlit as st
from streamlit_option_menu import option_menu

st.title("👨‍💻 Vinsup Infotech 👨‍💻")

# Sidebar menu
with st.sidebar:
    data = option_menu(
        menu_title="Vinsup Menu",
        options=["Home", "About", "Contact"],
        icons=["house", "people", "phone"]
    )

# Home section
if data == "Home":
    st.header("Registration Form")
    
    col1, col2 = st.columns(2)
    with col1:
        Name = st.text_input("Enter Your Name")
        Email = st.text_input("Enter Your Email")
    with col2:
        Num = st.text_input("Enter Your Number")
        Pass = st.text_input("Enter Your Password", type="password")

    if st.button("Submit"):
        st.write("Name:", Name)
        st.write("Email:", Email)
        st.write("Number:", Num)
        st.write("Password:", Pass)
        st.success("Data inserted successfully")

    st.metric(label="Python", value=20, delta="-20%")
    st.number_input("Enter an Integer", max_value=0)
    st.radio("Select your option", ["Option 1", "Option 2", "Option 3"])

# About section
elif data == "About":
    st.header("About Page")
    st.write("Welcome to the About page of Vinsup Infotech.")

# Contact section
elif data == "Contact":
    st.header("Contact Page")
    st.write("Feel free to reach out to us!")
