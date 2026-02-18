from fastapi import APIRouter, Depends, HTTPException, status

from services import NoteService
from .models import NoteCreate, NoteOut
from .repositories import NoteRepository

router = APIRouter(prefix="/notes", tags=["notes"])

def get_service():
    repo = NoteRepository()
    return NoteService(repo)

@router.post("/", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate, service: NoteService = Depends(get_service)):
    try:
        return service.create_note(title=payload.title, body=payload.body)
    except ValueError:
        raise HTTPException(status_code=422, detail="title_empty")
    
@router.get("/{note_id}", response_model=NoteOut)
def get_note(note_id: int, service: NoteService = Depends(get_service)):
    note = service.get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="note_not_found")
    return note