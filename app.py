import streamlit as st
import time
from scenarios.phishing import run_phishing
from scenarios.mitm import mitm_simulation
from scenarios.otp_phishing import otp_phishing_simulation

def initialize_session_state():
    if 'intro_complete' not in st.session_state:
        st.session_state.intro_complete = False
    if 'selected_scenario' not in st.session_state:
        st.session_state.selected_scenario = "Phishing Attack"

def show_intro():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Orbitron:wght@700&display=swap');
            
            .stApp { 
                background: linear-gradient(135deg, #000428, #004e92);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }
            .intro-container {
                text-align: center;
                color: white;
                animation: fadeOut 6s ease-in-out forwards;
                padding: 3rem;
                border-radius: 15px;
                background: rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.15);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                max-width: 800px;
                margin: auto;
            }
            @keyframes fadeOut {
                0% { opacity: 0; transform: translateY(20px); }
                20% { opacity: 1; transform: translateY(0); }
                80% { opacity: 1; transform: scale(1); }
                90% { opacity: 0.8; transform: scale(0.98); }
                100% { opacity: 0; transform: scale(0.95); }
            }
            .title {
                font-family: 'Orbitron', sans-serif;
                font-size: 3.5rem;
                margin-bottom: 1.5rem;
                background: linear-gradient(90deg, #00d2ff, #3a7bd5);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 0 15px rgba(0, 210, 255, 0.4);
                letter-spacing: 3px;
                line-height: 1.2;
            }
            .subtitle {
                font-family: 'Montserrat', sans-serif;
                font-size: 1.4rem;
                margin-bottom: 3rem;
                opacity: 0.9;
                line-height: 1.6;
            }
            .author {
                font-family: 'Montserrat', sans-serif;
                font-size: 1.2rem;
                margin-top: 3rem;
                color: rgba(255,255,255,0.7);
                border-top: 1px solid rgba(255, 255, 255, 0.2);
                padding-top: 1.5rem;
                display: inline-block;
            }
            .cyber-line {
                height: 3px;
                background: linear-gradient(90deg, transparent, rgba(0, 210, 255, 0.7), transparent);
                margin: 2rem auto;
                width: 50%;
            }
        </style>
        <div class="intro-container">
            <div class="title">SOCIAL ENGINEERING<br>SIMULATOR</div>
            <div class="cyber-line"></div>
            <div class="subtitle">Experience realistic cyber attack scenarios<br>to strengthen your security awareness</div>
            <div class="author">Developed by Malek Kabaja • Security Specialist</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Automatically transition after 6 seconds
    time.sleep(6)
    st.session_state.intro_complete = True
    st.rerun()

def main_app():
    st.sidebar.title("🔍 Social Engineering Simulator")
    scenario = st.sidebar.radio(
        "Choose a scenario:",
        ("Phishing Attack", "Man-in-the-Middle Attack", "OTP Phishing Attack"),
        key="scenario_radio_key"
    )
    
    if scenario == "Phishing Attack":
        run_phishing()
    elif scenario == "Man-in-the-Middle Attack":
        mitm_simulation()
    elif scenario == "OTP Phishing Attack":
        otp_phishing_simulation()

def main():
    initialize_session_state()
    if not st.session_state.intro_complete:
        show_intro()
    else:
        main_app()

if __name__ == "__main__":
    st.set_page_config(
        page_title="Social Engineering Simulator",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    main()