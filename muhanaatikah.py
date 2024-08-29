import streamlit as st
import base64
from streamlit_option_menu import option_menu
import requests

st.set_page_config(page_icon='🧕', layout= 'wide', initial_sidebar_state="auto")
# Menyisipkan CSS untuk memaksa light mode
st.markdown(
    """
    <style>
        /* Memaksa tampilan light mode */
        body {
            background-color: #ffffff; /* Warna latar belakang putih */
            color: #000000; /* Warna teks hitam */
        }
        .css-1d391kg {
            background-color: #ffffff; /* Warna latar belakang light untuk sidebar */
            color: #000000; /* Warna teks hitam untuk sidebar */
        }
        .css-1bymd8g {
            color: #000000; /* Warna teks light untuk header dan elemen lainnya */
        }
        /* Tambahkan aturan CSS lainnya sesuai kebutuhan untuk memastikan light mode */
    </style>
    """,
    unsafe_allow_html=True
)

# Hero Section

st.title("Muhana Atikah")
st.write("""
        Graduated from Business Statistics at Sepuluh Nopember Institute of Technology who is interested in the field of data and having 1 year experience in data quantitative/data analyst""")
    
# Tombol "Contact Me" yang mengarahkan ke bagian kontak di bawah
st.markdown(
    """
    <div style="display: flex; align-items: center; gap: 20px; justify-content: flex-start;">
        <a href="https://github.com/Hanatika" target="_blank">
            <img src="https://logos-download.com/wp-content/uploads/2016/09/GitHub_logo.png" alt="GitHub Logo" style="width:26px;">
        </a>
        <a href="https://www.linkedin.com/in/muhana-atikah" target="_blank">
            <img src="https://pngimg.com/uploads/linkedIn/linkedIn_PNG8.png" alt="LinkedIn Logo" style="width:26px;">
        </a>
        <a href="https://drive.google.com/file/d/1ebJxPhrG_4tHVPygpbthi66fz6GkDaz7/view?usp=sharing" target="_blank">
            <button style="background-color:#93CAED; padding: 3px 10px; border-radius: 5px; border: none; color: black; font-size: 16px;">
                Resume
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

#menu option
st.write('---')
with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Projects', 'Contact'],
        icons = ['person', 'code-slash', 'chat-left-text-fill'],
        orientation = 'horizontal'
    )
if selected == 'About':
    with st.container():
        col1, col2 = st.columns([0.3,1], gap="medium")
        with col1:
            st.image('assets/foto_ika_circle.png')
        with col2:
            st.write('#')
            st.subheader('Hi There, I am Tika')
            st.title('Business Statistics ITS')
            


    st.write('---')
    
    # CSS untuk membuat teks di dalam kolom berada di tengah
    st.markdown(
        """
        <style>
        .center-text {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Menggunakan columns dengan pengaturan kolom proporsional
    with st.container():
        col1, col3, col2 = st.columns([1, 2, 1])
        with col3:
            st.markdown('<div class="center-text">', unsafe_allow_html=True)
            st.markdown("## 🎓 Education")
            st.write("""
            **Formal Education**
            
            - Diploma IV - Business Statistics (2022 - 2024)
            - Diploma III - Statistics (2018 - 2021)
            """)

            st.write("""
            **Non-Formal Education**
            
            - Bootcamp Data Science by Rakamin Academy (7 Months)
            - Data Analytics Academy by Coding Studio (3 Months)
            """)
            st.markdown('</div>', unsafe_allow_html=True)

    with st.container():
        col1, col4, col2 = st.columns([1, 2, 1])
        with col4:
            st.markdown('<div class="center-text">', unsafe_allow_html=True)
            st.markdown("## 📋 Skills")
            st.write("""
            - **Data Analysis:** Data Collection, Data Cleaning, Data Preprocessing, Exploratory Data Analysis (EDA), Descriptive Statistics
            - **Programming Languages:** Python, SQL, R
            - **Tools:** Looker Studio, Google Colaboratory/Jupyter, R Studio, Excel/Spreadsheet, SPSS
            - **Databases:** PostgreSQL, MySQL
            """)
            st.markdown('</div>', unsafe_allow_html=True)

    with st.container():
        col1, col5, col2 = st.columns([1,2,1])   
        with col5:
            st.markdown("## ✒️Experience")
            st.write("""
                        - HRGA Analyst - Internship
                        - Data Collection - Freelance
                        """)

if selected == 'Projects':
    with st.container():
        st.header('My Projects')
        st.write('#')
        col6, col7 = st.columns((1,2.5))
        with col6:
            st.image('assets/resto.png')
        with col7:
            st.subheader('Restaurant Orders Dashboard')
            st.write('Creating a Restaurant Orders Dashboard for visualizing data and provides a comprehensive overview of a restaurants operational performance based on order data. This dashboard is designed to assist restaurant management in making more informed decisions, improving efficiency, and identifying growth opportunities')
            # Membuat tombol
            st.markdown("""
            <a href="https://lookerstudio.google.com/reporting/b357af35-231f-44e0-915e-1581a58369e8" target="_blank">
            <button style="background-color:White;">See More</button>
            </a>
            """, unsafe_allow_html=True)
        
        st.write('#')
        col8, col9 = st.columns((1,2.5))
        with col8:
            st.image('assets/ecom.png')
        with col9:
            st.subheader('The Look E-Commerce Report')
            st.write('The Look Users E-commerce Report that provides an in-depth analysis of The Looks online business performance. This report presents data and information related to e-commerce users. Its primary purpose is to offer valuable insights to management for making strategic decisions and identifying growth opportunities.')
            # Membuat tombol
            st.markdown("""
            <a href="https://lookerstudio.google.com/reporting/a8d88018-12f3-4442-b8ba-e01e52b78ea1" target="_blank">
            <button style="background-color:White;">See More</button>
            </a>
            """, unsafe_allow_html=True)
           
        st.write('#')
        col10, col11 = st.columns((1,2.5))
        with col10:
            st.image('assets/senti.png')
        with col11:
            st.subheader('Sentiment Analysis Gobis Application Review')
            st.write('Sentiment analysis of Gobis app reviews for identifying and quantifying the opinions or sentiments expressed in user reviews about the app. showed from background to insight of analysis to understand whether users feel positive or negative about the service provided by Gobis.')
            # Membuat tombol
            # Membuat tombol
            st.markdown("""
            <a href="https://drive.google.com/file/d/1ubUl_Q7mp92va9w4I4T9X3vwWVjy3yig/view?usp=sharing" target="_blank">
            <button style="background-color:White;">See More</button>
            </a>
            """, unsafe_allow_html=True)

        st.write('#')
        col12, col13 = st.columns((1,2.5))
        with col12:
            st.image('assets/lda.png')
        with col13:
            st.subheader('Topic Modelling Using Laten Dirichlet Allocation')
            st.write('Topic modelling using LDA from employee comment text, a generative statistical model that assumes documents are a mixture of topics, and each topic is a distribution over words.')
            # Membuat tombol
            st.markdown("""
            <a href="https://drive.google.com/file/d/1s3VmWFudIW__MFuzyatzkbpa73PDN1_8/view?usp=drive_link" target="_blank">
            <button style="background-color:White;">See More</button>
            </a>
            """, unsafe_allow_html=True)

        st.write('#')
        col12, col13 = st.columns((1,2.5))
        with col12:
            st.image('assets/employee.png')
        with col13:
            st.subheader('Employee Satisfaction Dashboard')
            st.write('reating a visual representation of key metrics related to how satisfied employees are with office facility. It provides an index satisfaction each office and helps organizations identify areas where improvements can be made.')
            # Membuat tombol
            st.markdown("""
            <a href="https://lookerstudio.google.com/reporting/6ee5db35-4eb5-46d8-adab-d036137a2dbe" target="_blank">
            <button style="background-color:White;">See More</button>
            </a>
            """, unsafe_allow_html=True)

if selected == 'Contact':
    # Konten kontak di bagian paling bawah halaman
    st.markdown('<a name="contact-section"></a>', unsafe_allow_html=True)
    st.subheader("Contact Me")
    st.write("Want To Connect? Feel Free Contact Me On")

    # Informasi kontak
    st.write(" **Email**: muhanaatikah28@gmail.com")
    st.write(" **Phone**: (+62) 812-6750-6250")
    st.write(" **Location**: Surabaya, Indonesia")



st.write('---')
st.markdown(
    """
    <style>
        .footer {
            width: 100%;
            background-color: transparent; /* Warna transparan agar menyatu dengan background */
            color: #000;
            text-align: center;
            padding: 10px 0;
            margin-top: 50px; /* Jarak antara konten dan footer */
            position: relative;
            bottom: 0;
        }
        .footer .left {
            float: left;
            margin-left: 20px;
        }
        .footer .right {
            float: right;
            margin-right: 20px;
        }
        .footer::after {
            content: "";
            display: table;
            clear: both;
        }
    </style>

    <div class="footer">
        <div class="left">
            Email: <a href="mailto:email@example.com">muhanaatikah28@gmail.com</a> | Surabaya, Indonesia
        </div>
        <div class="right">
            © 2024 Muhana Atikah
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

