import os
import requests
from PyPDF2 import PdfReader


def scrape_paper(paper_url: str, mock: bool = True):
  #scrapes paper for info
  response = requests.get(paper_url)
  with open('paper.pdf', 'wb') as f:
    f.write(response.content)
  reader = PdfReader('paper.pdf')
  text = ""
  for page in reader.pages:
    text += page.extract_text()
  return text

#   if mock:
#     paper_url = 'https://arxiv.org/pdf/1609.04747'
#     response = requests.get(paper_url)
#     with open('paper.pdf', 'wb') as f:
#       f.write(response.content)
#     reader = PdfReader('paper.pdf')
#     text = ""
#     for page in reader.pages:
#       text += page.extract_text()
#     return text

