import streamlit as st
import yagmail

st.title('Book a place with Jan')

st.write('Willkommen! Du bist hier gelandet weil du dich gerne mit Jan treffen möchtest? Dann bist du hier genau richtig! Im folgenden kannst du deine Verfügbarkeiten angeben, Jan wird dann schnellst möglich mit einem Zeitangebot auf dich zukommen.')
st.write("Bitte beachte, Jan's Zeit ist knapp. Solltest du ein offizielles Zeitangebot erhalten, bitten wir dich es zeitnah anzunehmen oder abzulehnen.")

st.subheader("Los geht's:")
name = st.text_input('Name:', '')
reason = st.text_input('Grund für die Anfrage:', '')

st.write('Bitte gebe im Folgenden deine Verfügbarkeiten an.')

days = st.multiselect(
     'An welchen Tagen bist du verfügbar?',
     ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
)

time = st.multiselect(
     'Zu welcher Tageszeit?',
     ['Morgens', 'Mittags', 'Abends']
)

st.write('Hast du noch eine Nachricht oder Anmerkungen für Jan?')

msg = st.text_input('')


send = st.button('Send!')



if send:

    subject = 'Appointment ' + name
    message = ['Vefügbarkeiten:', days, time, reason, msg]


    conn = yagmail.SMTP(st.secrets['username'], st.secrets['password'])
    conn.send(to = 'taubenschlag.ensemble@gmail.com', subject=subject, contents=message)
    st.write('Done!')
