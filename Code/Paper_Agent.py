import requests
import xml.etree.ElementTree as ET

#gets paper metadata from api enpoints
def search_arxiv(topic, max_results=1):
    base_url = "http://export.arxiv.org/api/query?"
    query = f"search_query=all:{topic}&start=0&max_results={max_results}"

    response = requests.get(base_url + query)
    
    if response.status_code == 200:
        root = ET.fromstring(response.text)
        papers = []

        #said api endpoints
        for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
            title = entry.find("{http://www.w3.org/2005/Atom}title").text
            summary = entry.find("{http://www.w3.org/2005/Atom}summary").text.strip()
            link = entry.find("{http://www.w3.org/2005/Atom}id").text
            pdf_link = None

            for link in entry.findall("{http://www.w3.org/2005/Atom}link"):
                if link.attrib.get("title") == "pdf":  
                    pdf_link = link.attrib["href"]
                    break

            if pdf_link:  # Only add if a PDF link exists
                papers.append({"title": title, "pdf_link": pdf_link, "summary": summary})
            else:
                papers.append({"title": title, "link": link, "pdf_link": None, "summary": summary})
        
        return papers
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []

def get_arxiv_pdf_url(arxiv_link):
    """Convert an arXiv paper link to its direct PDF URL."""
    arxiv_id = arxiv_link.split("/")[-1]  # Extract the arXiv ID (last part of the URL)
    return f"https://arxiv.org/pdf/{arxiv_id}.pdf"