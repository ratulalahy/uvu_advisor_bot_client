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

    def display_messages(self, messages, mode):
        """Displays messages in chat bubble format."""
        for message in messages:
            # Check if the message is from the user or the system/TA/Advisor
            if message.startswith("You:"):
                st.markdown(f"<div style='text-align: right; color: white; background-color: #006633; border-radius: 10px; padding: 10px; margin: 10px 0;'>{message[4:]}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align: left; color: white; background-color: #333333; border-radius: 10px; padding: 10px; margin: 10px 0;'>{mode}: {message}</div>", unsafe_allow_html=True)

    def run(self):
        UIComponentFactory.create_title("UVU GPT Advisor and Tutor System")
        UIComponentFactory.create_sidebar_header("Welcome")
        st.sidebar.write("Please select your mode and enter your query below.")

        mode = UIComponentFactory.styled_selectbox("Select your mode:", ["UVU Advisor", "UVU TA"], help_text="Choose whether you want advice or tutoring.")

        # Encapsulate the input and button within a form
        with st.sidebar.form(key="query_form"):
            user_input = UIComponentFactory.styled_text_input("Enter your query here:", key="user_query", help_text="Type your question or request for the selected mode.")
            submit_button = UIComponentFactory.styled_button("Submit", help_text="Click to submit your query.")

            # When the form is submitted, the input is processed without needing to reset it manually
            if submit_button:
                self.process_query(user_input, mode)

        # Display the conversation history for the selected mode outside the form
        conversation_key = 'advisor_conversation' if mode == "UVU Advisor" else 'ta_conversation'
        self.display_messages(st.session_state[conversation_key], mode)

    # def run(self):
    #     UIComponentFactory.create_title("UVU GPT Advisor and Tutor System")
    #     UIComponentFactory.create_sidebar_header("Welcome")
    #     st.sidebar.write("Please select your mode and enter your query below.")

    #     mode = UIComponentFactory.styled_selectbox("Select your mode:", ["UVU Advisor", "UVU TA"], help_text="Choose whether you want advice or tutoring.")

    #     user_input = UIComponentFactory.styled_text_input("Enter your query here:", key="user_query", help_text="Type your question or request for the selected mode.") 

    #     if UIComponentFactory.styled_button("Submit", help_text="Click to submit your query."):
    #         if user_input:  # Check if there is any input to process
    #             self.process_query(user_input, mode)
    #             st.session_state.user_query = ""  # Reset input box after processing the query

    #     # Display the conversation history for the selected mode
    #     conversation_key = 'advisor_conversation' if mode == "UVU Advisor" else 'ta_conversation'
    #     self.display_messages(st.session_state[conversation_key], mode)

    def process_query(self, user_input, mode):
        conversation_key = 'advisor_conversation' if mode == "UVU Advisor" else 'ta_conversation'
        st.session_state[conversation_key].append(f"You: {user_input}")

        # Decide which service to use based on the mode
        if mode == "UVU Advisor":
            response = self.advisor_service.general_query(user_input)
        else:  # UVU TA mode
            response = self.ta_service.general_query(user_input)

        # Append the response to the conversation history
        st.session_state[conversation_key].append(response)
        # No need to rerun after adjustments to display_messages

if __name__ == "__main__":
    
    chat_api = ChatCompletionAPI(base_url='https://0e80-161-28-242-150.ngrok-free.app/v1')
    app = StreamlitAppController(chat_api)
    app.run()