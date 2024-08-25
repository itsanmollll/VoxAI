import streamlit as st

# Set the title of the app
st.title("Simple Streamlit App")

# Add a text input box
user_input = st.text_input("Enter some text:")

# Display the text input back to the user
if user_input:
    st.write(f"You entered: {user_input}")

# Add a button and show a message when clicked
if st.button("Click Me"):
    st.write("Button clicked!")
