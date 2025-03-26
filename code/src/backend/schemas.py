from pydantic import BaseModel
from typing import List, Optional

class AttachmentSchema(BaseModel):
    filename: str
    file_type: str
    classification: str
    category: str  # Add category if needed

class EmailSchema(BaseModel):
    email_body: str
    classification: str  
    attachments: Optional[List[AttachmentSchema]] = None  # Set default to None

class EmailResponseSchema(BaseModel):
    email_body: str  
    classification: str
    attachments: List[AttachmentSchema]


