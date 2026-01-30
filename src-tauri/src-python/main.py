import task
import json
import datetime
import os

_tauri_plugin_functions = ["getTasks", "addTask", "removeTask", "changePriority"]

def loadTaskFile(path):
	if not os.path.exists(path):
		return "Need an actual path"
	currentTasks = task.getTasks(path)

#Move safePath into task.py
def transferPath():
	global savePath
	savePath = path

# Convert tasks to JSON for the frontend
def getTasks():
	global currentTasks

	taskArray = []
	for item in currentTasks:
		taskArray.append({
			"priority": item.priority,
			"description": item.description,
			"date": item.date
		})

	jsonTasks = json.dumps(taskArray)
	return jsonTasks

# Add new task
def addTask(description):
	global currentTasks

	priority = len(currentTasks) + 1
	newTask = task.Task(priority, description, datetime.datetime.now())
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