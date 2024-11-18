from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # Ensure both files are uploaded
    if 'data_file' not in request.files or 'json_file' not in request.files:
        return "No file part", 400

    data_file = request.files['data_file']
    json_file = request.files['json_file']

    # Read the CSV file (if you need to display it)
    data_df = pd.read_csv(data_file)

    # Read JSON file and format data
    json_data = json.load(json_file)
    anomalies = [{"datetime": item["filename"], "value": item["value"],
                  "is_anomaly": item["Anomaly"]} for item in json_data]

    return render_template('display.html', anomalies=anomalies, data=data_df.to_html(classes='csv-table'))


if __name__ == "__main__":
    app.run(debug=True)
