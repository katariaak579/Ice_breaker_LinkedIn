from flask import Flask, render_template, request, jsonify
from ice_breaker import ice_break as ice_break_with

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary_and_facts, profile_pic_url = ice_break_with(
        name=name
    )
    return jsonify(
        {
            "summary": summary_and_facts.summary,
            "facts": summary_and_facts.facts,
            "topics_of_interest": summary_and_facts.topic_of_interest,
            "ice_breakers": summary_and_facts.ice_breakers,
            "picture_url": profile_pic_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)