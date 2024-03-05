from flask import Flask,render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'San Francisco, CA',
        'salary': '$100,000'
    },
    {
        'id': 2,
        'title': 'Data Analyst',
        'location': 'New York, NY',
        'salary': '$80,000'
    },
    {
        'id': 3,
        'title': 'UX Designer',
        'location': 'Seattle, WA',
        'salary': '$90,000'
    },
    {
        'id': 4,
        'title': 'Marketing Specialist',
        'location': 'Chicago, IL',
        'salary': '$75,000'
    },
    {
        'id': 5,
        'title': 'Financial Analyst',
        'location': 'Los Angeles, CA',
        'salary': '$85,000'
    },
    {
        'id': 6,
        'title': 'Product Manager',
        'location': 'Austin, TX',
        'salary': '$110,000'
    },
    # Add more job items as needed
]

@app.route("/")
def hello_world():
    return render_template("Home.html",jobs=JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)