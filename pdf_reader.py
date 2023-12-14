import os
import re
import shutil
#import tkinter as tk
#rom tkinter import messagebox
from pdfminer.high_level import extract_text

# Configuration and path settings
staged_folder = 'staged_files'
completed_folder = 'staged_files_completed'
output_folder_txt = 'output_text_files'
output_folder_data = 'data'
old_data_folder = 'old_data'

def extract_text_from_pdfs(stage_folder, completed_folder):
    for pdf_file in os.listdir(stage_folder):
        if pdf_file.endswith(".pdf"):
            output_file_name = os.path.splitext(pdf_file)[0] + ".txt"
            output_path = os.path.join(staged_folder, output_file_name)  # Save in the same folder
            pdf_path = os.path.join(stage_folder, pdf_file)
            text = extract_text(pdf_path)

            # Add a space at the end of each line
            text = "\n".join([line.strip() + " " for line in text.splitlines()])

            with open(output_path, "w", encoding="utf-8") as out:
                out.write(text)
                print('writing:', output_file_name)
                print('length', len(text))
                
            if not os.path.exists(completed_folder):
                os.makedirs(completed_folder)
            shutil.move(pdf_path, os.path.join(completed_folder, pdf_file))


def process_text(text):
    text = text.encode('ascii', errors='ignore').decode('ascii')
    text = re.sub(r'[^A-Za-z0-9 .,?!]+', '', text)
    return text

def chunk_file_and_save(filename, doc_number):
    with open(filename, 'r') as f:
        content = f.read()

    content = process_text(content)
    word_list = content.split()
    start_idx = 0

    while start_idx < len(word_list):
        end_idx = start_idx + 500
        while end_idx < len(word_list) and word_list[end_idx][-1] not in ['.', '!', '?']:
            end_idx -= 1
        end_idx += 1

        chunk = ' '.join(word_list[start_idx:end_idx])
        with open(os.path.join(output_folder_data, f'doc_{doc_number}.txt'), 'w') as output_file:
            output_file.write(chunk)
            print('writing',outputfile)

        start_idx = end_idx
        doc_number += 1
        print(doc_number)
    return doc_number

def delete_old_data():
  for filename in os.listdir(old_data_folder):
    file_path = os.path.join(old_data_folder, filename)

    if os.path.isfile(file_path):
      os.remove(file_path)  # Remove the file
    elif os.path.isdir(file_path):
      shutil.rmtree(file_path)  # Remove the directory and all its contentscontents

if __name__ == '__main__':
    if not os.path.exists(completed_folder):
        print("Trying to create:", completed_folder)
        os.makedirs(completed_folder)
    extract_text_from_pdfs(staged_folder, completed_folder)

    for dir_name in [output_folder_data, old_data_folder]:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    if os.listdir(old_data_folder):
        delete_old_data()

    if os.listdir(output_folder_data):
        for filename in os.listdir(output_folder_data):
            dst_path = os.path.join(old_data_folder, filename)
            if os.path.exists(dst_path):
                os.remove(dst_path)
            shutil.move(os.path.join(output_folder_data, filename), dst_path)

    if not os.path.exists(staged_folder):
        raise FileNotFoundError("The 'staged_files' directory does not exist.")

    txt_files = [f for f in os.listdir(staged_folder) if f.endswith('.txt')]

    if not txt_files:
        raise FileNotFoundError("No .txt files found in the 'staged_files' directory.")

    doc_num = 1
    for file in txt_files:
        print(file)  
        doc_num = chunk_file_and_save(os.path.join(staged_folder, file), doc_num)
        os.remove(os.path.join(staged_folder, file))