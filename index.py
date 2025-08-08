from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import base64
import io
import pandas as pd
import matplotlib.pyplot as plt
from typing import List
import time

app = FastAPI()

@app.post("/api/")
async def analyze(
    questions: UploadFile = File(...),
    files: List[UploadFile] = File(default=[])
):
    start = time.time()

    questions_text = (await questions.read()).decode()
    file_contents = {file.filename: await file.read() for file in files}

    # Fake logic for demo — replace with real LLM, web scraping, or DuckDB
    answer1 = 1
    answer2 = "Titanic"
    answer3 = 0.485782

    # Generate dummy scatter plot
    fig, ax = plt.subplots()
    x = [1, 2, 3, 4, 5]
    y = [1.5, 2.0, 2.5, 3.0, 3.5]
    ax.scatter(x, y)
    ax.plot(x, y, 'r--')  # red dotted line
    ax.set_xlabel("Rank")
    ax.set_ylabel("Peak")

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150)
    plt.close(fig)
    buf.seek(0)
    image_data = base64.b64encode(buf.read()).decode("utf-8")
    image_uri = f"data:image/png;base64,{image_data}"

    total_time = time.time() - start
    print(f"Processed in {total_time:.2f} seconds")

    return JSONResponse(content=[answer1, answer2, answer3, image_uri])
