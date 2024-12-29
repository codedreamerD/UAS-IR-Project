from flask import Flask, render_template, request
from rank_bm25 import BM25Okapi
import json
from collections import Counter

app = Flask(__name__)

# Fungsi untuk membaca JSON
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Load data JSON
json_file_path = "processed_documents-2.json"  
data = load_json(json_file_path)

# Membuat korpus untuk BM25
corpus = [doc["tokens"] for doc in data]
bm25 = BM25Okapi(corpus)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    query = request.form['query'].lower().split()  # Tokenisasi query
    scores = bm25.get_scores(query)  # Hitung skor relevansi
    results = [(data[i]["filename"], scores[i]) for i in range(len(data))]
    results = sorted(results, key=lambda x: x[1], reverse=True)  # Urutkan berdasarkan skor
    return render_template('result.html', query=' '.join(query), results=results)

@app.route('/view/<filename>')
def view_file(filename):
    # Cari dokumen berdasarkan nama file
    doc = next((doc for doc in data if doc["filename"] == filename), None)
    if doc:
        # Hitung frekuensi kata dasar
        token_counts = Counter(doc["tokens"])

        # Kirim data tambahan untuk download link dan source URL
        download_link = doc.get("download_link", None)  # Properti untuk link unduhan
        source_url = doc.get("source_url", None)  # Properti untuk artikel asli (khusus TXT)
        
        return render_template(
            'view.html',
            filename=doc["filename"],
            content=doc["content"],
            token_counts=token_counts,
            download_link=download_link,
            source_url=source_url
        )
    else:
        # Jika dokumen tidak ditemukan, tampilkan pesan error
        return "Dokumen tidak ditemukan.", 404

if __name__ == "__main__":
    app.run(debug=True)
