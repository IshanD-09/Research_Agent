from flask import Flask, render_template, request, jsonify
import templates
import Paper_Agent  # Your existing research agent module
import Paper_Scraper
import RAG
import LLM
from flask_cors import CORS  # To allow frontend requests
from uuid import uuid4

app = Flask(__name__)
CORS(app)  # Allows JavaScript from different domains to access API

# 🏡 Serve the homepage
@app.route('/')
def home():
    return render_template('index.html')  # Loads templates/index.html

# 🔍 API to search for research papers
@app.route('/search', methods=['GET'])
def search_papers():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "No topic provided"}), 400

    # Get research papers from Paper_Agent
    papers = Paper_Agent.search_arxiv(query)  # Replace with your function
    
    if papers[0]['pdf_link']:
        # Format response
        results = [
            {"title": paper["title"], "link": papers[0]['pdf_link']}
            for paper in papers
        ]
    else:
        results = [
            {"title": paper["title"], "link": papers[0]['link']}
            for paper in papers
        ]

    text = Paper_Scraper.scrape_paper(results[0]['link'])
    texts = RAG.text_splitter.split_text(text)
    uuids = [str(uuid4()) for _ in range(len(texts))]
    RAG.vector_store.add_texts(texts=texts, ids=uuids)

    if papers[0]['pdf_link']:
        info = [
            {"title": "Summary: ",  "summary": LLM.summarize(RAG.vector_store.similarity_search_by_vector(embedding=RAG.embeddings.embed_query(request.args.get('query')), k=4))}
        ]
    else:
        info = [
            {"title": "Summary: ",  "summary": str(papers[0]['summarize'])}
        ]

    return jsonify({
        'paper': results[0],
        'info': info[0]
    })
if __name__ == '__main__':
    app.run(debug=True)
