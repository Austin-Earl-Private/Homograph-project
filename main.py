import os
from pathlib import Path
import re

def generate_path_list_from_string(string):

    return Path(string).parts


def generate_file_flow_list(unprocessed_file_folder_list):
    processed_list = []
    for element in unprocessed_file_folder_list:
        if element != "..":
            processed_list.append(element)
        else:
            if len(processed_list) > 0:
                processed_list.pop()

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
    # ziped = zip(string1_processed, string2_processed)
    #
    # for element in ziped:
    #     # Evaluate
    #     print(element)
    #     if element[0] != element[1]:
    #         return False
    #
    # return True


def run_test(cwd, string1, string2):
    # uri = "a/../.././././test/test.txt"
    #
    # uri1 = "/home/cs453/week05/test.txt"
    # uri2 = "/home/cs453/week05/../../cs453/week05/test.txt"
    # uri3 = "/home/cs453/week05/../week05/../week05/../week05/test.txt"
    # uri4 = "/home/cs453/week05/../../../../../../../home/cs453/week05/test.txt"

    # print(generate_path_list_from_string(uri4))
    # print(generate_file_flow_list(generate_path_list_from_string(uri1)))
    # print(generate_file_flow_list(generate_path_list_from_string(uri2)))
    # print(generate_file_flow_list(generate_path_list_from_string(uri3)))
    # print(generate_file_flow_list(generate_path_list_from_string(uri4)))

    print(test_homograph(cwd+string1, cwd+string2))


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
