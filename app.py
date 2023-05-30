from flask import Flask, request, jsonify, render_template
import pickle

# Load the model and TfidfVectorizer object from disk
filename = 'tags_classifier.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('tfidf_vectorizer.pkl','rb'))
binarizer = pickle.load(open('multilabel_binarizer.pkl', "rb"))

app = Flask(__name__)

# load the saved model
#model = joblib.load('path/to/your/model.pkl')

# define the route for rendering the form
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

# define the route for handling text input
@app.route('/predict', methods=['POST'])
def predict():
    # get the text input from the user
    title = request.form["title"]
    body = request.form["body"]
    data = title + " " + body
     
    data = data.lower() 
    # make predictions on the input
    
    vect = cv.transform([data])
    #my_prediction = classifier.predict(vect)
    predictions = classifier.predict(vect)
    tags = binarizer.inverse_transform(predictions)

    # pass the predictions to the HTML template
    return render_template('home.html', predictions=tags[0])

app.run(host='0.0.0.0', port=5000, debug=False)
