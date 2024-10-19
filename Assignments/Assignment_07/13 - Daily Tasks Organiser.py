from xml.etree import ElementTree as et


path = "Assignments\\Assignment_07\\Example file\\tasks.xml"
tree = et.parse(path)
root = tree.getroot()
print(root.tag + ":\n")

tasks = root.findall("Task")

items = ["Title", "DueDate", "Priority", "Status"]

for number in range(len(tasks)):
    print(f"task #{number + 1}:\n")
    task = tasks[number]
    for item in items:
        print(f"{item}: {task.find(item).text}")
    print(10 * "-")
