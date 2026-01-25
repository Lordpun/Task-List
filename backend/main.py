import task

currentTasks = task.getTasks()

# Add new task
def addTask(description, priority):
	newTask = Task(description, priority)
	fixPriority(priority)

	currentTasks.append(newTask)
	currentTasks = task.sortTasks(currentTasks)

	# Append tasks to the JSON file
	task.saveTasks(currentTasks)

# Account for priority change
def fixPriority(newPriority):
	for item in currentTasks:
		if item.priority <= newPriority:
			item.priority += 1