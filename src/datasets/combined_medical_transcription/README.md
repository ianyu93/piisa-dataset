# Combined Medical Transcription (medical_transcription_4 + medical_transcription_40)

Team Name: Piiilumminators

This dataset is a combination of two medical transcription datasets. It contains the following field:
- `text`: The text of the medical transcription

The combined dataset consists of 9,998 records in total.

Original datasets:
- [rungalileo/medical_transcription_4](https://huggingface.co/datasets/rungalileo/medical_transcription_4)
- [rungalileo/medical_transcription_40](https://huggingface.co/datasets/rungalileo/medical_transcription_40)

## How to Download and Use

1. Install required libraries: `pip install datasets jsonlines polars`
2. Download the script: `main.py`
3. Run the script: `python main.py`
4. This creates `combined_medical_transcription.jsonl` in your current directory.

## Notes

- This combined dataset contains 9,998 medical transcriptions from two different sources.
- The data contains sensitive medical information. Ensure you comply with all relevant data protection and privacy regulations when using this dataset.