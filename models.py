from pydantic import BaseModel
class NoteCreate(BaseModel):
    title: str
    body: str = ""

class NoteOut(NoteCreate):
    id: int
    title: str
    body: str | None
    created_at: str
