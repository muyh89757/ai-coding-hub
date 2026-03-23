# 火山方舟 API 接入

import httpx
from typing import List, Dict

class VolcengineProvider:
    """火山方舟 API 提供商"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://ark.cn-beijing.volces.com/api/v3"
    
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "doubao-pro"
    ) -> str:
        """调用火山方舟对话 API"""
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
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=30.0
            )
            
            if response.status_code != 200:
                raise Exception(f"火山方舟 API 调用失败：{response.text}")
            
            data = response.json()
            return data["choices"][0]["message"]["content"]
