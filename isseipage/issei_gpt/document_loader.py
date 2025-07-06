import os
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from .model import gpt_embeddings
import nltk

# Download required NLTK data before loading documents
# Based on LangChain documentation: https://python.langchain.com/docs/how_to/document_loader_markdown/
try:
    nltk.download('punkt', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    nltk.download('averaged_perceptron_tagger_eng', quiet=True)
except Exception as e:
    print(f"Warning: Could not download NLTK data: {e}")
    print("Please install required NLTK data manually or check your internet connection")

main_path = os.path.dirname(os.path.abspath(__file__))
md_path = os.path.join(os.path.dirname(main_path), "self_introduction.md")

# Check if markdown file exists
if not os.path.exists(md_path):
    raise FileNotFoundError(f"Markdown file not found: {md_path}")

try:
    # Load the markdown file
    loader = UnstructuredMarkdownLoader(md_path)
    documents = loader.load()
    
    # Create text splitter optimized for markdown structure
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,  #chunk size is 800 characters
        chunk_overlap=150,  #chunk overlap is 150 characters
        length_function=len,
        separators=[
            "\n## ",  # level 2 heading
            "\n### ",  # level 3 heading
            "\n\n",    # paragraph
            "\n",      # line break
            ". ",      # sentence end
            "! ",      # exclamation mark
            "? "       # question mark
        ]
    )
    
    # Split documents into chunks
    split_documents = text_splitter.split_documents(documents)
    
    # Create Chroma database with split documents
    db = Chroma.from_documents(documents=split_documents, embedding=gpt_embeddings)
    
    print(f"Loaded {len(split_documents)} document chunks from {md_path}")
    
except Exception as e:
    print(f"Error loading markdown file: {e}")
    raise

