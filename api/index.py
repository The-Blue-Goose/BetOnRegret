from flask import Flask, render_template, request
import random

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    return render_template("index.html", title="Home - Bet on Regret")

@app.route("/roulette", methods=["GET", "POST"])
def roulette():
    if request.method == "POST":
        trials = int(request.form["trials"])
        bet_type = request.form["bet"]
        
        if trials > 10000:
            return render_template("error.html", message="Please enter a number of trials less than or equal to 10,000.")

        wins = 0
        for _ in range(trials):
            outcome = random.randint(0, 37)  # 0–36 roulette wheel + 37 as 00
            if bet_type == "red":
                if outcome in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
                    wins += 1
            elif bet_type == "black":
                if outcome in [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]:
                    wins += 1
            elif bet_type == "single_number":
                if outcome == 17:  # assuming betting on 17
                    wins += 1

        payout = 0
        if bet_type == "red" or bet_type == "black":
            payout = wins * 2
        elif bet_type == "single_number":
            payout = wins * 36

        result = {
            "trials": trials,
            "wins": wins,
            "losses": trials - wins,
            "net": payout - trials
        }

        return render_template("results.html", result=result, game="Roulette")

    return render_template("roulette.html", title="Roulette - Bet on Regret")

@app.route("/craps", methods=["GET", "POST"])
def craps():
    if request.method == "POST":
        trials = int(request.form["trials"])

        if trials > 10000:
            return render_template("error.html", message="Please enter a number of trials less than or equal to 10,000.")
        
        wins = 0
        losses = 0

        for _ in range(trials):
            roll1 = random.randint(1, 6) + random.randint(1, 6)
            if roll1 in [7, 11]:
                wins += 1
            elif roll1 in [2, 3, 12]:
                losses += 1
            else:
                point = roll1
                while True:
                    roll2 = random.randint(1, 6) + random.randint(1, 6)
                    if roll2 == point:
                        wins += 1
                        break
                    elif roll2 == 7:
                        losses += 1
                        break

        payout = wins * 2
        result = {
            "trials": trials,
            "wins": wins,
            "losses": losses,
            "net": payout - trials
        }

        return render_template("results.html", result=result, game="Craps")


    return render_template("craps.html", title=" - Bet on Regret")

@app.route('/memes')
def memes():
    return render_template('memes.html', title='Memes - Bet on Regret')

@app.route('/videos')
def videos():
    return render_template('videos.html', title='Videos - Bet on Regret')

@app.route("/about")
def about():
    return render_template("about.html", title="About - Bet on Regret")

# Export the app for Vercel to detect
app = Flask(__name__, template_folder="../templates", static_folder="../static")

if __name__ == "__main__":
    app.run(debug=True)
