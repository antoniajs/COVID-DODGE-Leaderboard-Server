from flask import Flask, render_template, request, jsonify
from replit import db
import leaderboard
import json
app = Flask('app')

# db["number1"] = "Player 1"
# db["score1"] = 0
# db["number2"] = "Player 2"
# db["score2"] = 0
# db["number3"] = "Player 3"
# db["score3"] = 0
# db["number4"] = "Player 4"
# db["score4"] = 0
# db["number5"] = "Player 5"
# db["score5"] = 0

@app.route("/leaderboard")
def display_leaderboard():
  number1 = db["number1"] + ": " + str(db["score1"])
  number2 = db["number2"] + ": " + str(db["score2"])
  number3 = db["number3"] + ": " + str(db["score3"])
  number4 = db["number4"] + ": " + str(db["score4"])
  number5 = db["number5"] + ": " + str(db["score5"])
  return render_template('leaderboard.html', number1=number1, number2=number2, number3=number3, number4=number4, number5=number5)
  
@app.route("/update_leaderboard", methods = ["POST"])
def new_score():
  data = json.loads(request.data)
  print(data)
  if "username" in data and "score" in data:
    username = data["username"]
    score = data["score"]
    print(username, score)
    leaderboard.update_leaderboard(username, score)
  return {"message":"Received!"}
    
  
app.run(host='0.0.0.0', port=81)
