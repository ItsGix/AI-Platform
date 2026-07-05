Perfect. We'll follow the same format throughout the course so by the end you'll have both Python knowledge and a Git repository showing your progress.

Since your goal is **AI Platform Engineering**, everything will be tied back to infrastructure, Kubernetes, Docker, APIs and automation rather than random examples like "apples and bananas."

---

# Week 1 – Module 01

# Variables & Data Types

---

# 📖 Theory

## What is a Variable?

A variable is simply a named place in memory that stores data.

Think of it like a label stuck onto a storage box.

Instead of remembering:

```
16
```

you remember

```python
cpu_cores
```

Example:

```python
cpu_cores = 16
```

Now Python remembers that **cpu_cores** means **16**.

---

## Why Variables Matter

Imagine writing automation without variables.

Instead of

```python
print(16)
print(16)
print(16)
```

you can do

```python
cpu_cores = 16

print(cpu_cores)
print(cpu_cores)
print(cpu_cores)
```

Later if your server changes:

```
16 → 32 cores
```

you only update one line.

---

# Assignment (=)

The equals sign does **not** mean "equals" like maths.

It means:

> Store the value on the right inside the variable on the left.

Example

```python
ram = 128
```

means

```
Store 128 inside ram
```

---

# Variable Naming

Good

```python
gpu_name
vm_count
server_ip
worker_nodes
cluster_name
```

Bad

```python
a
x
thing
data
```

Python style uses:

```
snake_case
```

Example

```python
gpu_temperature
```

not

```
GpuTemperature
gpuTemperature
```

---

# Core Data Types

There are only a few you'll use constantly.

---

## Integer (int)

Whole numbers.

```python
cpu_cores = 16
```

```python
worker_nodes = 2
```

---

## Float

Decimal numbers.

```python
cpu_usage = 54.7
```

```python
latency = 0.34
```

---

## String (str)

Text.

```python
hostname = "worker-01"
```

```python
model = "RTX 3060"
```

Always inside quotes.

---

## Boolean (bool)

True or False.

```python
gpu_enabled = True
```

```python
cluster_online = False
```

You'll use these constantly later.

---

# Checking Types

Python can tell you what something is.

```python
cpu = 16

print(type(cpu))
```

Output

```python
<class 'int'>
```

Example

```python
hostname = "worker-01"

print(type(hostname))
```

Output

```
<class 'str'>
```

---

# Printing Variables

```python
hostname = "worker-01"

print(hostname)
```

Output

```
worker-01
```

Multiple values

```python
hostname = "worker-01"
ram = 128

print(hostname, ram)
```

Output

```
worker-01 128
```

---

# Comments

Python ignores comments.

```python
# GPU information

gpu = "RTX 3060"
```

Use comments to explain *why*, not *what*.

Good:

```python
# RTX 3060 is dedicated to llama.cpp inference
```

Bad:

```python
# This is a variable
gpu = "RTX 3060"
```

---

# 💻 Infrastructure Examples

## Example 1

```python
hostname = "k3s-worker-01"
ip_address = "192.168.77.101"

print(hostname)
print(ip_address)
```

---

## Example 2

```python
cpu_cores = 16
ram_gb = 128

print(cpu_cores)
print(ram_gb)
```

---

## Example 3

```python
gpu_model = "RTX 3060"
gpu_available = True

print(gpu_model)
print(gpu_available)
```

---

## Example 4

```python
cluster_name = "ai-platform"

control_planes = 1
worker_nodes = 2

print(cluster_name)
print(control_planes)
print(worker_nodes)
```

---

## Example 5

```python
llm = "Qwen 3"
context_size = 8192
temperature = 0.7

print(llm)
print(context_size)
print(temperature)
```

Notice how all four data types naturally appear in infrastructure work.

---

# ✍️ Exercises

Create variables for:

### Exercise 1

Your PC

```
CPU model
RAM
GPU
Windows version
```

---

### Exercise 2

Your AI Cluster

Store

* Cluster name
* Control planes
* Worker nodes
* GPU node
* Kubernetes version (just make one up for now)

---

### Exercise 3

Store

```
Current CPU usage
Current RAM usage
Current GPU temperature
```

Use floats where appropriate.

---

### Exercise 4

Create booleans

```
internet_connected

docker_running

gpu_available

cloudflare_tunnel_connected
```

---

### Exercise 5

Print everything.

---

# 🏆 Challenge

Without copying the examples exactly...

Create a Python program describing **your own AI Platform**.

Include at least:

* hostname
* IP address
* CPU
* RAM
* GPU
* operating system
* Kubernetes version
* number of worker nodes
* whether Docker is running
* whether the GPU is enabled

Print every value.

---

# 📝 Notes

Create a file:

```
python_course/python_course.md
```

Add something like this (in your own words if you prefer):

```markdown
# Module 01 – Variables & Data Types

## Variables
- Store values in memory
- Created using =
- Can be reused throughout a program

## Main Data Types
- int → Whole numbers
- float → Decimal numbers
- str → Text
- bool → True/False

## Useful Functions
print()
type()

## Naming
Use snake_case

Example:
gpu_model
worker_nodes
cluster_name
```

As you progress through the course, this file will become your own Python reference guide.

---

# 📁 Expected Project Structure

By the end of this module, your directory should look like:

```text
python/
├── python_course/
│   ├── python_course.md
│   └── week01/
│       └── module01/
│           └── variables.py
└── README.md
```

Put all of today's code and exercises into `variables.py`, separating sections with comments.

---

# ✅ Git Commit & Push

Once you've completed the exercises and challenge:

```bash
git status
git add .
git commit -m "Complete Week 1 Module 01 - Variables and Data Types"
git push
```

This gives you a clear history of your learning and builds a portfolio you can show to employers.

---

### Learning goals for this module

By the end of Module 01, you should be able to:

* Explain what a variable is and why it's useful.
* Choose the correct basic data type (`int`, `float`, `str`, or `bool`) for a value.
* Use meaningful `snake_case` variable names.
* Print variables and inspect their types with `print()` and `type()`.
* Represent simple infrastructure information (servers, clusters, GPUs, IPs) as Python variables.

Once you've finished the exercises and challenge, send me your `variables.py` (or paste its contents here). I'll review it like a mentor, point out improvements, explain any mistakes, and then we'll move on to **Week 1 – Module 02: Operators**.


