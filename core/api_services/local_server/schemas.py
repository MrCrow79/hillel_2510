from marshmallow import Schema, fields, ValidationError




def check_name(value):
    if value[0] != value[0].upper():
        raise ValidationError("First letter should be upper")

    if len(value)< 4:
        raise ValidationError("Name should have at least 4 symbols")




class BaseUserSchema(Schema):

    id = fields.Int(required=True)
    name = fields.Str(validate=check_name)
    score = fields.Int(allow_none=True)  #  можу бути None
    updated_date = fields.DateTime()
    created_date = fields.Raw()  # приймає будь-яке значення

#
# class UserSchema(Schema):
#
#     id = fields.Int()
#     name = fields.Str()
#     score = fields.Int()
#     updated_date = fields.DateTime()
#     created_date = fields.Float()
#     friends = fields.Nested(BaseUserSchema, many=True)  #
#
#
# class UserSchemav2(BaseUserSchema):
#
#     friends = fields.Nested(BaseUserSchema, many=True)
#
#
#
#
# class VolumeSchema(Schema):
#
#     id = fields.Int()
#     volume = fields.Int(allow_none=True)  #  може бути None

# class UserVolumeSchema(Schema):
#
#     id = fields.Int()
#     name = fields.Str(required=True)
#     score = fields.Int()
#     updated_date = fields.DateTime()
#     created_date = fields.Float()
#     volume_type = fields.Nested(VolumeSchema)  #  Nested = вкладене, many=True - означае список об'єктів BaseUserSchema
# # #  Nested = вкладене, many=True - означае список об'єктів BaseUserSchema
# #
# user2 = {
#     "created_date": 1734367927.6856365,
#     "id": 630,
#     "name": "Elvis",
#     "score": 58,
#     "updated_date": "2024-12-16T18:55:42+0200",
#     # 'volume_type': {'id': 4, 'volume': 2}
# }

# BaseUserSchema().load(user2)
#
# UserVolumeSchema().load(user2)

    #
# user =   {
#         "created_date": 1734367927.6856365,
#         "id": 630,
#         "name": "Elvis",
#         "score": 58,
#         "updated_date": "2024-12-16T18:55:42+0200",
#         "friends": [
#             {
#                 "created_date": 1734367927.6856365,
#                 "id": 123,
#                 "name": "Elvis",
#                 "score": 45,
#                 "updated_date": "2024-12-16T18:55:42+0200",
#             },
#             {
#                 "created_date": 1734367927.6856365,
#                 "id": 632,
#                 "name": "Elvis",
#                 "score": 89,
#                 "updated_date": "2024-12-16T18:55:42+0200",
#             }
#         ]
#
#     }
#
# UserSchemav2().load(user)