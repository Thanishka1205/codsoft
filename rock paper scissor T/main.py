from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    if 'user_score' not in session:
        session['user_score'] = 0
    if 'computer_score' not in session:
        session['computer_score'] = 0
    return render_template('index.html', user_score=session['user_score'], computer_score=session['computer_score'])

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = 'It\'s a tie!'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = 'You win!'
        session['user_score'] += 1
    else:
        result = 'Computer wins!'
        session['computer_score'] += 1

    return render_template('index.html', user_choice=user_choice, computer_choice=computer_choice, result=result, user_score=session['user_score'], computer_score=session['computer_score'])

@app.route('/reset')
def reset():
    session['user_score'] = 0
    session['computer_score'] = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)