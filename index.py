from fastapi import FastAPI, File, UploadFile
from typing import List, Optional
import utils
import pandas as pd
import io

app = FastAPI()

@app.post("/api/")
async def api_endpoint(
    questions: UploadFile = File(...),
    files: Optional[List[UploadFile]] = None
):
    question_text = (await questions.read()).decode("utf-8")

    dfs = {}
    if files is not None:
        for f in files:
            if f.filename.endswith('.csv'):
                dfs[f.filename] = utils.read_csv(io.BytesIO(await f.read()))
            # Implement other file handlers here

    # -- Sample answer logic --
    # Replace below with your full workflow per question

    answer1 = 1                                     # stub for example, update for real task
    answer2 = "Titanic"                             # stub for example, update for real task
    answer3 = 0.485782                              # stub for example, update for real task
    answer4 = utils.scatter_with_regression(
        dfs['data.csv']['Rank'], dfs['data.csv']['Peak']) if 'data.csv' in dfs else None

    return [answer1, answer2, answer3, answer4]
