from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from find_document_similaritys import *

app = FastAPI()
fds = FindDocumentSimilaritys()

class InputData:
    def __init__(self, text:str, count_documents: int = 5):
        self.text = text
        self.count_documents = count_documents

@app.get('/documents/')
def get_documents(data: InputData = Depends()):
    if data.count_documents < 1:
        return HTTPException(status_code=400, detail="Количество документов должно быть больше нуля!")
    
    if len(data.text) < 1:
        return HTTPException(status_code=400, detail="Для поиска документа, необходимо ввести текст!")

    return fds.find_documents(data.text, data.count_documents)