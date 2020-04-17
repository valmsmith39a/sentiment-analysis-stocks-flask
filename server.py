from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Monkeys throwing darts"

@app.route('/company-news-sentiment')
def company_news_sentiment():
	return "Tesla (TSLA) news sentiment is negative (2 positive, 8 negative)"

