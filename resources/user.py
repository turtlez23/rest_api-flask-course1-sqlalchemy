from flask_restful import Resource, reqparse

from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
      type=str,
      required=True,
      help='This field cannot be left blank!'
    )
    parser.add_argument('password',
      type=str,
      required=True,
      help='This field cannot be left blank!'
    )

    def post(self):
      data = UserRegister.parser.parse_args()

      if UserModel.find_by_username(data['username']):
        return {"message": "A user with that username already exists"}, 400
      
      # We can use dat **unpasking because we used a parser and we are shure abaut params
      user = UserModel(**data)
      user.save_to_db()

      return {"message": "User created succesfully."}, 201

    def get(self):
      return {"users": [u.json for u in UserModel.get_all_user()]}
