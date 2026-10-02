# Chapter 02 - Variables

## Status

Complete

## Lessons Reviewed

- Variables
- Variables Vary
- Math
- Negative Numbers
- Comments
- Variable Names
- Basic Variable Types
- F-Strings in Python
- NoneType Variables and quiz
- Dynamic Typing
- Math With Strings
- Multi-Variable Declaration
- Spellbook review exercise
- Character Report practice

## Core Idea

A variable is a name bound to a value. The name lets the program reuse the
value, and assigning to the same name again changes which value that name
refers to.

```python
node_count = 3
print(node_count)  # 3

node_count = 4
print(node_count)  # 4
```

`=` is the assignment operator. It assigns the value on the right to the name
on the left; it does not mean “is equal to” in the mathematical sense.

## Naming Variables

Python variable names cannot contain spaces. Prefer descriptive `snake_case`
names: lowercase words separated by underscores.

```python
replica_count = 3
cluster_region = "eu-west"
maintenance_enabled = False
```

Common naming styles:

| Style | Example | Typical use |
| --- | --- | --- |
| snake case | `active_node_count` | Python variables and functions |
| camel case | `activeNodeCount` | Common in JavaScript and Java |
| Pascal case | `ActiveNodeCount` | Common for class/type names |

Good names explain intent. `retry_limit` communicates more than `x`, and a
name should continue to describe its value after reassignment.

## Basic Value Types

The chapter introduced four common scalar types:

| Type | Meaning | Example |
| --- | --- | --- |
| `str` | text | `service_name = "inference-api"` |
| `int` | whole number | `replicas = 3` |
| `float` | number with a decimal part | `cpu_limit = 1.5` |
| `bool` | `True` or `False` | `healthy = True` |

Strings must be quoted. Numbers and booleans must not be quoted when their
numeric or logical behaviour is required. Boolean values are capitalised:
`True` and `False`.

Use `type()` when checking a value during learning or debugging:

```python
replicas = 3
print(type(replicas))          # <class 'int'>
print(type(replicas).__name__) # int
```

## Arithmetic and Order of Operations

Python supports the familiar arithmetic operators:

| Operation | Operator | Example |
| --- | --- | --- |
| addition | `+` | `total = ready + pending` |
| subtraction | `-` | `remaining = capacity - used` |
| multiplication | `*` | `memory_mb = pods * memory_per_pod_mb` |
| division | `/` | `average = total / count` |

Negative values use a leading minus sign:

```python
temperature_delta = -4
```

Parentheses make evaluation order explicit and prevent subtle calculation
errors:

```python
run_one_ms = 97
run_two_ms = 92
run_three_ms = 106
run_four_ms = 105

average_ms = (run_one_ms + run_two_ms + run_three_ms + run_four_ms) / 4
print(round(average_ms))  # 100
```

Without the parentheses, division would happen before most of the additions.

## Strings: Interpolation and Concatenation

An f-string inserts values into text. Prefix the opening quote with `f` and put
each expression inside braces:

```python
service = "vector-db"
replicas = 3
message = f"{service} is running {replicas} replicas."
```

F-strings are usually clearer than joining many pieces with `+`. String
concatenation still works when every operand is a string:

```python
prefix = "region="
region = "eu-west"
label = prefix + region
```

Concatenating a string directly with an integer raises a `TypeError`. Prefer an
f-string, or explicitly convert the number with `str()` when concatenation is
truly needed.

## `None`: No Value Yet

`None` represents the absence of a value. It is useful when a result has not
been determined or supplied yet.

```python
deployment_id = None

# Later, after a deployment is created:
deployment_id = "deploy-7f31"
```

`None` is different from `0`, `False`, `""`, and the string `"None"`. Test for
it with `is None` or `is not None`:

```python
if deployment_id is None:
    print("Deployment has not started.")
```

## Dynamic Typing

Python is dynamically typed: a name can be rebound to a value of another type.
This is valid syntax:

```python
port = 8080
port = "8080"
```

It is usually a poor design choice because later code can no longer rely on
what the name contains. Keep one clear meaning and type per variable when
possible:

```python
port = 8080
port_text = "8080"
```

Statically typed languages generally reject an incompatible assignment before
the program runs. Python instead requires care, tests, and—later in the
course—optional type hints to make expectations clear.

## Multiple Assignment

Related values can be unpacked into several variables on one line:

```python
service_name, desired_replicas, port = "model-api", 3, 8080
```

The number of names and values must match. Use this only when the values form a
clear group; separate assignments are often easier to scan and modify.

## Comments and Documentation

`#` begins a comment that continues to the end of the line:

```python
# Keep one replica available while a node is being drained.
minimum_available = 1
```

Comments should explain why a decision exists, not merely repeat the code.

Triple-quoted text is not technically a multi-line comment. It creates a
multi-line string literal. When placed first in a module, class, or function it
becomes a docstring; an otherwise unused string is still parsed as code. Use
`#` for comments and docstrings for documenting modules, classes, and
functions.

## Original Applied Example

This small status report combines naming, types, arithmetic, `None`, booleans,
f-strings, and multiple assignment in an AI-platform scenario:

```python
service_name = "embedding-api"
desired_replicas, ready_replicas = 4, 3
cpu_per_replica = 0.5
last_error = None

missing_replicas = desired_replicas - ready_replicas
requested_cpu = desired_replicas * cpu_per_replica
is_healthy = False

print(f"Service: {service_name}")
print(f"Ready: {ready_replicas}/{desired_replicas}")
print(f"Requested CPU: {requested_cpu} cores")
print(f"Healthy: {is_healthy}")
print(f"Last error: {last_error}")
```

Expected output:

```text
Service: embedding-api
Ready: 3/4
Requested CPU: 2.0 cores
Healthy: False
Last error: None
```

## Common Mistakes

- Putting quotes around numbers or booleans and accidentally creating strings.
- Writing `true`, `false`, or `none` instead of `True`, `False`, and `None`.
- Forgetting the `f` prefix on a string that contains `{expressions}`.
- Changing a variable to an unrelated type halfway through a program.
- Omitting parentheses when calculating an average.
- Confusing `None` with the string `"None"`.
- Adding strings and numbers with `+` without an explicit conversion.
- Using comments to restate obvious code instead of explaining intent.

## Quick Self-Check

1. What value and type does a variable hold after it is reassigned?
2. Why is `deployment_id is None` preferable to comparing it with `"None"`?
3. Where should parentheses go when calculating an average?
4. When is an f-string clearer than concatenation?
5. Why can changing a variable's type make a program harder to maintain?

## Reflection

This chapter moved from printing fixed values to modelling changing program
state. The most useful habits are choosing descriptive names, preserving a
variable's meaning and type, making arithmetic order explicit, and formatting
output with f-strings. These fundamentals map directly to infrastructure code,
where variables describe desired state, observed state, resource quantities,
feature flags, and values that may not yet be known.

## Completed

Chapter 02 completed on 2026-10-02.
