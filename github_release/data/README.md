# Data

Raw and processed benchmark datasets are intentionally not included in this partial release. Please download the datasets from their original sources and follow the corresponding data-use terms.

For local experiments, place each processed dataset in its own directory:

```text
data/<DATASET>/train.txt
data/<DATASET>/valid.txt
data/<DATASET>/test.txt
```

The files use tab-separated triples in the following format:

```text
head<TAB>relation<TAB>tail
```
