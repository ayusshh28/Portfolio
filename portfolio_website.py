# --- Import necessary libraries ---
import streamlit as st

from streamlit_lottie import st_lottie
import json
import joblib
import pandas as pd
import requests


# --- Page Configuration ---
st.set_page_config(page_title="Ayush's Portfolio", layout="wide")






# ---- Sidebar Styling ----
st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
        background: linear-gradient(to bottom right, #0f2027, #2c5364);
        justify-content: center;
        align-items: center;
        color: white;
        padding: 30px 15px;
        border-radius: 0 20px 20px 0;
        box-shadow: 2px 0 12px rgba(0,0,0,0.1);
        min-width: 320px !important;
        width: 320px !important;
        }


        .sidebar-title {
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
            background: linear-gradient(90deg, #FFDE59, #FF914D);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .sidebar-tab-container {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .sidebar-tab:hover {
            background-color: rgba(255, 255, 255, 0.2);
        }

        .main > div {
            padding-top: 0rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Sidebar Title ----
st.sidebar.markdown("<div class='sidebar-title'>🚀 Navigation Panel</div>", unsafe_allow_html=True)

# ---- Define Tabs ----
tabs = {
    "🏠 Home": "#4caf50",
    "ℹ️ About Me": "#2196f3",
    "💼 Projects": "#9c27b0",
    "📬 Contact": "#f44336"
}

# ---- Handle Selection via Session ----
if "selection" not in st.session_state:
    st.session_state.selection = list(tabs.keys())[0]

selection = st.session_state.selection

# ---- Render Sidebar Tabs ----
st.sidebar.markdown("<div class='sidebar-tab-container'>", unsafe_allow_html=True)

for tab, color in tabs.items():
    is_active = (tab == selection)
    button_color = color if is_active else "#ffffff22"
    text_color = "black" if is_active else "white"
    font_weight = "bold" if is_active else "normal"

    if st.sidebar.button(tab, key=tab):
        st.session_state.selection = tab
        selection = tab

st.sidebar.markdown("</div>", unsafe_allow_html=True)










# --- Custom CSS Styling ---
st.markdown("""
    <style>
     @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
       

    body, .main {
        background-color: #f9f9f9;
        font-size: 16px !important;
        
    }

    .main .block-container {
    max-width: 100% !important;
    padding: 1rem 3rem 4rem 2rem; /* top, right, bottom, left */
    margin-top: -40px !important; /* pulls all tab content upward */
    }

            
    
    .stTabs [role="tab"] {
        font-size: 18px;
        padding: 10px ;
        background: #f0f0f0;
        color: #333;
        border-radius: 10px 10px 0 0;
        margin-left:20px;
    }
    .stTabs [role="tab"][aria-selected="true"] {
        background: #aed581;
        color: black;
    }
    .stButton>button {
        background-color:  rgba(44, 83, 100, 0.4);
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
        
    }
            
            
    </style>
""", unsafe_allow_html=True)




# --- Home Section ---



if selection == "🏠 Home":
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700;900&display=swap" rel="stylesheet">
        <style>
            html, body, [class*="css"]  {
                font-family: 'Poppins', sans-serif;
            }

            .home-container {
                padding: 50px 80px;
                animation: fadeIn 1.2s ease-in;
            }

            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(20px); }
                100% { opacity: 1; transform: translateY(0); }
            }

            .home-heading {
                font-size: 90px;
                font-weight: 900;
                margin-bottom: 10px;
                background: linear-gradient(to right, #FF914D, #FFDE59);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            .typing {
                font-size: 24px;
                color: black;
                margin-bottom: 20px;
                border-right: 3px solid #FFDE59;
                white-space: nowrap;
                overflow: hidden;
                width: 0;
                animation: typing 3s steps(21, end) forwards;
            }

            @keyframes typing {
                from { width: 0 }
                to {  width: 21ch; }
            }

         

            .home-description {
                font-family: 'Poppins';
                font-size: 19px;
                font-weight: 300;
                line-height: 1.6;
                color: black;
            }


            }

        </style>
    """, unsafe_allow_html=True)

    # Optional background block (wrap section)
    # st.markdown("<div style='background-color: #1e1e2f; border-radius: 12px;'>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
            <div class="home-container">
                <h5>Hello! </h5>
                <h1 class="home-heading">I'm Ayush Katiyar</h1>
                <div class="typing">Aspiring AI/ML Engineer</div>
                <p class="home-description">
                    I'm a motivated and dedicated student with a strong passion for Artificial Intelligence (AI) and Machine Learning (ML).<br><br>
                    My interests span across Natural Language Processing, Computer Vision, and Data-Driven Problem Solving. I enjoy building intelligent systems that solve real-world challenges and thrive in collaborative environments where innovation happens.
                </p>

            </div>
        """, unsafe_allow_html=True)

        left, center, right = st.columns([0.4, 2, 1.6])

        # Put the button in the center column
        with center:
            with open("resume/CV.pdf", "rb") as file:
                st.download_button(
                    label="📄 Download CV",
                    data=file,
                    file_name="CV_AyushKatiyar.pdf",
                    mime="application/pdf",
                    key="download_cv_button"
                )
    with col2:
        st.markdown(
            """
            <style>
            .styled-image {
                display: flex;
                justify-content: center;
                margin-top: 60px;
                margin-bottom: 20px;
            }
            </style>
            <div class='styled-image'>
            """,
            unsafe_allow_html=True
        )

        st.image("images/me.png", width=300)

        st.markdown("</div>", unsafe_allow_html=True)


        # Inject custom class to image manually
        # st.markdown("""
        #     <script>
        #         const imgs = parent.document.querySelectorAll('img');
        #         for (const img of imgs) {
        #             if (img.src.includes("images/me.png")) {
        #                 img.classList.add("profile-img");
        #             }
        #         }
        #     </script>
        # """, unsafe_allow_html=True)

    # End background block
    st.markdown("</div>", unsafe_allow_html=True)

#    --------------------------------------------------------------



# --- About Section ---
elif selection == "ℹ️ About Me":
    
        st.subheader("About Me") 

        st.markdown(
            """
            <style>
            body {
                background-color: #f5f5f5;
            }
            .skill-tag {
                display: inline-block;
                padding: 8px 16px;
                margin: 6px ;
                background-color: #ffffff;
                color: #333;
                border: 1px solid #ccc;
                border-radius: 10px;
                font-size: 15px;
                font-family: 'Segoe UI', sans-serif;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                font-family: 'Segoe UI', sans-serif;
            }
            th, td {
                padding: 12px;
                border: 1px solid #ddd;
                text-align: center;
                font-size: 15px;
            }
            th {
                background-color: #c4f2f6;
                color: #333;
            }
            td {
                background-color: #f1efff;
                color: #222;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Tabs
        tab1, tab2 , tab3= st.tabs(["🎓 Education","💼 Skills","📜 Certifications"])




        # --------- Tab 2: Education ---------
        with tab1:
            st.markdown("<h3 style='font-size: 25px; font-weight: 600;'>🎓 Education</h3>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            education_table = """
            <table>
            <thead>
                <tr>
                <th>Qualification</th>
                <th>Stream</th>
                <th> Passout Year</th>
                <th>Institute</th>
                <th>City/State</th>
                <th>Score</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <td>BCA</td>
                <td>-</td>
                <td>2024</td>
                <td>Babu Banarasi Das University</td>
                <td>Lucknow, Uttar Pradesh</td>
                <td>8.6 CGPA</td>
                </tr>
                <tr>
                <td>12th</td>
                <td>Science</td>
                <td>2020</td>
                <td>Wendy High School</td>
                <td>Kanpur, Uttar Pradesh</td>
                <td>82%</td>
                </tr>
                <tr>
                <td>10th</td>
                <td>-</td>
                <td>2018</td>
                <td>Wendy High School</td>
                <td>Kanpur, Uttar Pradesh</td>
                <td>87%</td>
                </tr>
            </tbody>
            </table>
            """
            st.markdown(education_table, unsafe_allow_html=True)


                    # --------- Tab 1: Skills ---------
        with tab2:
            st.markdown("<h3 style='font-size: 25px; font-weight: 600;'>💼 Skills & Tools</h3>", unsafe_allow_html=True)

            # Add CSS for wrapping in 4 rows
            st.markdown("""
                <style>
                .skills-container {
            display: flex;
            flex-wrap: wrap;
            gap: 12px 14px;
            margin-top: 15px;
        }
                }
                .skill-tag {
            display: inline-block;
            padding: 10px 18px;
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #aaa;
            border-radius: 10px;
            font-size: 14px;
            font-weight: 500;
            line-height: 1.4;
            height: 42px;
            box-shadow: 1px 1px 4px rgba(0,0,0,0.08);
            white-space: nowrap;
        }
                </style>
            """, unsafe_allow_html=True)

            skills = [
                "Python", "SQL", "Matplotlib", "Seaborn", "NLP",
                "Pandas", "Power BI", "Tableau", "NumPy", "Streamlit",
                "Excel", "Scikit-learn", "HuggingFace Transformers", "GitHub",
                "Django", "HTML5", "CSS3", "Bootstrap", "Git"
            ]

            # Wrap all skills
            skill_html = '<div class="skills-container">' + ''.join(
                f"<div class='skill-tag'>{skill}</div>" for skill in skills
            ) + '</div>'
            
            st.markdown(skill_html, unsafe_allow_html=True)


        with tab3:  # Adjust tab index as per your layout
            st.markdown("<h3 style='font-size: 25px; font-weight: 600;'>🎓 Certifications</h3>", unsafe_allow_html=True)

            st.markdown("""
                <p style='font-size:17px; line-height: 1.9;'>

                <b>📘 Data Analysis Foundation</b> — LinkedIn Learning (2024)<br>
                <b>🗃️ SQL & Relational Databases 101</b> — CognitiveClass.ai (IBM) (2024)<br>
                <b>🐍 Python for Data Science (PY0101EN)</b> — IBM Developer Skills Network (2024)<br>
                <b>📊 Data Analysis using Microsoft Excel</b> — Coursera (2024)<br><br>

                <b>🏢 Deloitte Data Analytics Virtual Experience</b> — Forage (2024)<br>
                Gained hands-on experience in solving real-world business problems through data wrangling, visualization, and reporting.<br><br>

                <b>🏢 Tata Data Visualisation Virtual Experience</b> — Forage (2024)<br>
                Created interactive dashboards and data storytelling reports to guide strategic decision-making in a simulated business context.<br><br>

                🔗 <b>GitHub Repository (Certificates Folder)</b>:  
                <a href="https://github.com/ayusshh28/Certificates" target="_blank">
                    View All Certificates
                </a>

                </p>
            """, unsafe_allow_html=True)


# ---------------------------------------------------------------------------------------------------------------------------------------

# --- Services Section ---
elif selection == "💼 Projects":
    st.subheader("💼 My Projects")
    st.markdown("<br>", unsafe_allow_html=True)
    service_tabs = st.tabs(["🧠 LensX (NLP Suite)", "📊 Data Dashboards","🏦 Banking Automation System" ,"📄 Resume Builder"])
    with service_tabs[0]:
    # Load Models



        spam_model=joblib.load("spam_detect.pkl")
        language_model=joblib.load("lang_detect.pkl")
        news_model=joblib.load("news_category.pkl")
        review_model=joblib.load("review.pkl")


        # ---------------------------
        # Load Lottie animation from URL or local JSON
        # ---------------------------
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()



        # Custom CSS
        st.markdown("""
            <style>

            .lensx-tabs{
                    margin-top:40px;
                    }

            .lensx-box {
                padding: 10px 20px;
                border-left: 6px solid #2563eb;
                background-color: #f1f5f9;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
                margin-bottom:40px;
            }

            .lensx-title {
                font-size: 54px;
                font-weight: 900;
                color: #1e3a8a;
                text-shadow: 2px 2px #dbeafe;
                
            }

            .lensx-subtitle {
                font-size: 20px;
                font-weight: 500;
                color: #1e3a8a;

                
            }

            .stButton > button[kind="primary"] {
                background: var(--gradient);
                color: #fff;
                border: none;
                padding: 0.7rem 2.2rem;
                border-radius: 50px;
                font-weight: 600;
                transition: all 0.3s ease;
            }

            .stButton > button[kind="primary"]:hover {
                filter: brightness(1.1);
                transform: translateY(-2px);
                box-shadow: var(--shadow);
            }

                    

            </style>
        """, unsafe_allow_html=True)






        # ---------------------------
        # Load assets & models
        # ---------------------------
        lottie_nlp = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_qp1q7mct.json")

        # ---------------------------
        # Header Section: Lottie + Branding
        # ---------------------------
        col1, col2 = st.columns([2, 3])
        with col1:
            st_lottie(lottie_nlp, height=160, speed=1)
        with col2:
            st.markdown("""
                <div class="lensx-box">
                    <div class="lensx-title">LensX </div>
                <span class="lensx-subtitle"> (Lens Expert - NLP Suite) </span>  
                <div style='font-size: 1rem; color: #444; margin-top: 0.4rem; font-weight:bold'>
                    <em>From Spam to Sentiment – Know It All with <strong style='color: #1e3a8a'>LensX</strong></em>
                </div>
                </div>
                        
           

            """, unsafe_allow_html=True)

        # ---------------------------
        # Tabs layout
        # ---------------------------



        st.markdown("""
            <div style="margin-top: 30px; ">
                <h4 style="color:#1e3a8a;">📌 Project Overview: LENSX</h4>
                <p><strong>LENSX (LENS Expert)</strong> is a multi-model NLP suite built using Streamlit.</p>
                <p>It showcases 4 core text classification tasks:</p>
                <ul>
                    <li>🚨 <strong>Spam Detection</strong></li>
                    <li>🌐 <strong>Language Identification</strong></li>
                    <li>🍽️ <strong>Review Sentiment Analysis</strong></li>
                    <li>📰 <strong>News Classification</strong> <em>(under maintenance)</em></li>
                </ul>
                <p >🔧 Powered by <strong>Python</strong>, <strong>Scikit-learn</strong>, and real-world datasets, <br>
                LENSX serves as an interactive, educational NLP demo tool.</p>
            </div>
        """, unsafe_allow_html=True)



        

        st.markdown('<div class="lensx-tabs">', unsafe_allow_html=True)

        

        spam_tab, lang_tab, review_tab, news_tab = st.tabs([
            "🚨 Spam Classifier",
            "🌐 Language Detection",
            "🍽️ Review Sentiment",
            "📰 News Classification",
        ])

        st.markdown('</div>', unsafe_allow_html=True)


        # === 1. Spam Classifier ===
        with spam_tab:
            st.subheader("🔍 Detect whether a message is Spam or Not Spam")
            msg = st.text_input("Enter a message")
            if st.button("Classify"):
                prediction = spam_model.predict([msg])
                if prediction[0]==0:

                    st.error("🚫 Spam Alert! This message appears to be spam.")
                    st.markdown("### 🧨 Message flagged as SPAM!")
                    st.markdown("Be cautious while interacting with this message.")
                
                
                else:
                    st.success("✅ This message is clean and not spam.")
                    st.balloons()



            st.divider()
            uploaded_spam = st.file_uploader("Batch classify messages (CSV/TXT)", type=["csv", "txt"], key="spam_upload")
            if uploaded_spam:
                try:
                    lines = uploaded_spam.read().decode("utf-8").splitlines()
                    df_spam = pd.DataFrame(lines, columns=['Msg'])
                    df_spam["Prediction"] = pd.Series(spam_model.predict(df_spam['Msg'])).map({0: "Spam", 1: "Not Spam"})
                    df_spam.index += 1
                    st.dataframe(df_spam, use_container_width=True)
                except Exception as e:
                    st.error(f"Error processing file: {e}")

        # === 2. Language Detection ===
        with lang_tab:
            st.subheader("🌍 Identify the language of a text snippet")
            text_input = st.text_input("Enter text to detect language", key="lang_input")
            if st.button("Detect", key="lang_detect_btn") and text_input:
                lang_pred = language_model.predict([text_input])[0]
                st.success(f"Detected Language: **{lang_pred}**")

            st.divider()
            uploaded_lang = st.file_uploader("Batch detect languages (CSV/TXT)", type=["csv", "txt"], key="lang_upload")
            if uploaded_lang:
                try:
                    lines = uploaded_lang.read().decode("utf-8").splitlines()
                    df_lang = pd.DataFrame(lines, columns=["Text"])
                    df_lang["Language"] = pd.Series(language_model.predict(df_lang["Text"]))
                    df_lang.index += 1
                    st.dataframe(df_lang, use_container_width=True)
                except Exception as e:
                    st.error(f"Error processing file: {e}")

        # === 3. Review Sentiment ===
        with review_tab:
            st.subheader("🍽️ Analyse restaurant review sentiment")
            review_text = st.text_input("Write a restaurant review", key="review_input")
            if st.button("Analyse", key="review_btn") and review_text:
                review_pred = review_model.predict([review_text])[0]
                if review_pred:
                    st.success("😊 Positive Review")
                    st.balloons()
                else:
                    st.error("😞 Negative Review")

            st.divider()
            uploaded_reviews = st.file_uploader("Batch analyse reviews (CSV/TXT)", type=["csv", "txt"], key="review_upload")
            if uploaded_reviews:
                try:
                    lines = uploaded_reviews.read().decode("utf-8").splitlines()
                    df_reviews = pd.DataFrame(lines, columns=["Review"])
                    df_reviews["Sentiment"] = pd.Series(review_model.predict(df_reviews["Review"])).map({0: "Negative", 1: "Positive"})
                    df_reviews.index += 1
                    st.dataframe(df_reviews, use_container_width=True)
                except Exception as e:
                    st.error(f"Error reading file: {e}")

        with news_tab:
            st.markdown("""
            <div style="padding: 20px; background-color: #fff3cd; border-left: 6px solid #ffa500; font-size: 16px;">
                ⚠️ <strong>News Classifier is currently under maintenance.</strong><br>
                We're working hard to improve it. Please check back later!
            </div>
            """, unsafe_allow_html=True)

# --------------------------------------------------------------------------------------------------------------------------------------

        # Inject custom CSS to round corners of Streamlit images
        st.markdown("""
            <style>
   
            .section-heading {
                font-size: 25px;
                margin-top: 20px;
                margin-bottom: 10px;
                color: #4B4B4B;
            }
            </style>
        """, unsafe_allow_html=True)

        with service_tabs[1]:
            st.markdown('<h3 class="section-heading">📊 Power BI Dashboards</h3>', unsafe_allow_html=True)

            # 1️⃣ IPL Dashboard
            col1, spacer1, col2 = st.columns([1, 0.2, 2])
            with col1:
                with st.container():
                    st.markdown('<div class="rounded-img">', unsafe_allow_html=True)
                    st.image("./images/IPL.png", caption="IPL Dashboard", use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
            with col2:
                st.subheader("IPL Performance Dashboard (2008–2024)")
                st.write("""
                This Power BI dashboard tracks 17 seasons of IPL:  
                - Top run scorers & wicket takers  
                - Head-to-head stats  
                - Interactive filters for teams & players  
                - Season summaries & trends  
                """)
                st.markdown("[🔗 View Full Dashboard](https://github.com/ayusshh28/PowerBI-Dashboards/tree/main/IPL_Dashboard)", unsafe_allow_html=True)

            st.divider()

            # 2️⃣ World Cup Dashboard
            col3, spacer2 ,col4 = st.columns([1, 0.2, 2])
            with col3:
                with st.container():
                    st.markdown('<div class="rounded-img">', unsafe_allow_html=True)
                    st.image("./images/worldcup.png", caption="Cricket World Cup 2023",use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
            with col4:
                st.subheader("Cricket World Cup 2023 Dashboard")
                st.write("""
                Breakdown of team & player performance in the 2023 World Cup:  
                - Match scores, points table, NRR  
                - Top batsmen & bowlers  
                - Match filters by team & venue  
                - Visual match summaries  
                """)
                st.markdown("[🔗 View Full Dashboard](https://github.com/ayusshh28/PowerBI-Dashboards/tree/main/Worldcup_Dashboard)", unsafe_allow_html=True)

            st.divider()

            # 3️⃣ Environment Dashboard
            col5,spacer3, col6 = st.columns([1, 0.2, 2])
            with col5:
                with st.container():
                    st.markdown('<div class="rounded-img">', unsafe_allow_html=True)
                    st.image("./images/Environment.png", caption="Environment Analysis", use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
            with col6:
                st.subheader("Global Environmental Trends (2000–2023)")
                st.write("""
                An analysis of global environmental indicators:  
                - CO₂ emissions, temperature rise, rainfall  
                - Sea level, forest cover & renewable energy  
                - Yearly trends with country-wise breakdown  
                - Visual correlation between climate indicators  
                """)
                st.markdown("[🔗 View Full Dashboard](https://github.com/ayusshh28/PowerBI-Dashboards/tree/main/Environment_Dashboard)", unsafe_allow_html=True)



        with service_tabs[2]:
            st.markdown("""
            <div style="margin-top:20px;"></div>

            ### 🏦 Banking Automation System

            A desktop-based Python application that simulates core banking operations.  
            This project focuses on automation of basic financial tasks with a clean interface.

            **🔑 Key Features:**
            - 🧾 Account creation & management  
            - 💰 Deposit & withdrawal functionality  
            - 🧮 Transaction history & balance check  
            - 🔐 Secure login system  

            **🛠️ Tech Stack:**  
            Python · Tkinter · File Handling

            🔗 [View Source on GitHub](https://github.com/ayusshh28/Banking-Automation-Project)
            """,unsafe_allow_html=True)


        with service_tabs[3]:
            st.markdown("### 📝 Resume Builder")
            st.write("Coming soon: Input your details and get a PDF resume generated.")
# -----------------------------------------------------------------------------------------------------------------------------------------





# --- Contact Section ---
elif selection == "📬 Contact":
    st.markdown("<div style='margin-top: 30px; '></div>", unsafe_allow_html=True)
    st.markdown("<h2>📬 Contact Me</h2>", unsafe_allow_html=True)
    st.markdown("<p style= font-size:16px; color:gray; '>I'd love to hear from you. Reach out anytime!</p>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    # Left Column: Contact Info with styling, icons untouched
    with col1:
        st.markdown("""
        <div style='padding: 20px; background-color: #f9f9f9; border-radius: 10px; margin-top:30px;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08); font-size: 17px; line-height: 2.7;'>
            <p>
                <i class="fas fa-envelope" style="margin-right: 12px;"></i> 
                <strong>Email:</strong> 
                <a href="mailto:ayusshh28@gmail.com" style="text-decoration: none; color: #333;">ayusshh28@gmail.com</a><br>
                <i class="fas fa-phone" style="margin-right: 12px;"></i> 
                <strong>Phone:</strong> 
                <a href="tel:7068184204" style="text-decoration: none; color: #333;">7068184204</a><br>
                <i class="fab fa-github" style="margin-right: 12px;"></i> 
                <a href="https://github.com/ayusshh28" target="_blank" style="text-decoration: none; color: #333;">GitHub</a><br>
                <i class="fab fa-linkedin" style="margin-right: 12px;"></i> 
                <a href="www.linkedin.com/in/ayushh-katiyar" target="_blank" style="text-decoration: none; color: #0e76a8;">LinkedIn</a><br>
                <i class="fab fa-instagram" style="margin-right: 12px;"></i> 
                <a href="https://www.instagram.com/yourusername" target="_blank" style="text-decoration: none; color: #C13584;">Instagram</a><br>
                <i class="fab fa-facebook" style="margin-right: 12px;"></i> 
                <a href="https://www.facebook.com/yourusername" target="_blank" style="text-decoration: none; color: #3b5998;">Facebook</a>
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Right Column: Contact Form with improved design
    with col2:
        st.markdown(
            """
            <div style='margin-top: 30px; margin-left: 30px; margin-right: 10px;'>
            """,
            unsafe_allow_html=True
        )

        with st.form("contact_form"):
            st.markdown("#### ✍️ Send a Message", unsafe_allow_html=True)

            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message", height=150)

            submitted = st.form_submit_button("📨 Submit")
            if submitted:
                st.success("✅ Thank you! Your message has been sent.")

        st.markdown("</div>", unsafe_allow_html=True)






   
