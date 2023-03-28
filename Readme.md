# SeeNear NER (Named Entity recognization)

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

