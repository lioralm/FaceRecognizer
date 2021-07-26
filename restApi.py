from numpy import dot
from numpy.linalg import norm

from flask import Flask
from flask_restful import Resource, Api, reqparse

import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


def convert_string(s):
    feature = ast.literal_eval(s)
    return [float(n) for n in feature]


class Person(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()  # initialize

            parser.add_argument('name', required=True)  # add args
            parser.add_argument('features', required=True)

            args = parser.parse_args()  # parse arguments to dictionary

            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'name': args['name'],
                'features': args['features']
            }, index=[0])

            # read our CSV
            data = pd.read_csv('persons.csv')

            # add the newly provided values
            data = data.append(new_data, ignore_index=True)
            # save back to CSV
            data.to_csv('persons.csv', index=False)
            return "successes", 200  # return data with 200 OK

        except:
            return "fail", 500  # return data with 500 FAIL

    def get(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('features', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary
        feature = convert_string(args['features'])

        data = pd.read_csv('persons.csv', dtype={'name': str, 'features': str})  # read CSV

        data = data.to_dict('r')  # convert dataframe to dictionary

        cosine = []
        match = {}
        for dict in data:
            features = convert_string(dict['features'])
            # the cosine represnts the similarity between two vectors
            cos = dot(feature, features) / (norm(feature) * norm(features))
            cosine.append(cos)
            match[cos] = dict['name']

        persons = []
        # the biggest cosines represent the most similar persons
        cosine.sort(reverse=True)
        for c in cosine[:3]:
            persons.append(match[c])

        return persons, 200  # return data and 200 OK code

    pass


api.add_resource(Person, '/persons')  # '/person' is our entry point

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)  # run our Flask app