# MedicalTranscriptions

Team Name: Piiilumminators

This dataset contains medical transcriptions with the following fields:
- `description`: A short description of the patient
- `medical_specialty`: The specialty of the doctor
- `sample_name`: The name of the test or surgery
- `transcription`: The full text of the medical transcription
- `keywords`: Medical-related key terms

Link to the dataset: [tchebonenko/MedicalTranscriptions](https://huggingface.co/datasets/tchebonenko/MedicalTranscriptions)

## How to Download and Use

1. Install required libraries:
`datasets`
`jsonlines`
`polars`
2. Use the following Python code to download and load the dataset:
```python
from datasets import load_dataset

dataset = load_dataset("tchebonenko/MedicalTranscriptions")
```
## Notes

- This dataset contains sensitive medical information. Ensure compliance with relevant data protection and privacy regulations when using this dataset.
- The dataset contains 4,999 medical transcriptions. Always verify the current size upon loading, as it may be subject to updates.