import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get the Response from the LLama2 Model

def getLammaResponse(input_text, no_words, blog_style):

    ## Calling the LLama-2-Models
    llm = CTransformers(model='/Users/spartan/Desktop/Projects/Blog_Generation_using_LLama2_LLM_App/models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = 'llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})
    
    ## Prompt Template

    template = """
    Write a blog for {blog_style} job profile for a topic {input_text} 
    within {no_words} words.

    """

    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                            template = template)
    
    ## Generate the response from the LLama2 model
    response=llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response




st.set_page_config(page_title = "Generate Blogs",
                   page_icon= "🤖",
                   layout = "centered",
                   initial_sidebar_state="collapsed")

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

## Creating two more column for 2 additional fields

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No. of Words')
with col2:
    blog_style = st.selectbox("Writing the Blog for", ('Researchers','Data Scientist',"Common People"), index=0)


submit=st.button("Generate")

## Final Response
if submit:
    st.write(getLammaResponse(input_text, no_words, blog_style))