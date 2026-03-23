# MiniMax API 接入

import httpx
from typing import List, Dict

class MiniMaxProvider:
    """MiniMax API 提供商"""
    
    def __init__(self, api_key: str, group_id: str):
        self.api_key = api_key
        self.group_id = group_id
        self.base_url = "https://api.minimax.chat/v1"
    
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "abab6.5"
    ) -> str:
        """调用 MiniMax 对话 API"""
        async with httpx.AsyncClient() as client:
            payload = {
                "model": model,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 2048
            }
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            response = await client.post(
                f"{self.base_url}/text/chatcompletion_v2",
                headers=headers,
                json=payload,
                timeout=30.0
            )
            
            if response.status_code != 200:
                raise Exception(f"MiniMax API 调用失败：{response.text}")
            
            data = response.json()
            return data["choices"][0]["message"]["content"]
