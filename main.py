from flask import Flask
from flask import render_template, request
import requests
global API_URL
global headers
global response


# bkp
def query(text):
  payload = {"inputs": text}
  API_URL = "https://api-inference.huggingface.co/models/Ashish9879/aic_shakespeare"
  headers = {"Authorization": "Bearer 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"}
  response = requests.post(API_URL, headers=headers, json=payload)
  try:
    q = eval(
      str(response.content)[3:-2].replace("\\n",
                                          " ").replace("\\",
                                                       " "))["generated_text"]
    print(q)
  except Exception as e:
    q = e
    q = "I am sorry our creative expert is busy due to traffic, Please try again after some time. Thank you!"
  return q


app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/model')
def model():
  return render_template('model.html')


@app.route('/learn')
def learn():
  return render_template('learnmore.html')


@app.route('/graph')
def graph():
  return render_template('plot.html')


# bkp
@app.route('/model', methods=['POST'])
def process_form():
  # Get the prompt from the form data
  global prompt
  prompt = request.form['prompt']  # prompt is requesting from this form
  prompt
  # Process the prompt and return the result
  result = process_prompt(prompt)
  return result


def process_prompt(prompt):

  processed_prompt = query(prompt)

  return render_template('model.html', processed_prompt=processed_prompt)


app.run(host='0.0.0.0', port=81)
if __name__ == '__main__':
  app.debug = True
  app.run()
