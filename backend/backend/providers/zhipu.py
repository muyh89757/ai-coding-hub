# 智谱 GLM API 接入

import httpx
from typing import Optional, List, Dict, Any

class ZhipuProvider:
    """智谱 GLM API 提供商"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://open.bigmodel.cn/api/paas/v4"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "glm-4",
        temperature: float = 0.7,
        max_tokens: int = 2048
    ) -> str:
        """
        调用智谱 GLM 对话 API
        
        Args:
            messages: 对话消息列表
            model: 模型名称 (glm-4, glm-3-turbo)
            temperature: 温度参数
            max_tokens: 最大生成 token 数
        
        Returns:
            AI 生成的回复内容
        """
        async with httpx.AsyncClient() as client:
            payload = {
                "model": model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens
            }
            
            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30.0
            )
            
            if response.status_code != 200:
                raise Exception(f"智谱 API 调用失败：{response.text}")
            
            data = response.json()
            return data["choices"][0]["message"]["content"]
    
    async def generate_code(
        self,
        prompt: str,
        language: str = "python"
    ) -> str:
        """
        生成代码
        
        Args:
            prompt: 代码需求描述
            language: 编程语言
        
        Returns:
            生成的代码
        """
        messages = [
            {"role": "system", "content": f"你是一个专业的{language}程序员，请根据用户需求生成高质量的代码。"},
            {"role": "user", "content": f"请用{language}实现以下功能：{prompt}"}
        ]
        
        return await self.chat_completion(messages, model="glm-4")
    
    async def explain_code(
        self,
        code: str,
        language: str = "python"
    ) -> str:
        """
        解释代码
        
        Args:
            code: 需要解释的代码
            language: 编程语言
        
        Returns:
            代码解释
        """
        messages = [
            {"role": "system", "content": "你是一个专业的代码讲解助手，请用简洁清晰的语言解释代码的功能和实现原理。"},
            {"role": "user", "content": f"请解释以下{language}代码的功能：\n\n```{language}\n{code}\n```"}
        ]
        
        return await self.chat_completion(messages, model="glm-4")
    
    async def get_usage(
        self,
        start_date: str,
        end_date: str
    ) -> Dict[str, Any]:
        """
        获取使用量统计
        
        Args:
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)
        
        Returns:
            使用量统计数据
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/usage",
                headers=self.headers,
                params={"start_date": start_date, "end_date": end_date},
                timeout=10.0
            )
            
            if response.status_code != 200:
                raise Exception(f"获取使用量失败：{response.text}")
            
            return response.json()

# 使用示例
if __name__ == "__main__":
    import asyncio
    
    async def main():
        # 初始化 provider
        provider = ZhipuProvider(api_key="your_api_key")
        
        # 测试对话
        response = await provider.chat_completion(
            messages=[{"role": "user", "content": "你好，请介绍一下自己"}]
        )
        print(f"AI 回复：{response}")
        
        # 测试代码生成
        code = await provider.generate_code(
            prompt="实现一个快速排序算法",
            language="python"
        )
        print(f"生成的代码：{code}")
    
    # asyncio.run(main())
