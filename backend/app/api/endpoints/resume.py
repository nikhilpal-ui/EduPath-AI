from app.services.profile_analyzer import analyze_resume
from pathlib import Path

import pymupdf
from fastapi import APIRouter, File, UploadFile, HTTPException


router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    file_bytes = await file.read()

    if not file_bytes:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as f:
        f.write(file_bytes)

    try:
        document = pymupdf.open(file_path)

        extracted_text = ""

        for page in document:
            extracted_text += page.get_text()

        page_count = len(document)
        document.close()
        profile = analyze_resume(extracted_text)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Could not read PDF: {str(e)}"
        )

    return {
    "message": "Resume analyzed successfully",
    "filename": file.filename,
    "pages": page_count,
    "text_length": len(extracted_text),
    "profile": profile,
    "extracted_text": extracted_text[:10000]
}