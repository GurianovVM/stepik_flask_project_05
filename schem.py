from marshmallow import fields, Schema

class StoreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    address = fields.String()