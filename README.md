<p align="center">
  <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="180px" alt="PDF Summarizer" />
</p>

<h1 align="center">📝 PDF Summarizer</h1>

<p align="center">
  <b>Summarize PDF documents using NLP & HuggingFace Transformers with a clean Streamlit interface</b><br/>
  <a href="https://github.com/abdulrahmanhamdi/pdf-summarizer/stargazers">⭐ Star this repo</a> to support the project!
</p>

---

## 🚀 Features

- 📄 Upload **PDF files** with ease  
- 🔍 Automatically **extracts text** using `PyMuPDF`  
- 🧠 Summarizes using **HuggingFace Transformers** (`facebook/bart-large-cnn`)  
- ⚡ Simple and intuitive **Streamlit UI**  
- 🔀 Handles large texts by chunking and summarizing section-by-section  

---

## 📷 Demo

https://github.com/abdulrahmanhamdi/pdf-summarizer/assets/demo.gif  
> *(Replace this with a real demo GIF or screen recording)*

---

## 🛠️ Tech Stack

| Tool/Library          | Description                         |
|----------------------|-------------------------------------|
| `Streamlit`          | Web App Interface                   |
| `PyMuPDF (fitz)`     | PDF Text Extraction                 |
| `transformers`       | HuggingFace NLP Models              |
| `facebook/bart-large-cnn` | Summarization Model              |

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/abdulrahmanhamdi/pdf-summarizer.git
cd pdf-summarizer
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```txt
streamlit
transformers
PyMuPDF
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---

## 📌 Usage Preview

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:640/format:webp/1*MPA0qeIYqLYBy5v4gXuvXA.gif" width="70%">
</p>

---

## 🤖 Model Info

- **Model**: [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn)  
- Handles large texts in chunks (~1000 characters)  
- Each chunk is summarized with `max_length=150`, `min_length=30`  

---

## ⚠️ Limitations

- Scanned image-based PDFs will not work (no text to extract).  
- Model inference may take time for large documents.  
- Only basic preprocessing is applied — enhancements welcome!  

---

## 📄 License

This project is under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

Made with ❤️ by [Abdulrahman Hamdi](https://github.com/abdulrahmanhamdi)

If you found this useful, please ⭐ the repo and share it!
