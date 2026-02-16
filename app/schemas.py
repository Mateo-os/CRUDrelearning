from marshmallow import Schema, fields, validate

class TaskSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1))
    completed = fields.Boolean()
