"""
MODULE DOCSTRING
"""
import string
import json


def main():
    """
    MAIN FUNCTION
    """
    skip = True
    dictionary = dict()
    output = []
    print(dictionary)
    with open("text1.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line[2] == "." and line[0].isdigit():
                dekanat = line.split()[1]
                dictionary["деканат"] = dekanat
            elif line.startswith("("):
                protopresviterat = line.split()[0][1:]
                dictionary["протопресвітерат"] = protopresviterat
            elif line[0].isdigit():
                try:
                    output.append(local_dictionary)
                except:
                    pass
                skip = False
                local_dictionary = dict()
                local_dictionary["деканат"] = dekanat
                local_dictionary["протопресвітерат"] = protopresviterat
                spliter = list(line.split(","))
                city_name = spliter[0].split()[1]
                city_location = [50, 100]
                local_dictionary["населений пункт"] = {"назва": city_name,
                "location": {"lat": city_location[0], "lng": city_location[1]}}
                churches = dict()
                # churches_list =
                for elem in spliter[1:]:
                    if elem.strip().startswith("ц"):
                        churches["назва"] = " ".join(elem.strip().split()[1:])
                    else:
                        element = elem.split()
                        if len(element) == 1 and element[0][:-1].isdigit():
                            churches["рік"] = element[0][:-1]
                        elif (len(element) == 1 and element[0][
                                                   :-1] == "»Дн.«") or (len(
                            element) == 1 and element[0][:-1] == "»Дн«"):
                            churches["»Дн.«"] = "»Дн.«"
                        else:
                            churches[elem.split()[0]] = " ".join(
                                elem.split()[1:])
                local_dictionary["церкви"] = [churches]
            elif skip:
                pass
            else:
                key, value = line.split(":")[0], "".join(line.split(":")[1:])
                value_values = value.split(",")
                value_dictionary = dict()
                for elements in value_values:
                    try:
                        element_key = elements.strip().split()[0]
                        element_value = dict()
                        if element_key == "п." or element_key == "сін." or element_key == "гор.":
                            area = elements.strip().split()[1:]

                            for area_index in range(len(area) // 2):
                                element_value[area[area_index * 2 + 1]] = area[area_index * 2]
                        else:
                            element_key = elements.strip().split()[0]
                            element_value = "".join(elements.strip().split()[1:])


                    except:
                        element_key, element_value = "".join(elements.strip().split())  , "YES"
                    value_dictionary[element_key] = element_value
                local_dictionary[key] = value_dictionary
                print(key, value)
                # print(churches)
                # print(city_name)
                # print(spliter)
            with open("file.json", "w") as filer:
                json.dump(output, filer, indent=4, ensure_ascii = False)
            print(dictionary)


if __name__ == "__main__":
    main()
