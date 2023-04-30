import sys
import re
import logging
from transformers import AutoTokenizer
from flask import Flask, render_template, request

app = Flask(__name__)

# Count tokens in a file using a specified language model.
def count_tokens(file_path, model_name='gpt4'):
    try:
        # Read the file content.
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Initialize the tokenizer for the specified model.
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Tokenize the content using the tokenizer.
        tokens = tokenizer.tokenize(content)
        
        # Count the number of tokens.
        token_count = len(tokens)
        
        # Log the token count.
        logging.info(f'Token count for {file_path}: {token_count}')
        
        return token_count
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
        print(f'Error: File not found - {file_path}')
    except Exception as e:
        logging.error(f'Error processing file: {file_path} - {str(e)}')
        print(f'Error processing file: {file_path} - {str(e)}')

# Count tokens in a text string using a specified language model.
def count_tokens_text(text, model_name='gpt4'):
    try:
        # Initialize the tokenizer for the specified model.
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Tokenize the text using the tokenizer.
        tokens = tokenizer.tokenize(text)
        
        # Count the number of tokens.
        token_count = len(tokens)
        
        return token_count
    except ValueError as ve:
        error_message = f"Invalid model name: {model_name}."
        return None, error_message
    except OSError as oe:
        error_message = f"Model not found: {model_name}."
        return None, error_message
    except Exception as e:
        error_message = f"Error processing text: {str(e)}"
        return None, error_message

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the text and model name from the form.
        text = request.form['text']
        model_name = request.form['model_name']
        
        # Count tokens in the text using the specified model.
        token_count, error = count_tokens_text(text, model_name)
        
        # Render the results.
        return render_template('index.html', text=text, token_count=token_count, error=error)
    else:
        # Render the initial form.
        return render_template('index.html')

if __name__ == "__main__":
    # Set the file path for testing purposes.
    file_path = r'C:\your\file\path\here\NLP_intro.md'

    # Configure the logging.
    logging.basicConfig(filename='token_counter.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Count tokens in the file.
    token_count = count_tokens(file_path)

    if token_count is not None:
        print(f'The number of tokens in the file is: {token_count}')

    # Run the Flask app.
    app.run(debug=True)

