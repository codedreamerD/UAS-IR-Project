import os
import json
import re
from docx import Document
from PyPDF2 import PdfReader
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Initialize Sastrawi Stemmer
stemmer = StemmerFactory().create_stemmer()

# Mapping download links and source URLs
links = {
    "591-1186-1-SM.docx": "https://docs.google.com/document/d/1b9R2v_BuHvlMAzF7WOiUeolgeyS3p-Q-/edit?usp=drive_link",
    "18307-58685-1-RV.docx": "https://docs.google.com/document/d/1b9R2v_BuHvlMAzF7WOiUeolgeyS3p-Q-/edit?usp=drive_link",
    "40486-ID-ramuan-herbal-non-instan-dalam-naskah-kitab-tib-sebagai-alternatif-pengobatan.docx": "https://docs.google.com/document/d/1b7k5HFQMxfQSC75ea_vAXFYu5-5SKBOD/edit?usp=drive_link",
    "75178-Article Text-225005-1-10-20231127.docx": "https://docs.google.com/document/d/1bBujSU6BbT9EfgzNP2IUd2PqBPubAaQq/edit?usp=drive_link",
    "adiyasa-p130-138.docx": "https://docs.google.com/document/d/1b9nhYgP3E1r1P4InyP-sokQ6a9GTkOCh/edit?usp=drive_link",
    "323-Article Text-1145-1-10-20221206.pdf": "https://drive.google.com/file/d/1b4IqEJKuYoFyrLJeyxUQxfJ4ePOu0br0/view?usp=drive_link",
    "5972-Fix-Hal+9-18+PDF.pdf": "https://drive.google.com/file/d/1b-s2MhgcdyXb7Z2LfCPfuxzUwetHGIhR/view?usp=drive_link",
    "124817-ID-none.pdf": "https://drive.google.com/file/d/1b4ZO7VqDrIKAvpVnFrd3WY-7CHEBmx2Q/view?usp=drive_link",
    "E-book-Rempah-Herba-Luchman-HAkim-2016.pdf": "https://drive.google.com/file/d/1b3MjEziRottasZSC1mZ4cAnAZGfXynE9/view?usp=drive_link",
    "Pemanfaatan_Tumbuhan_Sebagai_Obat_Tradis.pdf": "https://drive.google.com/file/d/1b6ujCFJ-K9PK1JvveeZ_DB5Wk-brGsJ6/view?usp=drive_link",
    "artikel_1.txt": {
        "download_link": "https://drive.google.com/file/d/1azzkx8yIu0FAmad-DJAsWjRoT2m0tX9S/view?usp=drive_link",
        "source_url": "https://www.cnnindonesia.com/gaya-hidup/20231124115241-262-1028430/7-minuman-herbal-untuk-menyembuhkan-flu-tak-perlu-pakai-obat"
    },
    "artikel_2.txt": {
        "download_link": "https://drive.google.com/file/d/1azBg93UYcSrlavJmQPslBxgAP3r-KD6C/view?usp=drive_link",
        "source_url": "https://www.alodokter.com/45-masyarakat-indonesia-masih-lebih-percaya-obat-herbal-dibanding-obat-modern"
    },
    "artikel_3.txt": {
        "download_link": "https://drive.google.com/file/d/1ayrFFMFglieIoYOU-woam23sohW9sxiN/view?usp=drive_link",
        "source_url": "https://health.detik.com/berita-detikhealth/d-7692713/8-obat-herbal-untuk-asam-urat-ada-kunyit-hingga-air-putih"
    },
    "artikel_4.txt": {
        "download_link": "https://drive.google.com/file/d/1bFToPwaq02SmEPGjuRD4TlocLhHlmXv5/view?usp=sharing",
        "source_url": "https://health.detik.com/berita-detikhealth/d-7667607/6-manfaat-rebusan-daun-salam-untuk-kesehatan-mudah-dibuat-di-rumah"
    },
    "artikel_5.txt": {
        "download_link": "https://drive.google.com/file/d/1bDGuRgw7SPcD5CED1e1wr_5UQuS03u3h/view?usp=drive_link",
        "source_url": "https://www.cnnindonesia.com/gaya-hidup/20240821155433-255-1135809/5-air-rebusan-untuk-redakan-sakit-kepala-cenat-cenut-hilang"
    }
}

# Functions
def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def read_docx(file_path):
    doc = Document(file_path)
    return '\n'.join([p.text for p in doc.paragraphs])

def read_pdf(file_path):
    reader = PdfReader(file_path)
    return '\n'.join([page.extract_text() for page in reader.pages])

def tokenize(content):
    return re.findall(r'\b\w+\b', content.lower())

def remove_stopwords(tokens, stopword_file):
    with open(stopword_file, 'r', encoding='utf-8') as f:
        stopwords = set(f.read().splitlines())
    return [word for word in tokens if word not in stopwords]

def stem_tokens(tokens):
    return [stemmer.stem(word) for word in tokens]

# Main Process
def process_files_to_json(input_folder, output_file, stopword_file):
    result = []

    for root, _, files in os.walk(input_folder):
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            content = ""

            try:
                if ext == '.txt':
                    content = read_txt(file_path)
                elif ext == '.docx':
                    content = read_docx(file_path)
                elif ext == '.pdf':
                    content = read_pdf(file_path)
                else:
                    print(f"Unsupported format: {file}")
                    continue

                # Preprocessing
                tokens = tokenize(content)
                filtered_tokens = remove_stopwords(tokens, stopword_file)
                stemmed_tokens = stem_tokens(filtered_tokens)

                # Retrieve download link and source URL
                link_info = links.get(file, {})
                download_link = link_info.get("download_link") if isinstance(link_info, dict) else link_info
                source_url = link_info.get("source_url") if isinstance(link_info, dict) else None

                # Append processed data
                result.append({
                    "filename": file,
                    "content": content,
                    "tokens": stemmed_tokens,
                    "download_link": download_link,
                    "source_url": source_url
                })

                print(f"Processed: {file}")

            except Exception as e:
                print(f"Error processing {file}: {e}")

    # Save all data to a single JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, indent=4, ensure_ascii=False)

# Paths
input_folder = r"H:\My Drive\KULIAH\Semester 5\IFB307-DATA MINING DAN INFORMATION RETRIEVAL-DD\UAS\Program-2\PROJECT\DATASET"
output_file = r"H:\My Drive\KULIAH\Semester 5\IFB307-DATA MINING DAN INFORMATION RETRIEVAL-DD\UAS\Program-2\PROJECT\processed_documents-2.json"
stopword_file = r"H:\My Drive\KULIAH\Semester 5\IFB307-DATA MINING DAN INFORMATION RETRIEVAL-DD\UAS\Program-2\PROJECT\stopwords.txt"

# Buat folder jika belum ada
output_folder = os.path.dirname(output_file)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

process_files_to_json(input_folder, output_file, stopword_file)
