import streamlit as st
import pandas as pd
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text, read_pdf


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    
    input_type = st.radio("Select Input Type:", ["Single URL", "Upload CSV"])
    urls = []

    if input_type == "Single URL":
        url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
        if url_input:
            urls = [url_input]
    else:
        uploaded_file = st.file_uploader("Upload CSV file (must contain 'url' column)", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            if 'url' in df.columns:
                urls = df['url'].tolist()
            else:
                st.error("CSV file must contain a 'url' column")

    tone_input = st.selectbox("Select Tone", ["Formal", "Casual", "Persuasive", "Standard"])
    
    # Portfolio Upload
    st.sidebar.header("Portfolio Settings")
    portfolio_file = st.sidebar.file_uploader("Upload Resume/Portfolio (PDF)", type="pdf")
    custom_portfolio_data = None
    
    if portfolio_file:
        try:
            resume_text = read_pdf(portfolio_file)
            with st.spinner("Extracting portfolio items from resume..."):
                custom_portfolio_data = llm.extract_portfolio_items(resume_text)
            st.sidebar.success(f"Extracted {len(custom_portfolio_data)} items from resume!")
        except Exception as e:
            st.sidebar.error(f"Error processing resume: {e}")

    submit_button = st.button("Submit")

    if submit_button and urls:
        for url in urls:
            st.divider()
            st.write(f"### Processing: {url}")
            try:
                loader = WebBaseLoader([url])
                data = clean_text(loader.load().pop().page_content)
                portfolio.load_portfolio(custom_portfolio_data)
                jobs = llm.extract_jobs(data)
                for job in jobs:
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links, tone_input)
                    st.code(email, language='markdown')
            except Exception as e:
                st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)


