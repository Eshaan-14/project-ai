import streamlit as st
import google.generativeai as genai

st.title("Eshaan's Second Streamlit App")
st.write("Here's Eshaan's sss second attempt at using data to create a table:")

apikey="AIzaSyAj7N2akcgXUzGliR8h-2l21OQ3zAbaxbI"

# setting the api key
genai.configure(api_key=apikey)

# setting the text model
model = genai.GenerativeModel('gemini-1.5-flash')


tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat - Gen AI")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    role = st.selectbox("Select a Role", ["Professor", "Cricketer","politician","plumber","mechanic", "Student"])
    prompt = st.chat_input("Say something")

    if prompt:
        prompt_str = f"you are a {role}. please respond to: {prompt}"
        st.write(prompt_str)
        # generating response
        response = model.generate_content(prompt_str)

        # printing the response
        st.write("Response from Gemini AI:")
        st.write(response.text)

    ########### OUTPUT ###########
    # he query of life purpose has perplexed people 
    # across centuries ... 
    ########### OUTPUT ###########

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    