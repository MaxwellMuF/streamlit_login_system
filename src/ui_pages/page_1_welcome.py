import streamlit    as st

## Page: streamlit elements

st.title(body="Welcome to a Streamlit App!",
         help="This is a helper for streamlit elements. You can write some hints or usage.")

with st.container(border=True):
    st.header(body=f"Some Header: Hello *{st.session_state.username}*")
    st.write("Some more text: This is an example page.")
