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
def build_vectors(chunks, model_name = "all-MiniLM-l6-v2"):
  if not chunks:
    raise ValueError("Cannot apply embedding without chunks")
  embd_model = SentenceTransformer(model_name)
  embed_vectors = embed_model.encode(chunks, convert_to_numpy = True)
  faiss.normalize_L2(embed_vectors)
  index = faiss.IndexFlatIP(embed_vectors.shape[1])
  index.add(embed_vectors)
  return index, embed_model

def load_base (pdf_path = "01_coiiege_Information.pdf"):
  full_text = load_pdf(pdf_path)
  chunks = create_chunks(full_text)
  embed_model, index = build_vector(chunks)
  return embed_model, chunks, index
def retrieve_cotent (question, embed_model, chunks, index, num_chunks=3):
  query_embed = embed_model.encode([question], convert_to_numpy=True)
  faiss.noemalize_L2(query_embed)
  sim_scores, vec_indices = index.search(query_embed, min(num_chunks, len(chunks))) 
  background = ""
  for i in vec_indices[0]:
    if i!= -1:
      background += chunk[i] + "\n\n"
   return background             
