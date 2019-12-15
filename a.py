from flask import Flask, jsonify,request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # oject gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

    print("Sentence Overall Rated As", end=" ")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        return "Positive"
        #print("Positive")

    elif sentiment_dict['compound'] <= - 0.05:
        return "Negative"
        #print("Negative")

    else:
        return "Neutral"
        #print("Neutral")

    # Driver code

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
       print("q")
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<string:task_id>', methods=['GET'])
def get_Sentiment(task_id):
    print(sentiment_scores(task_id))
    return jsonify({'task': sentiment_scores(task_id)})

@app.route('/todo/api/v1.0/task', methods=['GET'])
def get_task1():
    arg1=request.args['a']
    return jsonify({'task': arg1})

if __name__ == '__main__':
    app.run(debug=True)