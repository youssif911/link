from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template with a message that shows when the page is visited
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Visit</title>
</head>
<body>
    <h1>Welcome!</h1>

    <p style="color:green">Someone visited this page!</p>
</body>
</html>
"""

# Route for the main page
@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True)
