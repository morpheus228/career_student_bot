from abc import ABC, abstractmethod

from repositories.postgres.models import Form


class Answers(ABC):  
    @abstractmethod
    async def get(self, user_id: int) -> Form:
        pass

    @abstractmethod
    async def create(self, user_id: int) -> Form:
        pass