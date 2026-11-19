import faiss
import numpy as np
from groq import Groq
from pydf import PDFReader
from sentence_transformers import SentenceTransformer

def load_pdf(pdf_path):
  reader = PDFReader(str(pdf_path))
  mypages = [i.extract_text() or "" fori in reader.pages]
  full_text = "\n".join(mypages).strip()
  if not fuii_text:
    raise valueError("No readable Text Found")
  return full_text  

def create_chunks(full_text, chunksize = 500,overlap=100):
  chunks = []
  start = 0
  while start<len(full_text):
    end = start+chunksize
    chunk = full_text[start:end]
    if chunk.strip():
      chunks.append(chunk)
    start = chunksize - overlap
return chunks
