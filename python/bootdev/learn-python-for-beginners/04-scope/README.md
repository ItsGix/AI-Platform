# Chapter 04 - Scope

## Status

Complete

## Lessons Reviewed

- Scope
- Local function scope
- Global scope
- Scope quiz

## Core Idea

Scope describes where a name is available in a program. A variable created
inside a function belongs to that function's local scope. A variable created
at the top level of a file belongs to the module's global scope.

```python
def calculate_available_nodes(total_nodes, unavailable_nodes):
    available_nodes = total_nodes - unavailable_nodes
    return available_nodes


ready_nodes = calculate_available_nodes(4, 1)
print(ready_nodes)  # 3
```

The parameters `total_nodes` and `unavailable_nodes`, along with the
`available_nodes` variable, exist only inside the function call. The returned
value crosses the scope boundary and is assigned to the global name
`ready_nodes`.

## Local Function Scope

Function parameters and variables assigned inside a function are local to
that function:

```python
def build_service_address(service_name, port):
    address = f"{service_name}:{port}"
    return address
```

The names `service_name`, `port`, and `address` are available while the
function runs. Trying to use `address` outside the function without returning
it causes a `NameError`:

```python
def build_service_address(service_name, port):
    address = f"{service_name}:{port}"


build_service_address("inference-api", 8080)
print(address)  # NameError: name 'address' is not defined
```

Each function call gets its own local values. This isolation allows the same
function to be reused without one call overwriting another call's local state.

## Global Scope

A name assigned at the top level of a Python file is global to that module.
Functions in the same module can read it:

```python
platform_name = "homelab-k3s"


def create_platform_label(component):
    return f"{platform_name}/{component}"
```

The function can read `platform_name` because the name exists in its parent
global scope. This does not mean a function can access every variable in the
program: it cannot see local variables belonging to other functions.

At this stage, a useful simplified name lookup model is:

1. Look in the current function's local scope.
2. Look in the module's global scope.
3. Look among Python's built-in names, such as `print`.

Python also supports enclosing scopes for nested functions, which can be
explored when closures and more advanced function design are introduced.

## Moving Data Across Scope Boundaries

Parameters carry data into a function. Return values carry results back out:

```python
def calculate_requested_memory(replicas, memory_per_replica_gb):
    requested_memory_gb = replicas * memory_per_replica_gb
    return requested_memory_gb


total_memory_gb = calculate_requested_memory(3, 2)
```

This is clearer than expecting the function to find and modify unrelated
global variables. The function declares its required inputs and gives the
caller control over the result.

## Local Names Can Shadow Global Names

If a function creates a local name that matches a global name, the local value
is used inside that function:

```python
environment = "production"


def show_environment():
    environment = "testing"
    return environment


print(show_environment())  # testing
print(environment)         # production
```

The local assignment does not replace the global value. Reusing the same name
can make code difficult to reason about, so distinct and descriptive names
are normally preferable.

Python has a `global` statement that permits a function to reassign a global
name, but shared mutable state creates hidden dependencies. Passing values in
and returning values out is usually the safer design.

## Choosing Appropriate Globals

Module-level values are useful when they describe stable configuration or
constants shared throughout a file. Python convention writes constant names
in uppercase:

```python
PLATFORM_NAME = "homelab-k3s"
DEFAULT_NAMESPACE = "ai-platform"
```

Changing runtime data—replica counts, health results, deployment identifiers,
or calculated capacity—should generally be passed through parameters and
return values instead of stored globally. This keeps dependencies visible and
makes functions easier to test in isolation.

## Original Applied Example

This capacity report uses a global constant for stable platform identity and
local variables for inputs and calculated state:

```python
PLATFORM_NAME = "homelab-k3s"


def calculate_requested_resources(
    replicas, cpu_per_replica, memory_per_replica_gb
):
    requested_cpu = replicas * cpu_per_replica
    requested_memory_gb = replicas * memory_per_replica_gb
    return requested_cpu, requested_memory_gb


def create_deployment_summary(service_name, replicas):
    requested_cpu, requested_memory_gb = calculate_requested_resources(
        replicas, 0.5, 2
    )
    qualified_name = f"{PLATFORM_NAME}/{service_name}"
    return (
        f"Deployment: {qualified_name}\n"
        f"Replicas: {replicas}\n"
        f"Requested CPU: {requested_cpu} cores\n"
        f"Requested memory: {requested_memory_gb} GiB"
    )


def main():
    summary = create_deployment_summary("embedding-api", 3)
    print(summary)


if __name__ == "__main__":
    main()
```

Expected output:

```text
Deployment: homelab-k3s/embedding-api
Replicas: 3
Requested CPU: 1.5 cores
Requested memory: 6 GiB
```

`PLATFORM_NAME` is intentionally global because it represents stable context
for the module. Resource inputs enter through parameters. Intermediate values
remain local, and the completed summary leaves the function through `return`.
No function silently changes shared state.

## Common Mistakes

- Trying to use a function's parameter or local variable outside that
  function.
- Assuming all variables are visible everywhere in the program.
- Forgetting to return a local result needed by the caller.
- Creating a local name that unintentionally hides a global name.
- Using global variables for changing state that should be explicit input.
- Trying to use one function's local variable from another function.
- Confusing a name's scope with the lifetime of the value it refers to.

## Quick Self-Check

1. Where can a function parameter be used?
2. Why can a function read a module-level global name?
3. How should a result move from local function scope to its caller?
4. What happens when a local name is the same as a global name?
5. Why are parameters usually preferable to changing global state?
6. Which kinds of values are reasonable module-level constants?

## Reflection

Scope makes the ownership and visibility of program data predictable. Local
variables keep temporary calculations isolated, while parameters and return
values create clear interfaces between parts of a program. In infrastructure
automation, minimizing mutable global state reduces accidental coupling and
makes the same function easier to reuse in scripts, tests, APIs, and scheduled
jobs.

## Completed

Chapter 04 completed on 2026-10-09.
