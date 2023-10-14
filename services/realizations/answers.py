from repositories.postgres.models import Form
from services.interfaces import Answers


class AnswersService(Answers):  
    def __init__(self):
        pass
    
    async def get(self, user_id: int) -> list[Form]:
        # получаем объекты Match, которые без паметки success в которых getter_id == user_id
        pass

    async def create(self, user_id: int, value: bool) -> Form:
        # update объект Match с success == value

        # отправляем сообщения обоим пользователям о том, что был коннект
        pass

    async def run():
        pass