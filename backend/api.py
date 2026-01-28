from flask import Flask, request, jsonify
import main

app = Flask(__name__)

@app.route("/task/list", methods=["GET"])
def getTasks():
	return jsonify(main.get_tasks()), 200

@app.route("/task/add", methods=["POST"])
def addTask():
	data = request.get_json()
	description = data.get("description")

	main.addTask(description)

	return "Added task succesfully", 201

@app.route("/task/remove", methods=["DELETE"])
def removeTask():
	data = request.get_json()
	priority = data.get("priority")	

	main.removeTask(priority)

	return "Removed task succesfully", 204

@app.route("/task/changePriority", methods=["PUT"])
def changePriority():
	data = request.get_json()
	priority = data.get("priority")
	direction = data.get("direction")

	main.changePriority(priority, direction)

	return "Changed priority sucesfully", 200