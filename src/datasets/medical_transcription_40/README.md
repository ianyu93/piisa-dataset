# medical_transcription_40

Team Name: Piiilumminators

This dataset contains medical transcriptions. It includes the following field:
- `text`: The text of the medical transcription

Link to the dataset: [rungalileo/medical_transcription_40](https://huggingface.co/datasets/rungalileo/medical_transcription_40)

## How to Download

To download and use this dataset, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required libraries:
`datasets`
`jsonlines`
`polars`
3. Use the following Python code to load the dataset:
```python
from datasets import load_dataset

dataset = load_dataset("rungalileo/medical_transcription_40")
```

## Notes

- This dataset contains medical information. Ensure you comply with all relevant data protection and privacy regulations when using this dataset.
- The dataset contains a total of 5,000 medical transcriptions, split into 4,500 for training and 500 for testing.