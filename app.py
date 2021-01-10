from flask import Flask, request, jsonify
import numpy as np
import traceback
import pandas as pd
import joblib
import ast

app = Flask(__name__)


@app.route('/ready', methods=['GET'])
def ready():
    return jsonify({'ready': True})


@app.route('/predict', methods=['POST'])
def predict():
    if model:
        try:
            # decode the dict stored as a string in the request
            string_ = request.data
            dict_str = string_.decode("UTF-8")
            data = ast.literal_eval(dict_str)

            df_data = pd.DataFrame.from_records([data])

            prediction = model.predict(df_data) - 1

            # model was trained with logged target data so predictions need to be post-processed
            prediction = np.exp(prediction) - 1

            return jsonify({'prediction': round(prediction[0])})

        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('No model found')
        return 'No model here to use'


if __name__ == '__main__':
    # load model
    model = joblib.load("random_forest.sav")
    print('Random forest model loaded')

    app.run(port=3000, debug=True)
