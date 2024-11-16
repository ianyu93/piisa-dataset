# Healthcare Dataset

Team Name: Piiilumminators

This dataset contains healthcare records with the following fields:
- `Age`: Patient's age at admission (in years)
- `Gender`: Patient's gender ("Male" or "Female")
- `Blood Type`: Patient's blood type (e.g., "A+", "O-")
- `Medical Condition`: Primary diagnosis (e.g., "Diabetes", "Hypertension")
- `Date of Admission`: Date of patient's admission
- `Doctor`: Name of the attending doctor
- `Hospital`: Name of the healthcare facility
- `Insurance Provider`: Patient's insurance company
- `Billing Amount`: Cost of healthcare services (float)
- `Room Number`: Patient's room number during stay
- `Admission Type`: Type of admission ("Emergency", "Elective", or "Urgent")
- `Discharge Date`: Date of patient's discharge
- `Medication`: Prescribed or administered medication
- `Test Results`: Outcome of medical tests ("Normal", "Abnormal", or "Inconclusive")

Link to the dataset: [prasad22/healthcare-dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset?resource=download)

## How to Download and Use

1. Ensure you have a Kaggle account and have set up the Kaggle API:
   - Create a Kaggle account if you don't have one
   - Go to 'Account' settings on Kaggle
   - Scroll to 'API' section and click 'Create New API Token'
   - This will download a `kaggle.json` file
   - Place this file in `~/.kaggle/` on Linux/macOS or `C:\Users\<Windows-username>\.kaggle\` on Windows
2. Install required libraries:
`kaggle`
`jsonlines`
`polars`
3. Use the following Python code to download and load the dataset:
```python
import kaggle
import pandas as pd
import os

kaggle.api.dataset_download_files('prasad22/healthcare-dataset', path='.', unzip=True)

df = pd.read_csv('healthcare_dataset.csv')
```

## Notes

- This dataset contains 55,500 healthcare records.
- ensure compliance with relevant data protection regulations.
- The large size of this dataset (55,500 records) makes it suitable for various machine learning tasks in the healthcare domain.