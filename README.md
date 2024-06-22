# **Text-Summarization Report**


---

## Data Collection 
- Searched for suitable dataset to be trained on my hardware <br>
- Selected 'Inshorts News Summary Dataset'
- Successfully loaded the selected dataset , saved that in Data Folder.

## Data Preprocessing and EDA 
- Extracted the required columns from the master dataset 
- Applied nlp preprocessing techniques on the extracted dataset.
- Visualized the data distribution between the input and target column   
- Saved the preprocessed dataset.

## Model Building (Ongoing)

- Selected t5-small model for abstractive summarization
- Prefine tuning results stored at `Summarization_Model/model.ipynb`
- Fine tuned it on my dataset , evaluated results at `Summarization_Model/evaluation.ipynb`

- Working on extractive model
