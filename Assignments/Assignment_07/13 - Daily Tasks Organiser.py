from xml.etree import ElementTree as et


path = "Assignments\\Assignment_07\\Example file (13)\\tasks.xml"
tree = et.parse(path)
root = tree.getroot()
items = ["Title", "DueDate", "Priority", "Status"]

while True:
    status = input("Enter the category of tasks you want to view (all, completed, pending): ")
    if status in ["all", "completed", "pending"]:
        break

if status == "all":
    print(root.tag + ":\n")
    tasks = root.findall("Task")
    for number in range(len(tasks)):
        print(f"task #{number + 1}:\n")
        task = tasks[number]
        for item in items:
            print(f"{item}: {task.find(item).text}")
        print(10 * "-")
        
elif status == "completed":
    print(root.tag + ":\n")
    tasks = root.findall("Task")
    tasks = [task for task in tasks if task.find("Status").text == "Completed"]
    if len(tasks) != 0:
        for number in range(len(tasks)):
            print(f"task #{number + 1}:\n")
            task = tasks[number]
            for item in items:
                print(f"{item}: {task.find(item).text}")
            print(10 * "-")
    else:
        print("No tasks available.")

elif status == "pending":
    print(root.tag + ":\n")
    tasks = root.findall("Task")
    tasks = [task for task in tasks if task.find("Status").text == "Pending"]
    if len(tasks) != 0:
        for number in range(len(tasks)):
            print(f"task #{number + 1}:\n")
            task = tasks[number]
            for item in items:
                print(f"{item}: {task.find(item).text}")
            print(10 * "-")
    else:
        print("No tasks available.")
