from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import config

# OpenAIの埋め込みモデルを設定
gpt_embeddings = OpenAIEmbeddings(api_key=config.OPENAI_API_KEY, model="text-embedding-3-small")

# LLMモデルのセットアップ
gpt_model = ChatOpenAI(api_key=config.OPENAI_API_KEY, model_name="gpt-4o-mini")
