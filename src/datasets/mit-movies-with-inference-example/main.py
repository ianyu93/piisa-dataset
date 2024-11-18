import polars as pl
import jsonlines

METADATA = {
    "dataset_name": "mit-movies-with-inference",
    "dataset_link": "https://huggingface.co/datasets/rungalileo/MIT_Movies_w_inference",
}

TRAIN_SPLIT = "data/train-00000-of-00001-e5c52d24927dabc6.parquet"
VALIDATION_SPLIT = "data/validation-00000-of-00001-0b2e4e56a7721170.parquet"
INFERENCE_EXAMPLE_SPLIT = (
    "data/inference_example-00000-of-00001-0c93fb2386c86578.parquet"
)
SPLITS = {
    "train": TRAIN_SPLIT,
    "validation": VALIDATION_SPLIT,
    "inference_example": INFERENCE_EXAMPLE_SPLIT,
}


def main():
    for split_name, split_path in SPLITS.items():
        df = pl.read_parquet(
            "hf://datasets/rungalileo/MIT_Movies_w_inference/" + split_path
        )


        records = df.select(["id", "text"]).iter_rows(named=True)

        with jsonlines.open(
            f"{METADATA['dataset_name']}-{split_name}.jsonl", "w"
        ) as writer:
            for record in records:
                writer.write(
                    {"meta": METADATA, "id": record["id"], "text": record["text"]}
                )


if __name__ == "__main__":
    main()
