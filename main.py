import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field

load_dotenv()

class NewsSummary(BaseModel):
    title: str = Field(description="News title")
    category: str = Field(description="News category")
    summary: str = Field(description="News summary")
    keywords: list[str] = Field(description="3 keywords")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_news(text: str):
    # 直接指定你清單裡有的最新可用模型
    target_model = "gemini-3.8-flash"
    print(f"正在使用模型: {target_model}")

    response = client.models.generate_content(
        model=target_model,
        contents=text,
        config={
            'response_mime_type': 'application/json',
            'response_schema': NewsSummary,
        },
    )
    print("--- 成功取得 AI 分析結果 ---")
    print(response.text)

if __name__ == "__main__":
    analyze_news("AI models are advancing rapidly and changing the tech industry.")