# SeeNear NER (Named Entity Recognization)

Our model was developed using Huggingface and Pytorch.  
We fine-tuned the Bert-base model by classifying datasets that can relate to disease in the dataset. 

## Named Entity  
Our model recognizes nine object names. (including 'O' for nothing)  


'O' - Nothing  
'PS_NAME' - Person Name (ex. 이영자)  
'FD_MEDICINE' - Medical Disciplines and Departments (ex. 내과)  
'TR_MEDICINE' - Medical Therapy / Prescription / Diagnosis (ex. 인공호흡)  
'OGG_MEDICINE' - Medical institution / Organization (ex.경희한의원)
'TMM_DISEASE' - Symptom / Disease name (ex. 기침)  
'TM_CELL_TISSUE_ORGAN' - Name of cell / Tissue / Organ (ex. 식도)   
'TMM_DRUG' - Drugs (ex. 근이완제)  
'CV_RELATION' - Realtionship (ex. 아들) 



## Test Our Code

If you go to [This Link](https://huggingface.co/keonju/korean_disease_ner) , you can use our model on the Hugging Face.  

### Using Pytorch
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("keonju/korean_disease_ner")
model = AutoModelForTokenClassification.from_pretrained("keonju/korean_disease_ner")

inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits
predictions = torch.argmax(logits, dim=2)
predicted_token_class = [model.config.id2label[t.item()] for t in predictions[0]]
print(predicted_token_class)
```

### Using Huggingface
```python
from transformers import pipeline

classifier = pipeline("ner", model="keonju/korean_disease_ner") 
```

- - -
</br>

# Start Guide

**Requirments**

What you need to build and run this application:   
- Python 3.10
- MySQL 8.0.26

**Installation**
```
$ git clone https://github.com/GDSC-seeNear/NER.git
```
If Linux
```
$ sudo apt-get install git-lfs
$ git lfs install
```

If Mac Os
```
$ brew install git-lfs
$ git lfs install
```

```
$ pip install -r requirements.txt
$ git clone https://huggingface.co/keonju/korean_disease_ner
```


**Run**
```
$ uvicorn main:app —host 0.0.0.0 --port 8080
```
</br>


### Reference

1. Fine-Tuned Model  
NER model fine-tuned [klue/bert-base](https://huggingface.co/klue/bert-base) for NER Task.  

2. Dataset  
Choose Named Entity in [모두의 말뭉치 - 개체명 분석 말뭉치 2020](https://corpus.korean.go.kr/request/corpusRegist.do)
