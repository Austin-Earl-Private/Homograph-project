import re


def clean_string(string):
   #define invalid characters in windows set
    dirty_chars = ['<', '>', ":", '"', '|', '?', '*']

   #save drive letters, remove from string ot be cleaned
    tempString = string[0:2]
    string = string[2:]

   #clean string of invalid characters
    for i in dirty_chars:
        string = string.replace(i, '')

   #make sure that the correct number of slashes exist
    cleaned_string = re.sub(r"/{2,}", "/", string)
   
   #prepend drive letters back onto cleaned string
    cleaned_string = tempString + cleaned_string

   #return string
    return cleaned_string
