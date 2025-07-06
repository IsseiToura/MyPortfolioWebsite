import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
SERP_API_KEY = os.getenv("SERP_API_KEY", "")