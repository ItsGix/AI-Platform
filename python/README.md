# Python

This directory documents my Python learning and the original programs I build
to apply it to infrastructure, platform engineering, and AI operations.

## Structure

### Boot.dev learning notes

[`bootdev/`](bootdev/) contains chapter notes from the Boot.dev DevOps Engineer
path. The notes explain concepts in my own words and do not contain copied
course solutions.

### Applied labs

[`labs/`](labs/) contains small, original programs that turn learning concepts
into infrastructure-focused exercises.

| Lab | Concepts practised |
| --- | --- |
| [Infrastructure Status Report](labs/infrastructure-status/) | Variables, scalar data types, f-strings, and readable terminal output |
| [Cluster Readiness](labs/cluster-readiness/) | Comparisons, boolean logic, conditionals, and operator precedence |

## Approach

The repository separates structured learning from independent application:

1. Learn the concept through Boot.dev.
2. Record concise notes in `bootdev/`.
3. Apply the concept in an original program under `labs/`.
4. Grow useful ideas into larger projects when their scope justifies it.

Each lab should explain its purpose, list the concepts it demonstrates, and
include instructions for running it. Dependencies and tests will live with the
project that needs them instead of being represented by empty placeholders.

## Running the labs

From the repository root:

```bash
python3 python/labs/infrastructure-status/status_report.py
python3 python/labs/cluster-readiness/cluster_readiness.py
```

The current labs use only the Python standard library.
