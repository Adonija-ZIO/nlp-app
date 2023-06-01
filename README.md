# Tag Classifier API

This is a Flask API that uses a trained model to classify tags for text inputs. It provides a web interface for users to enter a title and body of a text and get predicted tags based on the input. In this first version of our project, we train the first 100 tags of our data collect by SQL request.


## Getting Started

These instructions will help you set up and run the API on your local machine.

### Prerequisites

- Python 3.7 or higher
- Flask framework
- Required libraries (specified in `requirements.txt`)

### Installation

1. Clone the repository:

        git clone https://github.com/Adonija-ZIO/nlp-app.git
        cd nlp-app

2. Create a virtual environment (optional but recommended):

        python3 -m venv env
        source env/bin/activate


3. Install the dependencies:

        pip install -r requirements.txt


## Usage

1. Start the API server:

        python app.py


2. Open your web browser and go to `http://localhost:5000` to access the home page.

3. Enter a title and body of text in the provided input fields.

4. Click the "Submit" button to make predictions.

5. The predicted tags will be displayed on the page.

## Customization

You can modify the code to fit your specific use case. Here are a few possible customizations:

- Update the HTML templates in the `templates` directory to change the appearance of the web interface.
- Modify the preprocessing steps or add additional text processing techniques.
- Train your own model and replace the existing model files (`tags_classifier.pkl`, `tfidf_vectorizer.pkl`, `multilabel_binarizer.pkl`) with your trained model files.
- Add authentication or access control mechanisms to protect the API endpoints.

## Deployment

This API can be deployed to various hosting platforms or cloud services. Some popular options include:

- Heroku
- AWS Elastic Beanstalk
- Google Cloud Platform
- Microsoft Azure

Please refer to the documentation of your chosen deployment platform for detailed instructions on how to deploy a Flask application.


## Acknowledgments

- The Flask framework: [Flask](https://flask.palletsprojects.com/)
- Python machine learning libraries: [scikit-learn](https://scikit-learn.org/), [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/)



