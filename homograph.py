import os
import re


def generate_path_list_from_string(string):
    # This function worked as follows
    # string passed into function as the following format {letter}:{ folder or file }{ // or \ }{ folder or file }
    # Remove drive and append to list
    # split on // or \
    # if spliting element is empty string, ignore it
    # add to list and return
    parts = []
    directory_list = re.split('(\\w:)', string)
    parts.append(directory_list[1])
    files = re.split(r'\\|/', directory_list[2])
    for ele in files:
        if ele != "":
            parts.append(ele)
    return parts


def canonize_file_list(unprocessed_file_folder_list):
    # process file path list as a stack
    # folders append
    # back path ".." pops stack
    # by the end you should get the conical version of the path
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
    # canonize list
    # if they are not same length, they are not homographs
    # parse over list and check element by index to see if matches in other pair
    # return False if not same, return True if they are same
    string1_processed = canonize_file_list(generate_path_list_from_string(string1))
    string2_processed = canonize_file_list(generate_path_list_from_string(string2))

    if len(string1_processed) != len(string2_processed):
        return False

    for index, element in enumerate(string1_processed):
        if element != string2_processed[index]:
            return False

    return True


def run_test(cwd, string1, string2):
    if (test_homograph(cwd + string1, cwd + string2)):
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
