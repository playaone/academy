What is the difference between a SQLAlchemy model and a Marshmallow schema?
    An SQLAlchemy model defines database tables, relationships, columns, data types, and how the database is operated. Meanwhile a Marshmallow schema defines data serialization, data inputs, validations, and constraints of data received or sent to or from the client.

What is the difference between load() and dump()?
    Load collects data and validates them, while dump serializes data and returns a json compatible version.

Why does the creation schema require a title while the update schema does not?
    The creation schema must match what the database is expecting to create a new record. The update schema is not creating a new record rather updating an existing record, which means the required fields are already existing in the record.

What does unknown = RAISE do?
    This raises a validation error when the schema receives an unknown field.

Why should duplicate-title validation remain in the service?
    This is because dupplicate title is a business decision.

Why should API responses use schemas instead of returning model.__dict__?
    Schemas help control what is exposed, and returning model.__dict__ may expose sensitive data.

What is the purpose of many=True?
    This tells the schema that multiple instances of the data will be passed in, therefor it will serialize the data as multiple.

What is the difference between allow_none=True and load_default=None?
    "allow_none = True" tell the schema that null value is acceptable, while "load_default=None" tell the schema to assume null value as the default value of the field.