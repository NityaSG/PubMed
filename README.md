
# PubMed Search Results API using Flask

This is a simple Flask web server that fetches and returns PubMed search results based on a given query.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Dependencies](#dependencies)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/) (at least version 3.6)
- [pip](https://pip.pypa.io/en/stable/installing/) (Python Package Installer)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/pubmed-search-api-flask.git
   cd pubmed-search-api-flask
   ```

2. Install the project dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask server:

   ```sh
   python app.py
   ```

   The server will start and listen on port 5000 by default.

2. Open a web browser or use a tool like [curl](https://curl.se/) to access the API endpoint:

   ```sh
   curl http://localhost:5000/search?query=your_query_here
   ```

   Replace `your_query_here` with the desired search query.

3. The server will respond with a JSON object containing information about the top search result.

## API Endpoint

The API endpoint for retrieving PubMed search results is:

```
GET /search?query=<your_query>
```

Replace `<your_query>` with your desired search query.

## Dependencies

- [Flask](https://flask.palletsprojects.com/): Web framework for creating the server.
- [requests](https://docs.python-requests.org/en/latest/): HTTP library for making requests.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): Library for parsing HTML content.

## License

This project is licensed under the [MIT License](LICENSE).
