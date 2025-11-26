from soldiers.reader_CSV import reader_csv_file
from fastapi import FastAPI
import uvicorn
from fastapi import FastAPI,File, UploadFile

app = FastAPI()

@app.post("/assignWithCsv")
def get_file(file: UploadFile = File()):
        return reader_csv_file(file)
    

if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8000)