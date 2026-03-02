import streamlit as st
import os
import smtplib
from email.message import EmailMessage
import zipfile
import importlib

# Import your script dynamically since it starts with a number
mashup_script = importlib.import_module("102317201")

def send_email(receiver_email, zip_filename):
    # Setup your email credentials here
    sender_email = "rbiswas_be23@thapar.edu"
    sender_password = "abcd efgh ijkl mnop"  #i am not using my app pass here, security concerns, just go to google creat one and use yours here
    
    msg = EmailMessage()
    msg['Subject'] = 'Your Mashup is Ready!'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content('Please find attached your generated mashup.')

    with open(zip_filename, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='zip', filename=zip_filename)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

st.title("Audio Mashup Web App")

# Input fields
singer_name = st.text_input("Singer Name", value="Sharry Mann")
num_videos = st.number_input("# of videos", min_value=11, value=20)
audio_duration = st.number_input("Duration of each video (sec)", min_value=21, value=30)
email_id = st.text_input("Email Id", value="psrana@gmail.com")

if st.button("Submit"):
    if "@" not in email_id or "." not in email_id:
        st.error("Email id must be correct") #
    else:
        st.info("Generating mashup... This may take a few minutes.")
        
        try:
            output_mp3 = "mashup_result.mp3"
            zip_filename = "mashup_result.zip"
            
            # 1. Call the real functions from 102317201.py
            mashup_script.get_videos(singer_name, int(num_videos))
            mashup_script.process_and_merge(int(audio_duration), output_mp3)
            
            # 2. Zip the file so the user gets the result file in zip format
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                zipf.write(output_mp3)
                
            # 3. Send the email
            send_email(email_id, zip_filename)
            st.success(f"Success! Result file in zip format has been sent through email to {email_id}") #
            
        except Exception as e:
            st.error(f"An error occurred: {e}")