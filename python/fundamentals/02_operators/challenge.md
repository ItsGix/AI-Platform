# Challenge

## Objective

Create a Python script that determines whether your AI cluster is **ready** based on a set of conditions.

## Variables

Create the following variables:

* `workers`
* `control_plane`
* `gpu_available`
* `ram`

## Requirements

Your script should check that:

* There is **at least one** control plane node.
* There are **at least two** worker nodes.
* A GPU is available.
* There is **at least 32 GB** of RAM.

## Expected Output

If **all** of the above conditions are met, print:

```text
Cluster Ready
```

Otherwise, print:

```text
Cluster Not Ready
```

## Learning Goal

This challenge is designed to help you practise:

* Comparison operators (`>=`, `==`)
* Logical operators (`and`)
* Boolean values (`True` / `False`)
* Using the result of multiple conditions to make a decision with an `if` statement
