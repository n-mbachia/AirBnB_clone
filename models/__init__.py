"""Contains some global variables."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

