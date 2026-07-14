# Week 1 - Module 2 Reflection

## What did I learn?

This module introduced Python operators and how they are used to compare values and make decisions within a program. I learnt the difference between arithmetic, comparison, logical, assignment, membership and identity operators, along with how operator precedence affects calculations.

The most important concept for me was understanding that comparison operators return either `True` or `False`, and that logical operators such as `and` can combine multiple conditions into a single result.

## Which operator did I understand immediately?

The arithmetic operators (`+`, `-`, `*`, `/`) were straightforward because they behave similarly to normal mathematics.

Comparison operators such as `>=`, `<=` and `==` also made sense as they simply evaluate to `True` or `False`.

## Which operator was the most challenging?

Logical operators took the longest to fully understand because I needed to think about how multiple conditions are evaluated together.

I also learnt that a Boolean variable such as `gpu_available` does not need to be written as `gpu_available == True`; simply writing `gpu_available` is the preferred Python style.

## Practical Exercise

I created a small example that checks whether my AI cluster is considered "ready" by evaluating:

* At least two worker nodes
* One control plane node
* GPU availability
* A minimum amount of RAM

I then stored the result in a `cluster_ready` Boolean variable before using it within an `if` statement.

For additional practice, I also used Python's conditional (ternary) expression to create a `status` variable.

## How could I use this in AI Platform Engineering?

These concepts are directly applicable to infrastructure automation.

Examples include:

* Checking whether a Kubernetes cluster is healthy.
* Verifying enough worker nodes are online before deploying workloads.
* Confirming GPU resources are available before starting AI models.
* Validating system resources before running automation scripts.
* Making deployment decisions based on multiple infrastructure checks.

## Reflection

This module helped me understand how Python evaluates conditions rather than simply executing instructions. I found it useful to intentionally change values and predict whether the result would be `True` or `False` before running the program.

Being able to reason through these conditions will be important when I begin writing automation scripts that make decisions based on the state of infrastructure.

## Confidence Rating

**8.5/10**

I feel confident using comparison and logical operators and understand how they work together. I would like a little more practice with more complex conditions, but I feel ready to move on to Module 3.
