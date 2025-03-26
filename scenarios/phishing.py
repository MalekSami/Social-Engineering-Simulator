import streamlit as st
from datetime import datetime

def run_phishing():
    st.title("An unknown device or browser has been used to access your account:")

    # Get today's date
    today_date = datetime.today().strftime('%B %d, %Y')  # e.g., January 23, 2025


    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .email-box {
            padding: 20px;
            border: 1px solid #ddd;
            max-width: 800px;
            margin: auto;
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            height: auto;
        }
        .email-box h3 {
            color: #333;
            margin-bottom: 10px;
            font-size: 20px;
        }
        .email-box p {
            color: #555;
            line-height: 1.4;
            margin: 5px 0;
            font-size: 14px;
        }
        .email-box a {
            color: #1a73e8;
            text-decoration: underline;
        }
        .email-box a:hover {
            opacity: 0.8;
        }
        .email-box hr {
            border: 0;
            height: 1px;
            background: #ddd;
            margin: 10px 0;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .stButton button {
            color: white !important;
            border: none;
            padding: 12px 25px;
            cursor: pointer;
            text-align: center;
            font-size: 16px;
            border-radius: 5px;
            width: 160px;
        }
        .stButton button:first-of-type {
            background-color: #4CAF50 !important;
        }
        .stButton button:last-of-type {
            background-color: #f44336 !important;
        }
        .stButton button:hover {
            opacity: 0.9;
        }
        .highlight {
            background-color: #ffebee;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .footer {
            font-size: 12px;
            color: #777;
        }
        .footer a {
            color: #1a73e8;
        }
        .footer a:hover {
            opacity: 0.8;
        }
        .social-proof {
            background-color: #e8f5e9;
            padding: 12px;
            border-radius: 5px;
            font-size: 14px;
        }
        /* Styling for the answers section */
        .answer-section {
            margin-top: 30px;
            padding: 20px;
            border-radius: 10px;
            background-color: #f4f4f4;
            border: 1px solid #ddd;
            max-width: 800px;
            margin: auto;
            font-family: Arial, sans-serif;
        }
        .answer-header {
            font-size: 18px;
            color: #333;
            margin-bottom: 10px;
            font-weight: bold;
        }
        .answer-text {
            font-size: 14px;
            color: #555;
            margin: 5px 0;
            line-height: 1.5;
        }
        .correct-answer {
            background-color: #d4edda;
            padding: 15px;
            border-left: 5px solid #28a745;
            border-radius: 5px;
            margin: 10px 0;
            color: green;  /* Change text color to black */

        }
        .incorrect-answer {
            background-color: #f8d7da;
            padding: 15px;
            border-left: 5px solid #dc3545;
            border-radius: 5px;
            margin: 10px 0;
            color: red;  /* Change text color to black */

        }
        .answer-icon {
            font-size: 16px;
            margin-right: 10px;
        }
        .result-feedback {
            margin-top: 20px;
            font-size: 16px;
            color: #333;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Email content box with dynamic date
    email_content = f"""
        <div class="email-box">
            <h3>Account Security Notice</h3>
            <p><strong>From:</strong> "Security Team" &lt;security@companyname.com&gt;</p>
            <p><strong>To:</strong> You</p>
            <p><strong>Date:</strong> {today_date}</p>
            <p><strong>Subject:</strong> Urgent: Action Required for Your Account Security</p>
            <hr>
            <p>Dear [User Name],</p>
            <p>We detected unusual activity in your account. For your security, please verify your identity immediately by clicking the link below:</p>
            <p><a href="#" onclick="alert('This is a phishing test! Always check URLs before clicking.');">Verify My Account</a></p>
            <p>Your account will be suspended in <span id="countdown">24:00:00</span>.</p>
            <div class="highlight">
                <p style="color: #c62828; font-weight: bold;">Security Alert: Unusual login attempt detected from a new device.</p>
            </div>
            <p>If you believe this message was sent in error, please <a href="#" onclick="alert('This is a phishing test! Be cautious with unsubscribe links.');">unsubscribe here</a>.</p>
            <hr>
            <div class="social-proof">
                <p><strong>Malek Kabaja</strong> recently verified their account after receiving a similar notification. Protect your account now!</p>
            </div>
            <p>Thank you,<br>Security Team</p>
            <div class="footer">
                <p>This email was sent to you by Company Security Team.</p>
                <p> Riyadh , Olaya , 12271| <a href="#">Support Center</a></p>
            </div>
        </div>
    """
    st.markdown(email_content, unsafe_allow_html=True)

    # Buttons for user interaction
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="button-container">', unsafe_allow_html=True)

        # Check session state for choice made
        if "choice_made" not in st.session_state:
            st.session_state.choice_made = False

        button_disabled = st.session_state.choice_made

        # Create buttons with dynamic disabling
        button_col1, button_col2 = st.columns(2)
        with button_col1:
            if st.button("Verify Account", key="verify", disabled=button_disabled):
                st.session_state.result_message = "Oops! You've fallen for a phishing test. This is a reminder to stay vigilant and think before you click!"
                st.session_state.result_type = "incorrect"
                st.session_state.show_result = True
                st.session_state.choice_made = True  # Mark choice as made
        with button_col2:
            if st.button("Ignore", key="ignore", disabled=button_disabled):
                st.session_state.result_message = "Great job! You passed the phishing test!"
                st.session_state.result_type = "correct"
                st.session_state.show_result = True
                st.session_state.choice_made = True  # Mark choice as made
        st.markdown('</div>', unsafe_allow_html=True)

    # Display the answers section with feedback and result
    if st.session_state.get("show_result", False):
        result_class = "correct-answer" if st.session_state.result_type == "correct" else "incorrect-answer"
        result_icon = "✅" if st.session_state.result_type == "correct" else "❌"
        
        st.markdown(f"""
            <div class="answer-section">
                <div class="{result_class}">
                    <span class="answer-icon">{result_icon}</span>
                    <strong>{st.session_state.result_message}</strong>
                </div>
                <div class="answer-header">Red Flags in This Email:</div>
                <div class="answer-text">- The email creates a sense of urgency (24-hour deadline).</div>
                <div class="answer-text">- The link does not match the company's official domain.</div>
                <div class="answer-text">- The sender's email address looks suspicious.</div>
                <div class="answer-text">- The email asks for personal details or login credentials.</div>
                <div class="answer-text">- There are social proof elements that try to create a sense of urgency or trust.</div>
            </div>
        """, unsafe_allow_html=True)

# Initialize session state
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# Run the phishing simulation
if __name__ == "__main__":
    run_phishing()
