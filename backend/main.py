import task
import datetime

currentTasks = task.getTasks()

# Gets task list for the API
def getTasks():
	global currentTasks
	return currentTasks

# Add new task
def addTask(description):
	global currentTasks

	priority = len(currentTasks) + 1
	newTask = Task(description, priority, datetime.datetime.now())
	fixPriority(priority)

	currentTasks.append(newTask)
	currentTasks = task.sortTasks(currentTasks)

	# Append tasks to the JSON file
	task.saveTasks(currentTasks)

# Remove a task
def removeTask(priority):
	global currentTasks

	for item in currentTasks:
		if item.priority == priority:
			currentTasks.pop(item)
			return

# Account for priority change
def fixPriority(newPriority, changeDirection=True):
	global currentTasks

	for item in currentTasks:
		if item.priority <= newPriority and chageDirection:
			item.priority += 1
		elif item.priority >= newPriority and not changeDirection:
			item.priority -= 1

# Changes priority of a task
def changePriority(index, changeDirection):
	global currentTasks
	
	task = currentTasks[index]
	currentTasks.pop(index)

	if changeDirection:
		direction = 1
	else:
		direction = -1

	fixPriority(task.priority + direction, changeDirection)
	currentTasks.append(task)

	task.sortTasks(currentTasks)
	task.saveTasks(currentTasks)