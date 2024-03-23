# gill-cc3m

## Prepare data

Download from
[ConceptualCaptions](https://ai.google.com/research/ConceptualCaptions/download):

- `raw/Train_GCC-training.tsv`
- `raw/Validation_GCC-1.1.0-Validation.tsv`

Add header:

```sh
mkdir -p header

cp raw/Train_GCC-training.tsv header/training_00.tsv
sed -i '' -e '1s/^/caption\turl\n/' header/training_00.tsv

cp raw/Validation_GCC-1.1.0-Validation.tsv header/validation_00.tsv
sed -i '' -e '1s/^/caption\turl\n/' header/validation_00.tsv
```

Small dataset to test first:

```sh
cp header/training_00.tsv header/training_01.tsv
sed -i '' -e '100,$d' header/training_01.tsv

cp header/validation_00.tsv header/validation_01.tsv
sed -i '' -e '10,$d' header/validation_01.tsv
```

## Download

Require `img2dataset`, `wandb`:

```sh
uv venv
uv pip install img2dataset wandb
source .venv/bin/activate

# Create an account first
wandb login

img2dataset \
    --url_list header/training_01.tsv \
    --input_format "tsv" \
    --url_col "url" \
    --caption_col "caption" \
    --output_format webdataset \
    --output_folder output/training_01 \
    --processes_count 1 \
    --thread_count 4 \
    --image_size 256 \
    --retries 1 \
    --enable_wandb True \
    --wandb_project "gill-cc3m"

img2dataset \
    --url_list header/validation_01.tsv \
    --input_format "tsv" \
    --url_col "url" \
    --caption_col "caption" \
    --output_format webdataset \
    --output_folder output/validation_01 \
    --processes_count 1 \
    --thread_count 4 \
    --image_size 256 \
    --retries 1 \
    --enable_wandb True \
    --wandb_project "gill-cc3m"
```

## References

- https://github.com/kohjingyu/gill
- https://github.com/ray-ruisun/CC3M-Helper
- https://github.com/rom1504/img2dataset
- https://stackoverflow.com/a/9533736
- https://stackoverflow.com/a/4247319
