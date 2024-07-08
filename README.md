# **Text-Summarization Report**


---

## Data Collection 
- Searched for suitable dataset to be trained on my hardware <br>
- Selected 'Inshorts News Summary Dataset'
- Successfully loaded the selected dataset , saved that in Data Folder.

## Data Preprocessing and EDA 
- Extracted the required columns from the master dataset. 
- Applied nlp preprocessing techniques on the extracted dataset.
- Visualized the data distribution between the input and target column.
- Saved the preprocessed dataset.

## Model Building 

### Abstractive Approach 

- Selected t5-small model for abstractive summarization.
- Prefine tuning results stored at `Summarization_Model/model.ipynb` .
- Fine tuned it on my dataset , evaluated results at `Summarization_Model/evaluation.ipynb` 
- Model Size after fine tuning n ~ 800 MB .

- Final rogue scores after fine tuning are as follows:
   ` Rouge-1: 0.42 `
   ` Rouge-2: 0.22 `
   ` Rouge-L: 0.34 `

### Extractive Approach
- Performed Extractive Summarization pre-processing on the dataset by removing stopwords, punctuation, and special characters and white spaces.
- Selected Text Rank Algorithm for extractive summarization .
- Implemented through py summa library.

- Rouge scores for extractive summarization are as follows: (for 20% ratio of input text vs summary length)
   ` Rouge-1: 0.25 `
   ` Rouge-2: 0.12 `
   ` Rouge-L: 0.19 `

- Optimized ratio Length of summary to input text to get better results.

## Model Interface (Ongoing)

- Built Model Interface using streamlit library.
- Implemented in `Model_Interface/app.py`.
- Visualized Abstract and Extractive Summarization results on the interface.