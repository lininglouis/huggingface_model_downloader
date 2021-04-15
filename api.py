from model import HuggingfaceDownloader

def download_hf_model(model_name, output_dir='.'):
    downloader = HuggingfaceDownloader(model_name = model_name, output_dir=output_dir)
    downloader.run()

if __name__ == "__main__":
    pass
    #download_hf_model('bert-base-cased')