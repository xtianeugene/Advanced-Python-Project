from flask import Flask, render_template_string
app = Flask(__name__)

HTML = """
<h1>Eugene Wanzala<h1>
<p>Python developer in progress.</p>
<h2>Projects</h2>
<ul>
    <li>University Registration Form</li>
    <li>Weather App</li>
    <li>Blockchain Demo</li>
<ul>
"""

@app.route("/")
def home(): return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)