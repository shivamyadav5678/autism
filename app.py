import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Early Autism Detection",
    layout="wide",
    page_icon="🧠"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Custom styling for the .read-more-button link */
    .read-more-button {
        background-color: red;
        color: white !important;  /* Set text color to white */
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        text-decoration: none;  /* Remove underline */
        display: inline-block;
        margin-top: 20px;  /* Added space between the button and image */
    }
    
    }
    .read-more-button:focus {
        outline: none;  /* Remove outline on focus */
        text-decoration: none;
        border-radius: 5px;
    }
      .read-more-button:hover {
        outline: none;  /* Remove outline on focus */
        text-decoration: none;
        border-radius: 5px;
    }
    .main {
        background-color: #black;
        font-family: 'Arial', sans-serif;
    }
    .header {
        color: #004080;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .sub-header {
        color: #008080;
        font-size: 22px;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .footer {
        color: #666666;
        text-align: center;
        margin-top: 50px;
        font-size: 16px;
    }
    a {
        text-decoration: none;
        color: white;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<div class='header'>Early Autism Detection in Children Using Python</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>A Machine Learning Approach for Early Intervention</div>", unsafe_allow_html=True)

# Introduction Section
st.markdown(
    """
    ### What is Autism?
    Autism, or Autism Spectrum Disorder (ASD), is a developmental condition that affects how individuals perceive, communicate, and interact with others. 
    It is characterized by a range of symptoms, such as challenges with social skills, repetitive behaviors, and unique strengths or differences. 
    While the severity and impact of autism vary greatly, early diagnosis and intervention can significantly improve outcomes for children and their families.
    """,
    unsafe_allow_html=True
)

# "Read More" Button with proper styling
st.markdown(
    """
    <a href="https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders" target="_blank" class="read-more-button">
        Read More
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    """,
    unsafe_allow_html=True
)
# Image or Logo
image_url = "https://www.homage.sg/wp-content/uploads/2022/04/Signs-of-autism-1536x864.jpg"
st.image(image_url, caption="Empowering Families Through Technology", use_column_width=True)

# Welcome Section
st.markdown(
    """
    #### Welcome to the Autism Detection Platform
    Our project aims to provide an **efficient** and **user-friendly tool** for the early detection of autism in children. 
    Using advanced **Python-based machine learning algorithms**, this platform analyzes behavioral patterns to identify potential signs of autism. 
    By facilitating **early intervention**, we strive to make a positive impact on the lives of children and their families.
    """,
    unsafe_allow_html=True,
)

# Two-column Layout for Features
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Key Features:")
    st.write("- **AI-Powered Assessments** for analyzing patterns.")
    st.write("- **Interactive Questionnaires** for parents and caregivers.")
    st.write("- **Actionable Insights** for next steps and resources.")

with col2:
    st.markdown("### Why Early Detection Matters?")
    st.write("- Early diagnosis leads to more effective interventions.")
    st.write("- Supports child development and family planning.")
    st.write("- Reduces stress for families by providing clarity.")

# Call to Action
st.markdown(
    """
    ---
    ### Ready to Get Started?
    Use the **sidebar** to navigate to different pages and explore the platform!
    """,
    unsafe_allow_html=True
)


