import task
import json
import datetime

_tauri_plugin_functions = ["getTasks", "addTask", "removeTask", "changePriority"]

currentTasks = task.getTasks()

# Gets task list for the API
def getTasks():
	global currentTasks

	jsonTasks = json.dumps(currentTasks)
	return jsonTasks

# Add new task
def addTask(description):
	global currentTasks

	priority = len(currentTasks) + 1
	newTask = task.Task(description, priority, datetime.datetime.now())
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
			currentTasks.pop(currentTasks.index(item))
			fixPriority(priority, False)

			task.saveTasks(currentTasks)
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
def changePriority(priority, changeDirection):
	global currentTasks
	
	for item in currentTasks:
		if item.priority == priority:
			chosenTask = item
			currentTasks.pop(currentTasks.index(item))

	if changeDirection:
		direction = 1
	else:
		direction = -1

	fixPriority(chosenTask.priority + direction, changeDirection)
	currentTasks.append(currentTasks.index(chosenTask))

	task.sortTasks(currentTasks)
	task.saveTasks(currentTasks)