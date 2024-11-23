# app.py

from flask import Flask, render_template, request
from scraper import extract_contact_info  # Import the function from scraper.py

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        contact_info = extract_contact_info(url)  # Call the scraping function
        return render_template("index.html", contact_info=contact_info)
    return render_template("index.html", contact_info=None)

if __name__ == "__main__":
    app.run(debug=True)
