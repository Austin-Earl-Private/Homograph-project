import os
from pathlib import Path
import re

def generate_path_list_from_string(string):
    parts = []
    directory_list = re.split('(\\w:)',string)
    parts.append(directory_list[1])
    files = re.split(r'\\|/',directory_list[2])
    for ele in files:
        if ele != "":
            parts.append(ele)
    return parts

def generate_file_flow_list(unprocessed_file_folder_list):
    processed_list = []
    for element in unprocessed_file_folder_list:
        if element == "..":
            if len(processed_list) > 1:
                processed_list.pop()
        elif element == '.':
            pass
        else:
            processed_list.append(element)

    return processed_list


def test_homograph(string1, string2):
    string1_processed = generate_file_flow_list(generate_path_list_from_string(string1))
    string2_processed = generate_file_flow_list(generate_path_list_from_string(string2))

    if len(string1_processed) != len(string2_processed):
        return False

    for index, element in enumerate(string1_processed):
        if element != string2_processed[index]:
            return False

    return True



def run_test(cwd, string1, string2):
    if(test_homograph(cwd+string1, cwd+string2)):
        print(f'"{string1}" and "{string2}" are homographs')
    else:
        print(f'"{string1}" and {string2} are not homographs')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cwd = os.getcwd()
    cwd += '\\'
    # print(cwd)
    file1 = input("First Filename: ")
    file2 = input("Second Filename: ")

    # test = re.sub(r"/{2,}","/",file2)
    # print(test)
    run_test(cwd, file1, file2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
