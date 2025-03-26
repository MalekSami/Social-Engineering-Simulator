import streamlit as st
import time

def mitm_simulation():

    # Initialize session state
    if 'mitm_step' not in st.session_state:
        st.session_state.mitm_step = 1
        st.session_state.credentials = {}

    # Custom CSS for beautiful styling
    st.markdown("""
    <style>
        .bank-login {
            max-width: 500px;
            margin: 0 auto;
            padding: 2rem;
            border-radius: 15px;
            background: linear-gradient(145deg, #f6f9fc, #eef2f5);
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .bank-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .bank-logo {
            font-size: 2.5rem;
            color: #2563eb;
            margin-bottom: 0.5rem;
        }
        .bank-title {
            font-size: 1.5rem;
            color: #1e3a8a;
            font-weight: 600;
        }
        .bank-subtitle {
            color: #64748b;
            margin-bottom: 1.5rem;
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        .form-label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            color: #334155;
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
            padding: 12px 16px;
            border: 1px solid #cbd5e1;
        }
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            padding: 12px;
            background: linear-gradient(90deg, #2563eb, #1d4ed8);
            color: white;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        }
        .account-info {
            background: black;
            padding: 1.5rem;
            border-radius: 10px;
            margin-top: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
    </style>
    """, unsafe_allow_html=True)

    # Step 1: Beautiful Bank Login Page
    if st.session_state.mitm_step == 1:
        with st.container():
            st.markdown("""
            <div class="bank-login">
                <div class="bank-header">
                    <div class="bank-logo">🔒</div>
                    <div class="bank-title">Global Trust Bank</div>
                    <div class="bank-subtitle">Secure Online Banking Portal</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Form inputs
            username = st.text_input("Username", key="mitm_username")
            phone_number = st.text_input("Phone Number", key="mitm_phone")
            email = st.text_input("Email Address", key="mitm_email")
            password = st.text_input("Password", type="password", key="mitm_password")
            
            if st.button("Sign In", key="mitm_login_button"):
                if username and phone_number and email and password:
                    st.session_state.credentials = {
                        'username': username,
                        'phone': phone_number,
                        'email': email,
                        'password': password
                    }
                    st.session_state.mitm_step = 2
                    st.rerun()
                else:
                    st.error("Please fill in all fields to continue")
            
            if username and phone_number and email:
                st.markdown(f"""
                <div class="account-info">
                    <h4>Account Preview</h4>
                    <p><strong>Account Holder:</strong> {username}</p>
                    <p><strong>Account Type:</strong> Premium Checking</p>
                    <p><strong>Phone Number:</strong> {phone_number}</p>
                    <p><strong>Email:</strong> {email}</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

    # Step 2: Credential Interception
    elif st.session_state.mitm_step == 2:
        st.markdown("**You have successfully logged in.**")
        time.sleep(1)
        st.markdown("### **Step 2: Your login credentials are being intercepted...**")

        intercepted_data = f"""
        HTTP POST Request: /login
        - Username: {st.session_state.credentials['username']}
        - Phone Number: {st.session_state.credentials['phone']}
        - Email: {st.session_state.credentials['email']}
        - Password: {st.session_state.credentials['password']}
        - Session Cookie: None
        """
        st.code(intercepted_data, language='http')

        st.markdown("""  
        The attacker now has access to your login details. They can:  
        - Log into your account  
        - Change your password  
        - View your sensitive data  
        """)

        if st.button("Continue", key="mitm_step2_continue"):
            st.session_state.mitm_step = 3
            st.rerun()

    # Step 3: Session Hijacking
    elif st.session_state.mitm_step == 3:
        st.markdown("### **Step 3: The Attacker Hijacks Your Session**")
        st.write(f"**Attacker logs in as: {st.session_state.credentials['username']}**")
        time.sleep(2)

        if st.button("Continue", key="mitm_step3_continue"):
            st.session_state.mitm_step = 4
            st.rerun()

    # Step 4: Account Takeover
    elif st.session_state.mitm_step == 4:
        st.markdown("### **Step 4: The Attacker Controls Your Account**")
        st.markdown("""  
        Now the attacker can:  
        - Change your password  
        - View sensitive account data  
        - Perform unauthorized actions  
        """)
        time.sleep(2)

        if st.button("Continue", key="mitm_step4_continue"):
            st.session_state.mitm_step = 5
            st.rerun()

    # Step 5: Data Exposure
    elif st.session_state.mitm_step == 5:
        st.markdown("### **Step 5: Sensitive Data Exposed**")
        st.write("**Your password has been changed.** You're locked out.")
        
        st.markdown(f"""
            <div style="border: 1px solid #ccc; padding: 15px; background-color: #f9f9f9; border-radius: 5px; color: black;">
                <h4 style="font-size: 18px; color: black; font-family: 'Arial', sans-serif;">Account Overview</h4>
                <p><strong>Account Holder:</strong> {st.session_state.credentials['username']}</p>
                <p><strong>Account Type:</strong> Checking Account</p>
                <p><strong>Phone Number:</strong> {st.session_state.credentials['phone']}</p>
                <p><strong>Email:</strong> {st.session_state.credentials['email']}</p>
                <p><strong>Available Credit:</strong> $1500</p>
                <table style="width:100%; margin-top: 10px; border-collapse: collapse;">
                    <thead>
                        <tr style="background-color: #4CAF50; color: white;">
                            <th>Date</th>
                            <th>Description</th>
                            <th>Amount</th>
                            <th>Balance</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>2025-02-07</td>
                            <td>Fraudulent Transaction</td>
                            <td style="color: red;">-$1000</td>
                            <td style="color: green;">$4000</td>
                        </tr>
                        <tr>
                            <td>2025-02-06</td>
                            <td>Deposit</td>
                            <td style="color: green;">+$2000</td>
                            <td style="color: green;">$5000</td>
                        </tr>
                        <tr>
                            <td>2025-02-05</td>
                            <td>Withdrawal</td>
                            <td style="color: red;">-$500</td>
                            <td style="color: green;">$3000</td>
                        </tr>
                    </tbody>
                </table>
                <p><strong>Account Status:</strong> Compromised</p>
            </div>
        """, unsafe_allow_html=True)

        st.warning("""
        🔴 You've Been Hacked!  
        You entered sensitive information on an unverified platform.  
        Attacker now has full access to your account.
        """)

        if st.button("Restart Simulation", key="mitm_restart"):
            st.session_state.mitm_step = 1
            st.session_state.credentials = {}
            st.rerun()