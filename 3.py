def countIdenticalStrings(list_of_string):
    string_counts = {}

    for string in list_of_string:
        if string in string_counts:
            string_counts[string] += 1
        else:
            string_counts[string] = 1

    for count in string_counts.values():
        print(count, end=' ')

print("Введите список строк: ")
a = input()
a_strings = a.replace("[", "").replace("]", "").replace("'", "").split(', ')

print("Количество повторений строк: ")
countIdenticalStrings(a_strings)