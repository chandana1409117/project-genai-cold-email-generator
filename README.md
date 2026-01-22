# 📧 Cold Mail Generator

Cold email generator for services companies using Groq, LangChain, and Streamlit. It allows users to input the URL of a company's careers page. The tool then extracts job listings from that page and generates personalized cold emails. These emails include relevant portfolio links sourced from a vector database or a dynamically uploaded resume.

**Imagine a scenario:**
- Nike needs a Principal Software Engineer and is spending time and resources in the hiring process, onboarding, training, etc.
- AtliQ is a Software Development company that can provide a dedicated software development engineer to Nike. So, the business development executive (Mohan) from AtliQ is going to reach out to Nike via a cold email.

![img.png](imgs/img.png)

## New Features 🚀

### 1. Customizable Tone
Select the tone of your cold email to match your target audience. Options include:
- **Formal**: Professional and respectful.
- **Casual**: Relaxed and friendly.
- **Persuasive**: Focused on selling the value proposition.
- **Standard**: Balanced and direct.

### 2. Multiple Job Support
Process multiple job postings at once!
- **Single URL**: Paste a single job URL.
- **Upload CSV**: Upload a CSV file with a `url` column containing a list of job links. The app will generate emails for each one sequentially.

### 3. Resume/Portfolio Upload
Dynamically match your skills to the job!
- **Upload PDF**: Upload your resume or portfolio PDF in the sidebar.
- **AI Extraction**: The app parses your projects and tech stack to create a custom portfolio for the session, ensuring the generated emails reference your actual relevant experience.

## Architecture Diagram
![img.png](imgs/architecture.png)

## Set-up

1.  **Get an API Key**:
    Get an API_KEY from [Groq Console](https://console.groq.com/keys). Inside `app/.env.example` (rename to `.env`), update the value of `GROQ_API_KEY` with the API_KEY you created.

2.  **Install Dependencies**:
    ```commandline
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit App**:
    ```commandline
    streamlit run app/main.py
    ```

## Usage
1.  **Select Input Type**: Choose between "Single URL" or "Upload CSV".
2.  **Portfolio (Optional)**: Upload your PDF resume in the sidebar to use your own projects.
3.  **Tone**: Select your desired email tone.
4.  **Submit**: Click "Submit" to generate your cold emails!

## Copyright
Copyright (C) Codebasics Inc. All rights reserved.

**Additional Terms:**
This software is licensed under the MIT License. However, commercial use of this software is strictly prohibited without prior written permission from the author. Attribution must be given in all copies or substantial portions of the software.
