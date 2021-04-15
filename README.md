## Environments and Install
python 3.7
pip install -r requirements.txt

## Examples
```
# download to local directory 
python run.py --model_name 'bert-base-chinese'   

# download to some specified directory
python run.py --model_name 'bert-base-chinese'  --output_dir 'Some Directory'
```


## Tested Models
three models has been tested using this script
model_name = 'bert-base-chinese' 
model_name = 'hfl/chinese-roberta-wwm-ext'
model_name = 'bert-base-cased'