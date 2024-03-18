# LLama2 Blog Generation

This project is a Streamlit application for generating blog content using the LLama-2 language model.

## Prerequisites

Before running this application, you need to download the LLama-2 model from the Hugging Face Model Hub. The model file `llama-2-7b-chat.ggmlv3.q8_0.bin` (7.16 GB) can be obtained from the following link:

[Download LLama-2 Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)


## Setup
To run this chatbot, you'll need to have Python installed on your machine. Follow these steps to set up the environment:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/DJagad/Blog_Generation_Using_Llama2.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Blog_Generation_Using_Llama2
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Add your model at getLammaResponse(input_text, no_words, blog_style): function:

    ```bash
    llm = CTransformers(model='__Add_Your_Complete_Model_path_here__,
                        model_type = 'llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})
    ```

5. Run the following command to start the Streamlit app:

```bash
streamlit run app.py
```

## Functionality
1. **Input Topic and Parameters:** Enter the blog topic, select the writing style, and specify the number of words for the blog content.
2. **Generate Blog:** Click on the "Generate" button to generate the blog content.

## Usage
1. Enter the blog topic in the provided text input.
2. Select the writing style from the dropdown menu.
3. Specify the number of words for the blog content.
4. Click on the "Generate" button to generate the blog content.

## Technologies Used
- Streamlit: For building interactive web applications.
- Langchain: For generating blog content using the LLama-2 language model.

# Technologies Used
- Streamlit: For building interactive web applications.
- Langchain: For generating blog content using the LLama-2 language model.