import os
import numpy as np
from dotenv import load_dotenv
from flask import Flask, request, jsonify, session
from flask_cors import CORS
import faiss
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# Load .env and config
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash-lite-preview-06-17")

# Flask app
app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:5173"])
app.secret_key = os.getenv("SECRET_KEY")

# Constants
model_name = "models/gemini-2.5-flash-lite-preview-06-17"
SYSTEM_PROMPT = """
Sen bir psikolojik destek botusun. Kullanıcının duygularını anlamaya çalış, sakinleştirici, cesaret verici, empatik ve nazik cevaplar ver. 
Kullanıcıyı dinle ve gerektiğinde profesyonel yardım almaya yönlendir. Sadece nazik ve destekleyici ol.
"""

# Load knowledge base
with open("data.txt", "r", encoding="utf-8") as file:
    knowledge_texts = [line.strip() for line in file if line.strip()]

# Embedding model
embed_model = SentenceTransformer("C:\\Users\\mehta\\Desktop\\ChatBot\\all-MiniLM-L6-v2")
print("Model yüklendi")
kb_embeddings = embed_model.encode(knowledge_texts)

# FAISS index
dimension = kb_embeddings.shape[1]
faiss_index = faiss.IndexFlatL2(dimension)
faiss_index.add(np.array(kb_embeddings))

# Similarity search
def get_similar_knowledge(query, top_k=3):
    query_vec = embed_model.encode([query])
    distances, indices = faiss_index.search(np.array(query_vec), top_k)
    return [knowledge_texts[i] for i in indices[0]]

@app.route("/", methods=["GET"])
def index():
    return "API çalışıyor"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    lang = session.get("language", "tr")

    if not user_message.strip():
        return jsonify({"answer": "Lütfen bir mesaj yazınız." if lang == "tr" else "Please enter a message."})

    # En alakalı veri seti cümlelerini bul
    relevant_contexts = get_similar_knowledge(user_message, top_k=3)
    context_text = "\n".join(relevant_contexts)

    # Yeni prompt: veri + kullanıcı mesajı
    prompt = f"""{SYSTEM_PROMPT}

Bilgi:
{context_text}

Kullanıcı: {user_message}

Cevabın:"""

    # Gemini cevabı üret
    try:
        response = model.generate_content(
            
            contents=prompt,
           
        )
        answer = response.text.strip()

    except Exception as e:
        print(f"API çağrısında hata: {e}")
        answer = "Üzgünüm, şu anda cevap veremiyorum."

    return jsonify({"answer": answer})

if __name__ == "__main__":
   
    app.run(host="127.0.0.1", port=5000, debug=True)
