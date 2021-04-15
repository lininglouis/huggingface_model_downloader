## Motivation
Hugginface provide some nice models on its website, and transformer library can help you automatically download them to your machine when you import the model. But sadly, the downloaded model losts its origin name, and it is not easy to load those model from local.

One way to get the model with names is to visit its webpage like [this](https://huggingface.co/bert-base-chinese/tree/main). But you have to click each file and download. Hence, I wrote this script to parse that webpage and download models all together automatically.

## Environments and Install
The environment is python 3.7

To install the necessary libraries, please 
```
pip install -r requirements.txt
```

## How to download ?
```
# download to local directory 
python run.py --model_name 'bert-base-cased'  

# download to some specified directory
python run.py --model_name 'bert-base-cased'  --output_dir 'Some Directory'
```


## Tested Models
three models has been tested for downloading using this script
```
python run.py --model_name 'bert-base-cased'  
python run.py --model_name 'hfl/chinese-roberta-wwm-ext'  
python run.py --model_name 'bert-base-chinese'  
```
