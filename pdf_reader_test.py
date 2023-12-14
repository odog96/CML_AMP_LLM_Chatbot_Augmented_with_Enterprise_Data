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
  
  
  