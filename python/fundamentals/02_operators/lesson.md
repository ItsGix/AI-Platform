# Week 1 – Module 2: Operators

This module teaches you how Python performs calculations and comparisons, which you'll use constantly in automation, infrastructure scripts, Kubernetes tooling, and AI applications.

---

## Learning Objectives

By the end of this module you'll understand:

* Arithmetic operators
* Assignment operators
* Comparison operators
* Logical operators
* Membership operators
* Identity operators
* Operator precedence

You'll also use your own homelab as the examples.

---

# Directory Structure

Inside your repository create:

```text
python/
└── fundamentals/
    └── 02_operators/
        ├── lesson.md
        ├── exercise.py
        ├── challenge.md
        └── reflection.md
```

Exactly the same layout as Module 1.

---

# Lesson 1 - Arithmetic Operators

These are simply maths.

```python
cores = 16
workers = 2

print(cores + workers)
print(cores - workers)
print(cores * workers)
print(cores / workers)
print(cores // workers)
print(cores % workers)
print(cores ** 2)
```

Know what each one does.

| Operator | Meaning        |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiply       |
| /        | Divide         |
| //       | Floor division |
| %        | Remainder      |
| **       | Power          |

---

## Infrastructure Example

Imagine you have

```python
memory_gb = 128
nodes = 4

memory_per_node = memory_gb / nodes

print(memory_per_node)
```

This is a realistic calculation you'll perform later with Kubernetes sizing.

---

# Lesson 2 - Assignment Operators

You've already seen this.

```python
pods = 3

pods += 1

print(pods)
```

Other examples

```python
pods -= 1
pods *= 2
pods /= 2
```

---

# Lesson 3 - Comparison Operators

These return either

```python
True
```

or

```python
False
```

Example

```python
cpu = 16

print(cpu == 16)
print(cpu != 8)
print(cpu > 8)
print(cpu < 32)
print(cpu >= 16)
print(cpu <= 8)
```

---

## Real AI Example

```python
gpu_memory = 12

print(gpu_memory >= 8)
```

Could output

```
True
```

Meaning the GPU can run a particular model.

---

# Lesson 4 - Logical Operators

Combine conditions.

```python
ram = 128
gpu = True

print(ram >= 64 and gpu)
```

Returns

```
True
```

Another

```python
internet = True
vpn = False

print(internet or vpn)
```

Another

```python
server_running = False

print(not server_running)
```

---

# Lesson 5 - Membership Operators

Checks if something exists.

```python
services = [
    "Immich",
    "OpenWebUI",
    "Portainer",
    "AMP"
]

print("Immich" in services)

print("Plex" in services)
```

Outputs

```
True
False
```

You'll use this constantly later.

---

# Lesson 6 - Identity Operators

Checks whether two variables reference the same object.

```python
a = 10
b = a

print(a is b)
```

Usually not used much until later.

Just know it exists.

---

# Lesson 7 - Operator Precedence

Python follows maths order.

```python
print(2 + 3 * 4)
```

Outputs

```
14
```

Not

```
20
```

Parentheses override.

```python
print((2 + 3) * 4)
```

Outputs

```
20
```

---

# Exercise

Create variables using your own homelab.

Example ideas:

```python
cpu_cores = 16
ram = 128
workers = 2
control_plane = 1
gpu_memory = 12
```

Perform:

* Addition
* Subtraction
* Multiplication
* Division
* Comparison
* Logical operators
* Membership checks using a list of your services

Print every result.

### What this module unlocks

After Module 2, you'll have the foundations needed for Module 3: **Control Flow (`if`, `elif`, `else`)**. That's where your scripts start making decisions—the basis of infrastructure automation, health checks, and AI platform tooling.
