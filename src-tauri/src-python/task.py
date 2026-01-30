import random
import json
import os

class Task:
	def __init__(self, priority, description, date):
		self.priority = priority
		self.description = description
		self.date = date

# Check if any data has been added to the task JSON
def isEmptyJSON(jsonFile):
	if not os.path.exists(jsonFile):
		with open(jsonFile, "w") as jsonFile:
			jsonFile.close()
		return True

	if os.path.getsize(jsonFile) > 0:
		return False
	
	return True

# Gets tasks from a JSON and puts them into an array
def getTasks(taskFile):
	if isEmptyJSON(taskFile):
		return []
	
	tasks = []
	with open(taskFile, "r") as json_file:
		data = json.load(json_file)
		for task in data:
			tasks.append(Task(task['priority'], task['description'], task['date']))
	return tasks

def saveTasks(taskList, taskFile):
	saveList = []
	for item in taskList:
		saveList.append({
			'priority': item.priority,
			'description': item.description,
			'date': item.date
		})

	with open(taskFile, 'w') as outfile:
		json.dump(saveList, outfile)

# Check if sort task array worked
def sortTasksCheck(sortedArray):
	if sortedArray[0].priority != 1:
		return False

	currentValue = 1
	for item in sortedArray:
		if item.priority == currentValue + 1:
			currentValue += 1
		else:
			return False

	return True

# Sort task array
def sortTasks(taskList):
	sorted = False

	sortedArray = []

	while not sorted:
		pivot = taskList.index(random.choice(taskList))
		pivotVal = taskList[pivot].priority

		lesserArray = []
		greaterArray = []

		for item in taskList:
			if item == taskList[pivot]:
				continue
			
			if item.priority < pivotVal:
				lesserArray.append(item)
			else:
				greaterArray.append(item)

		sortedArray = lesserArray + [taskList[pivot]] + greaterArray

		if sortTasksCheck(sortedArray):
			return sortedArray