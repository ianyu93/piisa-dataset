# ehrcomplete_icdfiltered

Team Name: Piiilumminators

This dataset contains electronic health records (EHR) with associated ICD-9 codes. It includes the following fields:
- `TEXT`: The text of the medical transcription or health record
- `ICD9_CODE`: A list of codes from the International Classification of Diseases, 9th Revision (ICD-9) - the standard system for classifying diseases and health problems

Link to the dataset: [ricardosantoss/ehrcomplete_icdfiltered](https://huggingface.co/datasets/ricardosantoss/ehrcomplete_icdfiltered)

## How to Download

To download and use this dataset, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required libraries:
-`datasets`
3. Use the following Python code to load the dataset:
```python
from datasets import load_dataset

dataset = load_dataset("ricardosantoss/ehrcomplete_icdfiltered")
```

## Notes 
- This dataset contains sensitive medical information. Ensure you comply with all relevant data protection and privacy regulations when using this dataset.
- The dataset includes train, validation, and test splits, with a total of approximately 48.7k records.