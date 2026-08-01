from marshmallow import (
    EXCLUDE,
    RAISE,
    Schema,
    fields,
    validate,
    validates_schema
)
from marshmallow.exceptions import ValidationError

class ProjectCreateSchema(Schema):
    class Meta:
        unknown = RAISE
        
    title = fields.String(
        required=True,
        validate=validate.Length(min=1, max=150)
    )
    
    description = fields.String(
        required=True,
        validate=validate.Length(min=1, max=2000)
    )
    
    github_url = fields.Url(
        load_default=None,
        allow_none=True
    )
    
    website_url = fields.Url(
        load_default=None,
        allow_none=True
    )
    
    technologies = fields.String(
        load_default=None,
        allow_none=True,
        validate=validate.Length(max=500)
    )
    
    @validates_schema
    def normalize_text_fields(self, data, **kwargs):                    
                    
        for field_name in ("title", "description"):
            value = data.get(field_name)
            
            if isinstance(value, str):
                cleaned_value = value.strip()
                
                if not cleaned_value:
                    raise ValidationError(
                        "Field cannot contain only whitespace.",
                        field_name=field_name
                    )
                    
                data[field_name] = cleaned_value
        
        for field_name in ("github_url", "website_url", "technologies"):
            value = data.get(field_name)
            
            if isinstance(value, str):
                cleaned_value = value.strip()
                data[field_name] = cleaned_value or None
                

class ProjectUpdateSchema(Schema):
    class Meta:
        unknown = RAISE
        
    title = fields.String(validate=validate.Length(min=1, max=150))
    
    description = fields.String(validate=validate.Length(min=1, max=2000))
    
    github_url = fields.Url(
        allow_none=True
    )
    
    website_url = fields.Url(
        allow_none=True
    )
    
    technologies = fields.String(
        allow_none=True
    )
    
    @validates_schema
    def validate_and_normalize(self, data, **kwargs):
        print("Validating and normalizing data:", data)
        if not data:
            raise ValidationError(
                "Provide at least one field to update."
            )
            
        for field_name in ("title", "description"):
            if field_name not in data:
                continue
            
            value = data[field_name]
            
            if isinstance(value, str):
                cleaned_value = value.strip()
                
                if not cleaned_value:
                    raise ValidationError(
                        "Field cannot contain only whitespace.",
                        field_name=field_name
                    )
                    
                data[field_name] = cleaned_value
                
        for field_name in ("github_url", "website_url", "technologies"):
            if field_name not in data:
                continue
            
            value = data[field_name]
            
            if isinstance(value, str):
                cleaned_value = value.strip()
                
                data[field_name] = cleaned_value or None
                
                
class ProjectResponseSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    
    github_url = fields.Url(allow_none=True)
    
    website_url = fields.Url(allow_none=True)
    
    technologies = fields.String(allow_none=True)
    
    created_at = fields.DateTime(allow_none=True)
    
    updated_at = fields.DateTime(allow_none=True)


project_create_schema = ProjectCreateSchema()
project_update_schema = ProjectUpdateSchema()
project_response_schema = ProjectResponseSchema()
projects_response_schema = ProjectResponseSchema(many=True)


    
    