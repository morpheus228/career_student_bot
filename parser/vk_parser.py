import asyncio
import httpx
from pydantic import BaseModel, Field


class VkPost(BaseModel):
    id: int
    is_ads: bool = Field(alias="marked_as_ads")
    text: str 
    from_id: int



class VkParser:
    def __init__(self, token: str):
        self.token: str = token

        self.v = "5.81"
        self.filter = 'owner'
        self.url = 'https://api.vk.com/method/wall.get'

    async def parse_posts(self, group_id: str, number: int = 10):
        async with httpx.AsyncClient() as client:
            params = {
                'access_token': self.token,
                'v': self.v,
                'domain': group_id,
                'count': number,
                'filter': self.filter}
            
            response = await client.get(self.url, params=params)
            return [VkPost(**post) for post in response.json()['response']['items']]

    
async def main():
    token = "vk1.a.JnQfBgR3z0pPsF_Q7QWuRt9t1d28wF0vauk07fDkk_FlMNMTsTmgHC1tCq95qEVWPShnyc-qlonVlevRKFNT0ifKCY7a9wSVDjteXa8G9Sr7jYFA0Hc6CSTcKccAychY57f_Kr4zbLuxhDNwGhAO_kIt00vY8RrZM4vEhFwge7Cqcn5_nHkNVT8iZmg50MlKk4jMxx7At9G_rpNPmYcpmg"
    vp = VkParser(token)
    print(await vp.parse_posts('guap_job', number=2))



asyncio.run(main())