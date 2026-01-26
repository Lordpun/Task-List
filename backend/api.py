from flask import Flask, jsonify
import main

app = Flask(__name__)

@app.route("/task/list", methods=["GET"])
def getTasks():
	return jsonify(main.get_tasks())

@app.route("/task/add/<description>", methods=["POST"])
def addTask(description):
	pass

@app.route("/task/remove/<priority>", methods=["DELETE"])
def removeTask(priority):
	pass

@app.route("/task/changePriority/up/<priority>", methods=["PUT"])
def changePriorityUp(priority):
	pass

@app.route("/task/changePriority/down/<priority>", methods=["PUT"])
def changePriorityDown(priority):
	pass