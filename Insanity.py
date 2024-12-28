import streamlit as st
st. set_page_config(layout="wide")
tab1, tab2 = st.tabs(["Home", "Apply"])


with tab1:
    tab1.title("The <name> Program")
    col1, col2 = st.columns([3,2])
    col1.image("https://www.loans.com.au/contentAsset/image/26c57517-4aaa-4137-8377-fb170de877ee")
    col2.subheader("About This Project")
    col2.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    tab1.divider()
    st.markdown(
        """
        <style>
    img {
        border-radius: 35px 35px 25px 25px;
        padding-top: 15px;
        padding-right: 10px;
    }
    .st-emotion-cache-10trblm{
        padding-top:12px;
    }

    </style>
    """
    ,
    unsafe_allow_html=True
    )
    
with tab2:
    st.markdown(

    """
  <iframe
    id="surveylegend-survey"
    src="https://s.surveylegend.com/-OFD7swlIZw7a72rT4ga"
    width="100%"
    height="1000px"
    loading="lazy"
    style="frameborder: 0; border: 0; margin: 0 auto;"
>
</iframe>

    """,
    unsafe_allow_html=True
)
    
