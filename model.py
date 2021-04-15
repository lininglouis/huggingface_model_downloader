import requests_html
from requests_html import HTMLSession
from utils import download, mkdir_if_not_exists

class HuggingfaceDownloader():
    def __init__(self, model_name, output_dir='.'):
        self.model_name = model_name
        self.get_html()
        self.extract_file_urls()
        self.output_dir = f'{output_dir}/{self.model_name}'

    def get_html(self):
        session = HTMLSession()
        url = f'https://huggingface.co/{self.model_name}/tree/main'
        self.html = session.get(url).html

    def extract_file_urls(self):
        web_site = f'https://huggingface.co'
        file_mid_name =  f'/{self.model_name}/resolve'
        self.file_urls = []
        for a in self.html.find('a'):
            href = a.attrs['href']
            if href.startswith(file_mid_name):
                full_url = web_site + href 
                self.file_urls.append(full_url)

    def run(self):
        mkdir_if_not_exists(self.output_dir)
        for file_url in self.file_urls:
            download(file_url, self.output_dir)


