from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()

UPLOAD_FOLDER = "src/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

templates = Jinja2Templates(directory="src/templates")


@router.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


@router.post("/upload/", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    file_location = f"{UPLOAD_FOLDER}/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    return templates.TemplateResponse("success.html", {"request": request, "filename": file.filename})


@router.get("/download/{file_name}")
async def download_file(file_name: str):
    file_path = f"{UPLOAD_FOLDER}/{file_name}"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type='application/octet-stream', filename=file_name)
    return {"error": "File not found"}
