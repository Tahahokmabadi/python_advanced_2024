text_path = input("Enter the absolute pr relative path of your text file: ")

word = input("What word would you like to search for in the text: ")

text_file = open(text_path, "r")
text_data = text_file.read()

count_of_words = len(text_data.split())
count_of_lines = len(text_file.readlines())
text_file.close()

word_count = text_data.count(word)

report_path = "report.txt"
report_file = open(report_path, "w")
report_file.write(f"Total words: {count_of_words}\n")
report_file.write(f"Total line: {count_of_lines}\n")
report_file.write(f'Occurrences of "{word}": {word_count}\n')
report_file.close()

report_file = open("report.txt", "r")
print("\nReport contents:")

report_data = report_file.read()
print(report_data)
report_file.close()