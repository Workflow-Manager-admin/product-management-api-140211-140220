from marshmallow import Schema, fields, validate

# PUBLIC_INTERFACE
class ProductSchema(Schema):
    """Product Marshmallow schema for serialization/validation."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=120))
    description = fields.Str(allow_none=True, validate=validate.Length(max=256))
    price = fields.Float(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
