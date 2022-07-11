import streamlit as st
import yagmail

send = st.button('Send!')

if send:
    conn = yagmail.SMTP(st.secrets['username'], st.secrets['password'])
    conn.send(to = 'taubenschlag.ensemble@gmail.com', subject="Yellow!")
    st.write('Done!')
