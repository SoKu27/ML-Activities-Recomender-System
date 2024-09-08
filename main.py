from flask import Flask, render_template, session, request
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import random 

activities_data = pd.read_csv('activitiesData.csv')

X = activities_data[['Age', 'Gender', 'nightorday']]
y = activities_data.drop(columns=['Age', 'Gender', 'nightorday'])

model = DecisionTreeClassifier()
model.fit(X, y)

app = Flask(__name__)

@app.route('/')
def main():
  return render_template("index.html")

@app.route('/results', methods=['GET', 'POST'])
def index():

    age = int(request.form['age'])
    gender = int(request.form['gender'])
    if(gender == 1):
      genderreturn = "men"
    else: 
      genderreturn = "women"
    nightorday = int(request.form['nightorday'])
    if(nightorday == 1):
      nightordayreturn = "daytime☀️"
    else: 
      nightordayreturn = "nighttime🌑"
    


    prediction_input = pd.DataFrame([[age, gender, nightorday]], columns=['Age', 'Gender', 'nightorday'])
    predictions = model.predict(prediction_input)
    activities_list = [
      "Learn to play a new musical instrument",
      "Take a beginner's coding class",
      "Start a vegetable garden",
      "Learn a new language",
      "Volunteer at a local animal shelter",
      "Take a dance class",
      "Start a blog or vlog",
      "Learn to knit or crochet",
      "Try a new cuisine",
      "Take a photography class",
      "Go on a solo camping trip",
      "Learn to paint or draw",
      "Start a book club",
      "Take a pottery class",
      "Learn to play a board game",
      "Start a home garden",
      "Learn to play a card game",
      "Take a calligraphy class",
      "Learn to bake bread",
      "Take a DIY home improvement class"
    ]
    print(predictions)

    filtered_activities = [activity for i, activity in enumerate(activities_list) if predictions[0][i] != 0]
    print(filtered_activities)
    x = len(filtered_activities)
    random.shuffle(filtered_activities)
    match_list = []
    for i in range(x):
      if(i == 1):
        match_list.append(random.randint(90, 100))
      if(i == 2):
        match_list.append(random.randint(80, 90))
      if(i == 3):
        match_list.append(random.randint(70, 80))
      if(i == 4):
        match_list.append(random.randint(60, 70))
      if(i == 5):
        match_list.append(random.randint(50, 60))
      if(i == 6):
        match_list.append(random.randint(40, 50))
      if(i == 7):
        match_list.append(random.randint(35, 45))
      if(i == 8):
        match_list.append(random.randint(30, 40))
      if(i == 9):
        match_list.append(random.randint(25, 35))
      if(i == 10):
        match_list.append(random.randint(20, 30))
      if(i == 11):
        match_list.append(random.randint(15, 25))
      if(i == 12):
        match_list.append(random.randint(10, 20))
    print(match_list)
    combined = zip(filtered_activities, match_list)


    return render_template("results.html", info = {
      "age": age,
      "gender": genderreturn,
      "nightorday": nightordayreturn,
      "combined": combined,
      "matches": match_list
    })

if __name__== "__main__":
  app.run(debug=True)