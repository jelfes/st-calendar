import streamlit as st
from yagmail import SMTP

send = st.button('Send!')
if send:
    conn = SMTP("taubenschlag.ensemble@gmail.com", oauth2_file="gmail-api-credentials/credentials.json")
    conn.send(subject="Yellow!")
    st.write('Done!')
