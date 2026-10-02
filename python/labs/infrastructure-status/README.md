# Infrastructure Status Report

## Purpose

This lab uses basic Python values to produce a readable summary of a gaming PC
and a small k3s-based AI platform. It turns the introductory variables lesson
into an infrastructure-oriented command-line report.

## Concepts Practised

- Descriptive `snake_case` variable names
- Strings, integers, floats, and booleans
- Comments and units of measurement
- F-string interpolation
- Newline escape sequences
- Grouping terminal output into readable sections

## Run

From the repository root:

```bash
python3 python/labs/infrastructure-status/status_report.py
```

## Learning Notes

The important step in this exercise was moving beyond isolated values and
combining them into useful output. Grouping related information makes the
report easier to scan, while descriptive names preserve the meaning of values
such as node counts, resource utilisation, and service status.

This is intentionally a small learning lab rather than a live monitoring tool:
the values are examples stored directly in the script. A future project could
collect the same information from system or Kubernetes APIs.
