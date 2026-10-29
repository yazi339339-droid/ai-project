# 📰 AI 新聞摘要與分析工具 (AI News Summarizer)

這是一個基於 Python 與 Google Gemini API 開發的新聞自動化分析與摘要工具。利用最新的 Gemini 語言模型與 Pydantic 結構化資料驗證，將任意新聞文字自動解析並輸出為標準的 JSON 格式，方便後續資料處理與系統整合。

## ✨ 專案亮點

- **結構化輸出 (Structured Outputs)**：使用 Pydantic定義模式，確保 API 回傳格式為嚴格的 JSON（包含標題、分類、摘要與關鍵字）。
- **現代化 Python 環境管理**：採用高效能的 `uv` 進行依賴套件管理與環境隔離。
- **最新 API 支援**：整合官方最新的 `google-genai` SDK 並使用 `gemini-3.8-flash` 模型。
- **安全性設計**：金鑰分離管理，避免敏感 API Key 洩露至版控系統。

## 🛠️ 技術棧 (Tech Stack)

- **Language**: Python 3.10+
- **Environment Management**: `uv`
- **AI Model**: Google Gemini API (`google-genai` SDK)
- **Data Validation**: Pydantic v2
- **Environment Variables**: `python-dotenv`

## 🚀 快速開始 (Quick Start)

### 1. 複製儲存庫與環境準備

```bash
# 下載專案
git clone [https://github.com/yazi339339-droid/ai-project.git](https://github.com/yazi339339-droid/ai-project.git)
cd ai-project

# 使用 uv 自動建立環境並安裝依賴
uv sync
