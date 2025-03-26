import streamlit as st
import time

def display_fake_login_page():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
        
        .login-container {
            max-width: 450px;
            margin: 40px auto;
            font-family: 'Inter', sans-serif;
        }
        .login-card {
            background: linear-gradient(145deg, #1a3a8f, #0d2b66);
            border-radius: 12px;
            padding: 35px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            color: white;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .login-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.08) 10%, transparent 50%);
            transform: rotate(25deg);
            animation: glowing 8s linear infinite;
        }
        @keyframes glowing {
            0% { transform: rotate(25deg) translate(0, 0); opacity: 0.5; }
            50% { transform: rotate(25deg) translate(40px, 40px); opacity: 0.8; }
            100% { transform: rotate(25deg) translate(0, 0); opacity: 0.5; }
        }
        .login-header {
            text-align: center;
            margin-bottom: 25px;
            position: relative;
            z-index: 1;
        }
        .login-title {
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 8px;
            letter-spacing: 0.5px;
        }
        .login-subtitle {
            font-size: 15px;
            opacity: 0.9;
            margin-bottom: 30px;
        }
    </style>
    
    <div class="login-container">
        <div class="login-card">
            <div class="login-header">
                <div style="font-size: 32px; margin-bottom: 10px;">🔐</div>
                <div class="login-title">Secure Account Login</div>
                <div class="login-subtitle">Enter your credentials to continue</div>
            </div>
    """, unsafe_allow_html=True)

def display_otp_page():
    st.markdown("""
    <style>
        .otp-card {
            background: linear-gradient(145deg, #1a3a8f, #0d2b66);
            border-radius: 12px;
            padding: 35px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            color: white;
            text-align: center;
            margin: 40px auto;
            max-width: 450px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .otp-code {
            font-size: 28px;
            letter-spacing: 5px;
            margin: 25px 0;
            font-weight: bold;
            background: rgba(0,0,0,0.3);
            padding: 15px;
            border-radius: 8px;
            display: inline-block;
        }
    </style>
    
    <div class="otp-card">
        <h3 style="margin-bottom: 15px;">🔒 Two-Factor Authentication</h3>
        <p style="margin-bottom: 10px;">We sent a verification code to your device</p>
        <div class="otp-code">3 5 9 7 4</div>
        <p style="font-size: 13px; opacity: 0.8;">This code expires in 2 minutes</p>
    </div>
    """, unsafe_allow_html=True)

def display_attack_details():
    with st.expander("🔍 What Just Happened?", expanded=True):
        st.markdown("""
        - You entered credentials on a fake login page
        - The attacker relayed them to the real service
        - You provided the legitimate OTP to the attacker
        - They now have full access to your account
        """)
    
    with st.expander("⚙️ Technical Details"):
        st.markdown("""
        - **Proxy Server**: Attacker intercepted all communications
        - **Session Hijacking**: Stole your authentication tokens
        - **OTP Window**: Exploited the 2-minute valid period
        """)

def otp_phishing_simulation():
    st.title("🔓 OTP Phishing Simulation")
    
    # Initialize session state
    if 'otp_stage' not in st.session_state:
        st.session_state.otp_stage = 1
        st.session_state.credentials = {}
    
    # Stage 1: Fake Login Page
    if st.session_state.otp_stage == 1:
        display_fake_login_page()
        
        username = st.text_input("Username", key="otp_username")
        password = st.text_input("Password", type="password", key="otp_password")
        
        st.markdown("</div>", unsafe_allow_html=True)  # Close login-container
        
        if st.button("Continue", key="otp_login_btn", use_container_width=True):
            if username and password:
                st.session_state.credentials = {'username': username, 'password': password}
                st.session_state.otp_stage = 2
                st.success("✓ Login successful. Redirecting to 2FA...")
                time.sleep(1.5)
                st.rerun()
            else:
                st.error("Please enter both username and password")

    # Stage 2: OTP Prompt
    elif st.session_state.otp_stage == 2:
        display_otp_page()
        
        otp = st.text_input("Enter verification code", key="otp_input", max_chars=6)
        
        if st.button("Verify", key="otp_verify_btn", use_container_width=True):
            if otp == "35974":  # Check against the hardcoded OTP
                st.session_state.otp_stage = 3
                st.success("Verification complete")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid code. Please try again.")

    # Stage 3: Attack Reveal
    elif st.session_state.otp_stage == 3:
        st.error("""
        ## 🚨 Account Compromised
        The attacker now has full access to your account!
        """)
        
        st.image("https://cdn-icons-png.flaticon.com/512/753/753345.png", width=120)
        
        st.markdown("""
        <div style="
            background: #fff3f3;
            border-left: 4px solid #ff4b4b;
            padding: 16px;
            border-radius: 4px;
            margin: 20px 0;
        ">
        <h4 style="color: #d32f2f; margin-top: 0;">What the attacker can do:</h4>
        <ul style="color: black;">
            <li>Access sensitive information</li>
            <li>Make unauthorized transactions</li>
            <li>Change account settings</li>
            <li>Lock you out of your account</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        display_attack_details()
        
        with st.expander("🛡️ How To Protect Yourself"):
            st.markdown("""
            - **Verify URLs**: Always check website addresses
            - **Use Authenticator Apps**: Prefer over SMS OTPs
            - **Security Keys**: Consider physical security keys
            - **Report Suspicious Emails**: Contact IT immediately
            """)
        
        if st.button("🔄 Restart Simulation", key="otp_restart_btn", type="primary"):
            st.session_state.otp_stage = 1
            st.session_state.credentials = {}
            st.rerun()

if __name__ == "__main__":
    otp_phishing_simulation()
