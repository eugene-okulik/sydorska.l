import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('file', help='File or folder path')
parser.add_argument('-d', '--date', help='Date for search')
parser.add_argument('--text', help='Text to search for', required=True)
args = parser.parse_args()

file_path = args.file
search_text = args.text.upper()
files_to_process = []

if os.path.exists(file_path):
    if os.path.isfile(file_path):
        files_to_process = [file_path]
    else:
        for f in os.listdir(file_path):
            full_path = os.path.join(file_path, f)
            if os.path.isfile(full_path):
                files_to_process.append(full_path)
else:
    print("Entered path does not exist.")
    exit(1)

for file in files_to_process:
    with open(file, 'r', encoding='utf8') as new_file:
        name_of_file = os.path.basename(file)
        current_block = []
        current_time = None

        for line in new_file:
            line = line.rstrip('\n')
            if line and line[0].isdigit():
                if current_block:
                    for block_line in current_block:
                        words = block_line.split()
                        for i in range(len(words)):
                            if search_text in words[i].upper():
                                start = max(0, i - 5)
                                end = min(len(words), i + 6)
                                snippet = words[start:end]
                                print(name_of_file, current_time, ' '.join(snippet))
                                break
                current_time = line[0:22]
                current_block = [line]
            else:
                current_block.append(line)

        if current_block:
            for block_line in current_block:
                words = block_line.split()
                for i in range(len(words)):
                    if search_text in words[i].upper():
                        start = max(0, i - 5)
                        end = min(len(words), i + 6)
                        snippet = words[start:end]
                        print(name_of_file, current_time, ' '.join(snippet))
                        break
