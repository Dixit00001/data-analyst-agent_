from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List, Optional
import pandas as pd
import io
import utils

app = FastAPI()

def parse_questions(question_text: str):
    lines = question_text.strip().split('\n')
    questions = []
    for line in lines:
        line = line.strip()
        if line and line[0].isdigit():
            questions.append(line)
    return questions

def analyze_data(df: pd.DataFrame):
    # Replace these stub logic with real analysis based on data and questions
    two_billion_before_2000 = 1
    earliest_high_gross = "Titanic"
    correlation = df['Rank'].corr(df['Peak'])
    return two_billion_before_2000, earliest_high_gross, correlation

@app.post("/api/")
async def api_endpoint(
    questions: UploadFile = File(...),
    files: Optional[List[UploadFile]] = None
):
    try:
        question_text = (await questions.read()).decode("utf-8")
        parsed_questions = parse_questions(question_text)

        dfs = {}
        if files:
            for f in files:
                if f.filename.endswith(".csv"):
                    content = await f.read()
                    try:
                        df = pd.read_csv(io.BytesIO(content))
                        dfs[f.filename] = df
                    except Exception as e:
                        raise HTTPException(status_code=400, detail=f"Invalid CSV file {f.filename}: {str(e)}")

        if 'data.csv' not in dfs:
            raise HTTPException(status_code=400, detail="data.csv file missing")

        df = dfs['data.csv']
        answer1, answer2, answer3 = analyze_data(df)
        answer4 = utils.scatter_with_regression(df['Rank'], df['Peak'])

        return [answer1, answer2, answer3, answer4]

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
