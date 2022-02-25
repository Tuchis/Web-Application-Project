"""
MODULE DOCSTRING
"""
import os

files = os.listdir("data/text")
files.sort()
num_groups = 0
files_grouped = []
elem_number = 0
for elem in files:
    if int(elem[-7:-4]) - 1 != elem_number or elem_number == 0:
        files_grouped.append([])
        num_groups += 1
        files_grouped[num_groups - 1].append(elem)
    else:
        files_grouped[num_groups - 1].append(elem)
    elem_number = int(elem[-7:-4])


for elem_index in range(len(files_grouped)):
    with open(f"text{elem_index + 1}.txt", "w") as file:
        for text_file in files_grouped[elem_index]:
            with open(f"data/text/{text_file}", "r") as text:
                for line in text:
                    if line == "\n" or line == " \n":
                        continue
                    file.write(line)
