from aiogram import Bot
from aiogram.types import FSInputFile

import repositories
from repositories.postgres.models import Form
from utils.files import save_document
from ..interfaces import Forms



class FormsService(Forms):
	def __init__(self, repository: repositories.Forms, bot: Bot):
		self.repository: repositories.Forms = repository
		self.bot: Bot = bot

	async def create(self, user_id: int, data: dict) -> int:
		video = data.get('video', None)
		if video is not None:
			video = await save_document(self.bot, user_id, video)
		data['video'] = video
		
		photo_1 = data.get('photo_1', None)
		if photo_1 is not None:
			photo_1 = max(data['photo_1'], key=lambda x: x.file_size)
			photo_1 = await save_document(self.bot, user_id, photo_1)
		data['photo_1'] = photo_1

		photo_2 = data.get('photo_2', None)
		if photo_2 is not None:
			photo_2 = max(data['photo_2'], key=lambda x: x.file_size)
			photo_2 = await save_document(self.bot, user_id, photo_2)
		data['photo_2'] = photo_2

		photo_3 = data.get('photo_3', None)
		if photo_3 is not None:
			photo_3 = max(data['photo_3'], key=lambda x: x.file_size)
			photo_3 = await save_document(self.bot, user_id, photo_3)
		data['photo_3'] = photo_3

		return self.repository.create(Form(
			user_id = user_id,
			gender = data['gender'],
			faculty = data['faculty'],
			course = data['course'],
			name = data['name'],
			about = data['about'],
			request = data['request'],
			photo_1 = data['photo_1'],
			photo_2 = data['photo_2'],
			photo_3 = data['photo_3'],
			video = data['video']
		))
	
	async def get_by_user_id(self, user_id: int) -> Form:
		form = self.repository.get_by_user_id(user_id)
		
		if form is not None:
			form = self.prepare_media(form)
			
		return form
	
	async def get_by_id(self, form_id: int) -> Form:
		form = self.repository.get_by_id(form_id)
		
		if form is not None:
			form = self.prepare_media(form)
			
		return form
	
	@staticmethod
	def prepare_media(form):
		if form.video is not None:
				form.video = FSInputFile("files/" + form.video)
		else:
			if form.photo_1 is not None:	
				form.photo_1 = FSInputFile("files/" + form.photo_1)

			if form.photo_2 is not None:
				form.photo_2 = FSInputFile("files/" + form.photo_2)

			if form.photo_3 is not None:
				form.photo_3 = FSInputFile("files/" + form.photo_3)
		
		return form