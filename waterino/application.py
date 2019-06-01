from flask import Flask
from flask_restplus import Resource, Api, fields

application= app = Flask(__name__)
api = Api(app)

depth = 0.0
depth_model = api.model("depthModel", {
    "depth": fields.Float(depth)
})

@api.route('/depth')
class DepthCalculate(Resource):
    def get(self):
        global depth
        print("Inside get method " + str(depth))
        return {'distance':depth}

    @api.expect(depth_model)
    def post(self):
        global depth
        new_depth = api.payload
        depth = new_depth['depth']
        print(new_depth['depth'])
        return {'result': 'Updated'}, 201


if __name__ == '__main__':
    app.run(debug=True)





