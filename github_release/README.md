# CMCA-KGC

Core implementation of **CMCA-KGC**, a knowledge graph completion framework with channel mixing and multi-scale community awareness.

## Public release

This repository contains selected public reference components used in CMCA-KGC:

- a compact channel-mixing block;
- an interface for externally prepared community features;
- a lightweight description of the expected dataset layout.

The complete multi-scale community construction, data preparation, training,
validation, and experimental configuration files are not included in this
partial release. They will be organized and released in a later version after
the paper review process is completed.

## Directory structure

```text
github_release/
├── model/
│   └── channel_mixing.py
├── data/
│   └── README.md
└── README.md
```

## Dataset layout

The complete datasets are not redistributed here. Please obtain each benchmark from its original source and place the processed files under a dataset directory containing:

```text
train.txt
valid.txt
test.txt
```

Each line should contain one tab-separated triple:

```text
head<TAB>relation<TAB>tail
```
