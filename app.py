import streamlit as st
from key import google_gemini_api_key 
import google.generativeai as genai
genai.configure(api_key=google_gemini_api_key)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

st.set_page_config(layout='wide')

st.title('✍️ Blog It')

st.subheader('Craft your own blogs with help of AI')


with st.sidebar:
    st.title('Input your blog details')
    st.title('Enter details of the blog you want to generate')

    blog_title = st.text_input('Blog title')

    keywords = st.text_area('Keywords (comma-seperated)')

    num_words = st.slider('Number of Words',min_value=250,max_value=1000,step=250)

    num_images = st.number_input('Number of images',min_value=1,max_value=5,step=1) 
    prompt_parts = [
        f"Generate a comprehensive, engaging blog post relevant to the given titl \"{blog_title}\" and keywords \"{keywords}\" in the blog post. It should be \"{num_words}\" words long."
    ]

    response = model.generate_content(prompt_parts)
    submit_button = st.button('Generate Blog')

if submit_button:
        st.write(response.text)