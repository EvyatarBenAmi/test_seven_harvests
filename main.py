from fastapi import FastAPI
import uvicorn
from fastapi import FastAPI,File, UploadFile
import csv

app = FastAPI()

@app.post("/assignWithCsv")
def reader_csv_file(file: UploadFile = File()) -> list[dict]:
    text = file.read().decode()
    reader = csv.DictReader(text.splitlines())
    list_soldier = [row for row in reader]
    print(list_soldier)
    return list_soldier

if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8000)