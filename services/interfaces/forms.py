from abc import ABC, abstractmethod

from repositories.postgres.models import Form


class Forms(ABC):
	@abstractmethod
	async def create(self, user_id: int, data: dict) -> int:
		pass

	@abstractmethod
	async def get_by_user_id(self, user_id: int) -> Form:
		pass
	
	@abstractmethod
	async def get_by_id(self, form_id: int) -> Form:
		pass
	
	# @abstractmethod
	# async def check_uniqueness(self, api_id: int, api_hash: str, phone_number: str) -> bool:
	# 	pass
	
	# @abstractmethod
	# async def request_sms_code(self, api_id: int, api_hash: str, phone_number: str) -> tuple[Client, SentCode]:
	# 	pass
	
	# @abstractmethod
	# def get(self, user_id: int) -> Client|None:
	# 	pass
	
	# @abstractmethod
	# def give(self, name: str, session_string: str):
	# 	pass