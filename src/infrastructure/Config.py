from src.business_logic.images_repository import ImagesRepository
from src.infrastructure.images_file_repository import ImagesFileRepository


def images_repository() -> ImagesRepository:
    return ImagesFileRepository()
