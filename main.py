from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/api/")
async def analyze(questions: UploadFile = File(...), files: list[UploadFile] = File(default=[])):
    questions_txt = (await questions.read()).decode()
    file_dict = {f.filename: await f.read() for f in files}
    
    # Replace this with your real logic
    return JSONResponse(content={
        "message": "Received your request",
        "questions": questions_txt[:100],
        "file_names": list(file_dict.keys())
    })
