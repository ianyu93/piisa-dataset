# synth-ehr-icd10-llama3-format

Team Name: Piiilumminators

This dataset contains Electronic Health Records (EHR) with corresponding ICD-10 codes. It includes the following fields:
- `ehr_text`: Patient's medical history and clinical information
- `icd_code`: List of codes from the International Statistical Classification of Diseases and Related Health Problems (ICD-10)

Link to the dataset: [generative-technologies/synth-ehr-icd10-llama3-format](https://huggingface.co/datasets/generative-technologies/synth-ehr-icd10-llama3-format)

## How to Download and Use

1. Install required libraries:
`datasets`
`jsonlines`
`polars`
2. Use the following Python code to download and load the dataset:
```python
from datasets import load_dataset

dataset = load_dataset("generative-technologies/synth-ehr-icd10-llama3-format")
```
## Notes
- This dataset contains 379,243 Electronic Health Records.
- ensure compliance with relevant data protection regulations.
- The large size of this dataset (379,243 records) makes it suitable for various machine learning tasks in the medical domain.