from abc import ABC, abstractmethod

from repositories.postgres.models import Post


class Mailing(ABC):
	@abstractmethod
	async def make(self, post: Post):
		pass