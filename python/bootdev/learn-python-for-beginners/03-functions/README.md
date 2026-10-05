# Chapter 03 - Functions

## Status

Complete

## Lessons Reviewed

- Defining and calling functions
- Function execution order
- Multiple parameters
- Printing versus returning
- Where to declare functions
- Organising a program around `main()`
- Small conversion exercises
- Functions that return `None`
- Multiple return values
- Parameters versus arguments
- Default parameter values
- Exercises combining calculations, strings, and multiple returns

## Core Idea

A function is a named, reusable block of code that performs one focused task.
It can receive values from its caller, work with them, and return a result.

```python
def calculate_required_cpu(replicas, cpu_per_replica):
    return replicas * cpu_per_replica


required_cpu = calculate_required_cpu(3, 0.5)
print(required_cpu)  # 1.5
```

The `def` statement creates the function. Its indented body runs only when the
function is called. In the example, `3` and `0.5` are supplied to the function,
the multiplication is evaluated, and `1.5` is returned to the caller.

## Parameters and Arguments

These terms describe the two sides of a function call:

| Term | Meaning | Example |
| --- | --- | --- |
| Parameter | A name in the function definition | `replicas` |
| Argument | A value supplied when calling the function | `3` |

```python
def build_endpoint(service_name, port):
    return f"http://{service_name}:{port}"


endpoint = build_endpoint("model-api", 8080)
```

Here, `service_name` and `port` are parameters. `"model-api"` and `8080` are
arguments.

With positional arguments, order matters. Reversing the arguments would bind
each value to the wrong parameter. Descriptive names and a small number of
parameters make calls easier to understand.

## Returning Values

`return` sends a value back to the caller and immediately ends the current
function call:

```python
def available_replicas(desired, unavailable):
    return desired - unavailable
```

The caller can store the result, pass it to another function, or use it in a
larger expression:

```python
ready = available_replicas(5, 2)
message = f"Ready replicas: {ready}"
```

Keeping calculations inside functions and presentation at the edge of the
program makes the logic easier to reuse and test.

## Printing Is Not Returning

`print()` displays text in the console. `return` makes a result available to
the caller. They solve different problems.

| Operation | Purpose | Result available to caller? |
| --- | --- | --- |
| `print(value)` | Show information to a person | No |
| `return value` | Hand data back to calling code | Yes |

```python
def get_cluster_name():
    return "homelab-k3s"


cluster_name = get_cluster_name()
print(cluster_name)
```

If `get_cluster_name()` printed the name instead, `cluster_name` would receive
`None`. Debug prints can be useful while investigating code, but reusable
functions should normally return their useful result.

## Functions That Return `None`

Every Python function returns a value. If execution reaches the end without
an explicit value, the result is `None`.

These functions have the same return value:

```python
def first_example():
    return None


def second_example():
    return


def third_example():
    pass
```

`pass` is a placeholder statement. It lets an otherwise empty function body
remain syntactically valid, but it does no work.

An unexpected `None` often means a function printed a value or reached its end
when it was meant to return a result.

## Multiple Return Values

A function can appear to return several values separated by commas:

```python
def calculate_capacity(replicas, cpu_per_replica, memory_per_replica_gb):
    total_cpu = replicas * cpu_per_replica
    total_memory_gb = replicas * memory_per_replica_gb
    return total_cpu, total_memory_gb


cpu, memory_gb = calculate_capacity(3, 0.5, 2)
```

Python packages the returned values into one tuple, then unpacking assigns its
items to separate names. Position still matters, and the number of receiving
variables must match the number of returned items.

## Default Parameter Values

A default makes an argument optional for callers:

```python
def build_service_name(component, namespace="ai-platform"):
    return f"{namespace}/{component}"


default_name = build_service_name("inference-api")
custom_name = build_service_name("inference-api", "testing")
```

The first call uses `"ai-platform"`; the second overrides it with `"testing"`.
Parameters without defaults must come before parameters with defaults:

```python
def valid(required_value, optional_value="default"):
    return required_value, optional_value
```

Defaults are most useful when one value is genuinely the common case. They
should not hide information that callers need to choose deliberately.

## Definition and Execution Order

Python executes a file from top to bottom. A function must have been defined
before execution reaches a call to it.

Defining a function does not run its body. This allows one function to refer
to another function defined later in the file, provided both definitions have
executed before the first call is made.

```python
def main():
    print(create_status("model-api"))


def create_status(service_name):
    return f"{service_name}: ready"


main()
```

A common real-world entry-point pattern is:

```python
if __name__ == "__main__":
    main()
```

The guard runs `main()` when the file is executed directly, while allowing its
functions to be imported elsewhere without starting the program automatically.

## Designing Useful Functions

A useful function normally:

- has one clear responsibility;
- uses a verb-based name that describes its action;
- receives the information it needs through parameters;
- returns data instead of depending on console output; and
- avoids surprising changes outside its own body.

Small functions can be composed: one calculates data, another formats it, and
`main()` coordinates the overall flow.

## Original Applied Example

This example applies parameters, positional arguments, default values,
multiple returns, f-strings, and a program entry point to an infrastructure
capacity report:

```python
def calculate_capacity(replicas, cpu_per_replica, memory_per_replica_gb):
    total_cpu = replicas * cpu_per_replica
    total_memory_gb = replicas * memory_per_replica_gb
    return total_cpu, total_memory_gb


def create_capacity_report(service_name, replicas=1):
    total_cpu, total_memory_gb = calculate_capacity(replicas, 0.5, 2)
    return (
        f"Service: {service_name}\n"
        f"Replicas: {replicas}\n"
        f"Requested CPU: {total_cpu} cores\n"
        f"Requested memory: {total_memory_gb} GiB"
    )


def main():
    print(create_capacity_report("embedding-api", 3))
    print()
    print(create_capacity_report("health-check"))


if __name__ == "__main__":
    main()
```

Expected output:

```text
Service: embedding-api
Replicas: 3
Requested CPU: 1.5 cores
Requested memory: 6 GiB

Service: health-check
Replicas: 1
Requested CPU: 0.5 cores
Requested memory: 2 GiB
```

The calculation function returns reusable data and knows nothing about output
formatting. The report function turns that data into text. `main()` decides
what to run and is the only part responsible for printing.

## Common Mistakes

- Forgetting the parentheses when calling a function.
- Calling a function before Python has executed its definition.
- Incorrectly indenting the function body.
- Printing a result when the caller needs it returned.
- Forgetting to store or use a returned value.
- Assuming a function without `return` produces a useful result instead of
  `None`.
- Passing positional arguments in the wrong order.
- Unpacking a different number of names from the values returned.
- Placing a required parameter after a parameter with a default.
- Writing statements after `return` and expecting them to run.

## Quick Self-Check

1. What is the difference between a parameter and an argument?
2. Why can a function print the correct text but still return `None`?
3. What happens to statements after a `return` is executed?
4. Why does order matter for positional arguments and unpacked return values?
5. When is a default parameter appropriate?
6. Why is calculation logic easier to reuse when it returns data rather than
   printing it?

## Reflection

This chapter changed the focus from individual statements to reusable program
structure. Functions create explicit boundaries: parameters define the input,
the body performs one job, and the return value defines the output. Separating
calculation, formatting, and orchestration is directly useful in infrastructure
automation, where the same logic may be called from a script, a test, an API,
or a scheduled job.

## Completed

Chapter 03 completed on 2026-10-05.
