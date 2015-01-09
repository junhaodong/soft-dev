#!/usr/bin/python
from flask import Flask, render_template, request
import getResults

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results")
def results():
    question = request.args.get("question")
    #print question
    answer = getResults.search_query(question)
    return render_template("results.html", question=question,answer=answer)

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
    app.run()
