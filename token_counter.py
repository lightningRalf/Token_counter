import sys
import re
import logging


def count_tokens(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            content = re.sub(r'\!\[.*?\]\(.*?\)|\[(.*?)\]\(.*?\)|\#\#*\s|\`|\*|[\*_]{2,}|[-]{3,}|\d\.\s|\n', '', content)
            tokens = content.split()
            token_count = len(tokens)
            logging.info(f'Token count for {file_path}: {token_count}')
            return token_count
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
        print(f'Error: File not found - {file_path}')
    except Exception as e:
        logging.error(f'Error processing file: {file_path} - {str(e)}')
        print(f'Error processing file: {file_path} - {str(e)}')


if __name__ == "__main__":
    file_path = r'C:\your\file\path\here\NLP_intro.md'

    logging.basicConfig(filename='token_counter.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    token_count = count_tokens(file_path)

    if token_count is not None:
        print(f'The number of tokens in the file is: {token_count}')
