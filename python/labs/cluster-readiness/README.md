# Cluster Readiness

## Purpose

This lab evaluates whether an AI cluster meets a small set of readiness
requirements and prints a clear status.

A cluster is considered ready when:

- At least one control-plane node is available.
- At least two worker nodes are available.
- A GPU is available.
- At least 32 GB of RAM is available.

## Concepts Practised

- Comparison operators such as `>=`
- Boolean values
- Combining conditions with `and`
- Multi-line expressions and parentheses
- `if`/`else` control flow
- Conditional expressions

## Run

From the repository root:

```bash
python3 python/labs/cluster-readiness/cluster_readiness.py
```

With the current example values, the program prints:

```text
Cluster Ready
Cluster Ready
```

The result is intentionally printed once through an `if` statement and once
through a conditional expression so both approaches can be compared.

## Learning Notes

This exercise demonstrates how several individual checks can be combined into
one meaningful decision. A boolean variable does not need to be compared with
`True`; it can be used directly in the expression. Changing the input values
and predicting the result before running the script is a useful way to practise
reasoning about compound conditions.

In production, readiness would be based on live data and would normally return
structured diagnostic details rather than a single hard-coded message.
