from flask import Flask, render_template, redirect, request
app = Flask (__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    ninja= "ninja"
    return render_template('show.html', ninja= ninja)

@app.route('/ninja/<color>')
def color(color):
    print color
    if color=="blue":
        return render_template('show.html', color=color)
    elif color=="orange":
        return render_template('show.html', color=color)
    elif color=="red":
        return render_template('show.html', color=color)
    elif color=="purple":
        return render_template('show.html', color=color)
    else:
        color="notapril"
    return render_template('show.html', color=color)








app.run(debug=True)
