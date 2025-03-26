
import mimetypes
from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Email, Attachment
from schemas import EmailSchema, EmailResponseSchema
#import multipart

router = APIRouter(prefix="/api", tags=["Email Processing"])

# Define categories based on file types
FILE_CATEGORIES = {
    "public": ["image/jpeg", "image/png", "text/plain"],
    "private": ["application/pdf", "application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"],
    "confidential": ["application/zip", "application/x-rar-compressed"],
}

def classify_attachment(filename: str) -> str:
    mime_type, _ = mimetypes.guess_type(filename)
    if mime_type:
        for category, types in FILE_CATEGORIES.items():
            if mime_type in types:
                return category
    return "unknown"

@router.post("/process-email", response_model=EmailResponseSchema)
async def process_email(
    email_body: str = Form(...),
    classification: str = Form(...),  # Accept classification from frontend
    attachments: list[UploadFile] = File(None),
    db: Session = Depends(get_db),
):
    email = Email(body=email_body, category=classification)
    db.add(email)
    db.commit()
    db.refresh(email)

    attachment_responses = []
    for file in attachments or []:
        category = classify_attachment(file.filename)
        attachment = Attachment(filename=file.filename, file_type=file.content_type, classification=category, email_id=email.id)
        db.add(attachment)
    attachment_responses.append({"filename": file.filename, "file_type": file.content_type, "classification": category, "category": category})

    db.commit()
    return {"email_body": email_body, "classification": category, "attachments": attachment_responses}