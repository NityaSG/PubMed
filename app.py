from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    url = "https://pubmed.ncbi.nlm.nih.gov/?term=" + query
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('a', {'class': 'docsum-title'}, limit=1)
    data = []
    for result in results:
        link = "https://pubmed.ncbi.nlm.nih.gov" + result.get('href')
        description = result.text
        data.append({"link": link, "description": description})
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
