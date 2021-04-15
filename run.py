from model import HuggingfaceDownloader
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model_name', required=True)
parser.add_argument('--output_dir', default='.')
args = parser.parse_args()

downloader = HuggingfaceDownloader(model_name = args.model_name, output_dir=args.output_dir)
downloader.run()
