from flask import Flask, render_template, request, jsonify
from bot.services.calorie import UserData, plan as calorie_plan
from bot.services.program import generate

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/calories')
def api_calories():
    try:
        gender = request.args.get('gender', 'M')
        age = int(request.args['age'])
        height = float(request.args['height'])
        weight = float(request.args['weight'])
        activity = float(request.args.get('activity', 1.2))
    except (KeyError, ValueError):
        return jsonify({'error': 'invalid parameters'}), 400

    data = UserData(gender=gender, age=age, height=height, weight=weight, activity=activity)
    return jsonify(calorie_plan(data))


@app.route('/api/program')
def api_program():
    level = request.args.get('level', 'novice')
    gender = request.args.get('gender', 'M')
    return jsonify({'plan': generate(level, gender)})

@app.route('/programs')
def programs():
    return render_template('programs.html')

if __name__ == '__main__':
    app.run(debug=True)
