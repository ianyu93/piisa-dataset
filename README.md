# Overview

This repository contains the code for the PIISA dataset.

## Setup

### Dev Container

This repository provides `.devcontainer` configuration for VSCode. While not mandatory, it is recommended to use the dev container to develop in this repository.

- [Getting Started with Dev Containers](https://www.youtube.com/watch?v=b1RavPr_878)
- [Documentation](https://code.visualstudio.com/docs/devcontainers/containers)

### Poetry

This repository uses poetry for dependency management. To install the dependencies, run:
```bash
poetry install
```
#### Exporting Requirements

We provide `requirements.txt` for the project for non-Poetry users. To export the requirements to a `requirements.txt` file, run:
```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

### Formatting
This repository uses `black` for formatting. To format the code, run:
```bash
black
```
If running with Poetry, run:
```bash
poetry run black
```
