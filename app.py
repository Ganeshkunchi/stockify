import joblib
from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
app = Flask(__name__)
global X_train, X_test, y_train, y_test

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/prediction')
def prediction():  # put application's code here
        return render_template('prediction.html')

@app.route('/prediction1', methods=['POST', 'GET'])
def pred():
        a = []
        if request.method == "POST":
            b = request.form['b']
            c = request.form['c']
            p = request.form['p']
            a.extend([b, c, p])


            model = joblib.load('dumpy.pkl')

            y_pred = model.predict([a])
            #acc3 = accuracy_score(y_test, y_pred)
            return render_template('prediction.html', op=y_pred,msg1="done")
        return render_template('prediction.html', msg1="notdone")


if __name__ == '__main__':
     app.run(debug = True)