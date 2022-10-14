import re


def clean_string(string):
    dirty_chars = ['<', '>', ':', '"', '|', '?', '*']

    for i in dirty_chars:
        string = string.replace(i, '')

    cleaned_string = re.sub(r"/{2,}", "/", string)

    return cleaned_string
