# app.py

import streamlit as st
import os
import sys

# Adjusting the script directory for relative imports
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from ui_components import UIComponentFactory
from services.academic_advising import AdvisorService
from services.ta_service import TAService
from api.chat_api import ChatCompletionAPI


class StreamlitAppController:
    def __init__(self, chat_api: ChatCompletionAPI):
        self.advisor_service = AdvisorService(chat_api)
        self.ta_service = TAService(chat_api)
        
        # Initialize separate conversation lists for each mode
        if 'advisor_conversation' not in st.session_state:
            st.session_state.advisor_conversation = []
        if 'ta_conversation' not in st.session_state:
            st.session_state.ta_conversation = []
        if 'selected_mode' not in st.session_state:
            st.session_state.selected_mode = None

    def run(self):
        UIComponentFactory.create_title("UVU GPT Advisor and Tutor System")
        UIComponentFactory.create_sidebar_header("Welcome")
        st.sidebar.write("Please select your mode and enter your query below.")

        mode = UIComponentFactory.styled_selectbox("Select your mode:", ["UVU Advisor", "UVU TA"], help_text="Choose whether you want advice or tutoring.")

        # Check if mode has changed and reset the relevant conversation if so
        if mode != st.session_state.selected_mode:
            st.session_state.selected_mode = mode
            if mode == "UVU Advisor":
                st.session_state.advisor_conversation = []
            else:  # mode == "UVU TA"
                st.session_state.ta_conversation = []

        user_input = UIComponentFactory.styled_text_input("Enter your query here:", "query", help_text="Type your question or request for the selected mode.")

        # Display the conversation history for the selected mode
        conversation_key = 'advisor_conversation' if mode == "UVU Advisor" else 'ta_conversation'
        for message in st.session_state[conversation_key]:
            st.container().markdown(f"> {message}")

        if UIComponentFactory.styled_button("Submit", help_text="Click to submit your query."):
            self.process_query(user_input, mode)

    def process_query(self, user_input, mode):
        if user_input:
            conversation_key = 'advisor_conversation' if mode == "UVU Advisor" else 'ta_conversation'
            st.session_state[conversation_key].append(f"You: {user_input}")

            if mode == "UVU Advisor":
                response = self.advisor_service.process_query(user_input)
            else:  # UVU TA mode
                response = self.ta_service.provide_hint(user_input)

            st.session_state[conversation_key].append(f"{mode}: {response}")
            st.session_state.query = ""  # Clear input box after processing the query
            st.experimental_rerun()


if __name__ == "__main__":
    
    chat_api = ChatCompletionAPI(base_url='https://4158-161-28-242-155.ngrok-free.app/v1')
    app = StreamlitAppController(chat_api)
    app.run()