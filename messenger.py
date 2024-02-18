import streamlit as st
import time
import pyautogui

def main():
    st.title("Auto Message Sender")

    your_message = st.text_input('Enter your text message here:')
    counts = st.number_input('How many times do you want to send the message?', min_value=1, step=1, value=1)

    if st.button('Start Sending'):
        st.write("This program will run in 10 seconds...")
        time.sleep(10)
        message_count = counts
        while message_count > 0:
            pyautogui.typewrite(your_message)
            pyautogui.press("enter")
            message_count -= 1
            st.write(f"Message sent successfully!, {message_count} messages left.")

if __name__ == "__main__":
    main()
