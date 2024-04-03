import streamlit as st

class UIComponentFactory:
    @staticmethod
    def create_title(text, color="#006633"):
        st.markdown(f"""
            <style>
            .title {{
                color: {color};
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                margin-top: 1rem;
            }}
            </style>
            <div class="title">{text}</div>
            """, unsafe_allow_html=True)

    @staticmethod
    def create_sidebar_header(text, color="#006633"):
        st.sidebar.markdown(f"""
            <style>
            .sidebar-header {{
                color: {color};
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }}
            </style>
            <div class="sidebar-header">{text}</div>
            """, unsafe_allow_html=True)

    @staticmethod
    def styled_selectbox(label, options, index=0, help_text=None, color="#006633"):
        # Apply custom CSS to the selectbox via a container
        container = st.sidebar.container()
        container.markdown(f"""
            <style>
            .stSelectbox .css-2b097c-container {{
                border: 2px solid {color};
                border-radius: 20px;
            }}
            .stSelectbox .css-1uccc91-singleValue {{
                color: {color};
            }}
            </style>
            """, unsafe_allow_html=True)
        return container.selectbox(label, options, index=index, help=help_text)

    @staticmethod
    def styled_text_input(label, key, help_text=None, color="#006633"):
        # Custom styling for text input
        st.sidebar.markdown(f"""
            <style>
            .stTextInput>div>div>input {{
                color: {color};
                border: 2px solid {color};
                border-radius: 20px;
            }}
            </style>
            """, unsafe_allow_html=True)
        return st.sidebar.text_input(label, key=key, help=help_text)

    @staticmethod
    def styled_button(label, help_text=None, color="#006633"):
        st.sidebar.markdown(f"""
            <style>
            .stButton>button {{
                border: 2px solid {color};
                border-radius: 20px;
                color: white;
                background-color: {color};
                font-size: 16px;
                font-weight: bold;
                height: 3em;
                width: 100%;
                margin-top: 1em;
            }}
            </style>""", unsafe_allow_html=True)
        return st.sidebar.button(label, help=help_text)