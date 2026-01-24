import random

class Task:
	def __init__(self, description, priority, complete = False):
		self.description = description
		self.priority = priority
		self.complete = complete


# Gets tasks from a JSON and puts them into an array
def getTasks():
	tasks = []
	with open('tasks.json') as json_file:
		data = json.load(json_file)
		for task in data:
			tasks.append(Task(task['description'], task['priority'], task['complete']))
	return tasks

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