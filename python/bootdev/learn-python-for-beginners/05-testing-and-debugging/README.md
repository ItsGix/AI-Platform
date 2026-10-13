# Chapter 05 - Testing and Debugging

## Status

Complete

## Lessons Reviewed

- Unit tests
- Debugging
- Debugging practice
- Stack traces

## Core Idea

Testing checks whether code behaves as expected. Debugging is the process of
finding and correcting the cause when it does not.

A productive development loop is:

1. Write a small amount of code.
2. Run it or its tests.
3. Compare the actual result with the expected result.
4. Investigate the smallest useful area when they differ.
5. Fix one problem, then run the tests again.

Short feedback loops make it easier to identify which change introduced a
problem. Tests preserve those expectations so later changes can be checked
automatically.

## Unit Tests

A unit test is a small automated check of one focused unit of behaviour,
usually a function. It calls the code with known inputs and verifies the
returned result:

```python
def calculate_total_xp(level, xp_to_add):
    current_xp = level * 100
    return current_xp + xp_to_add
```

A test for the function can be written with Python's built-in `unittest`
module:

```python
import unittest


class TestCalculateTotalXp(unittest.TestCase):
    def test_adds_level_xp_and_new_xp(self):
        actual = calculate_total_xp(3, 100)
        expected = 400
        self.assertEqual(actual, expected)
```

The test has three conceptual parts:

1. **Arrange** the inputs and expected result.
2. **Act** by calling the function.
3. **Assert** that the actual result matches the expectation.

Clear test names describe the behaviour being protected, making failures
easier to understand.

## Test Behaviour, Not Console Output

Checking returned values tests what a function does without coupling the test
to how information is displayed:

```python
def calculate_requested_cpu(replicas, cpu_per_replica):
    return replicas * cpu_per_replica
```

A test can call this function repeatedly with different arguments. If it only
printed the result, other code could not use the value directly and the test
would need to capture and compare console text.

Use `print()` temporarily to observe execution while debugging. Use `return`
to expose a function's result to callers and tests.

## Test More Than the Happy Path

One passing example does not prove a function works for every meaningful
input. A useful test set includes:

- a normal representative case;
- boundary values such as zero or one;
- different combinations of valid inputs; and
- cases related to bugs that were previously found.

For example:

```python
class TestCalculateRequestedCpu(unittest.TestCase):
    def test_three_replicas(self):
        self.assertEqual(calculate_requested_cpu(3, 0.5), 1.5)

    def test_zero_replicas(self):
        self.assertEqual(calculate_requested_cpu(0, 0.5), 0.0)

    def test_one_full_core_replica(self):
        self.assertEqual(calculate_requested_cpu(1, 1.0), 1.0)
```

In the course environment, running executes a visible subset of tests while
submitting runs additional tests. This models an important real-world habit:
passing the examples tried manually does not replace a broader automated test
suite, including edge cases.

## Failures and Errors

The distinction helps narrow an investigation:

| Outcome | Meaning | First question |
| --- | --- | --- |
| Pass | Actual behaviour matched the expectation | Are important cases covered? |
| Failure | Code ran, but actual and expected values differed | Which calculation or assumption is wrong? |
| Error | The test could not complete because an exception occurred | What does the traceback identify? |

Always compare the input, expected result, and actual result. A failing test is
evidence about one behaviour; it is not merely an obstacle to silence.

## A Deliberate Debugging Process

When behaviour is wrong:

1. Reproduce the problem consistently.
2. Read the failing test or requirement.
3. Reduce the problem to the smallest relevant input.
4. Inspect intermediate values with temporary `print()` calls.
5. Identify where actual behaviour first diverges from expectation.
6. Change one thing at a time.
7. Re-run the focused test, then the complete test suite.
8. Remove temporary debug output once it is no longer useful.

```python
def calculate_remaining_capacity(total_capacity, used_capacity):
    remaining_capacity = total_capacity + used_capacity  # Bug
    print("remaining_capacity:", remaining_capacity)
    return remaining_capacity
```

For inputs `10` and `4`, the temporary output exposes `14` instead of `6`.
The incorrect `+` operation is then much easier to isolate. After correcting
it to `-`, run the tests again and remove the temporary print.

Debug output should answer a specific question. Printing every variable can
create noise that hides the useful evidence.

## Build and Test Incrementally

Writing an entire program before running it makes every new line a possible
cause of failure. Instead, establish one working step at a time:

1. Create a syntactically valid function with a temporary result.
2. Add one calculation and inspect or test it.
3. Return the calculated value and test it.
4. Add the next piece of behaviour.
5. Repeat until the complete requirement passes.

This method is used by experienced engineers as well as beginners. Small
verified changes reduce uncertainty and make regressions easier to locate.

## Reading a Stack Trace

A stack trace, or traceback, records the path Python followed before an
exception stopped execution. Rather than treating it as one large message,
extract the useful parts:

1. Read the final line for the exception type and message.
2. Find the nearest frame that points to code under your control.
3. Note the file name and line number.
4. Inspect the displayed source line and its surrounding context.
5. If several functions are involved, follow the frames to understand the
   call path.

Example:

```text
Traceback (most recent call last):
  File "capacity.py", line 8, in <module>
    print(calculate_ratio(4, 0))
  File "capacity.py", line 4, in calculate_ratio
    return ready / total
ZeroDivisionError: division by zero
```

The final line names the error. The frame above it identifies the failing
operation in `calculate_ratio`, while the earlier frame shows who called it.

Syntax errors can point to indentation, an unfinished string, a missing
delimiter, or another location where Python could no longer parse the file.
Fix the first reported syntax problem and run the code again; another error
may have been hidden behind it.

## Original Applied Example

This compact example keeps the production function and tests together for the
notes. In a project they would normally live in separate files, such as
`capacity.py` and `test_capacity.py`.

```python
import unittest


def calculate_requested_resources(
    replicas, cpu_per_replica, memory_per_replica_gb
):
    requested_cpu = replicas * cpu_per_replica
    requested_memory_gb = replicas * memory_per_replica_gb
    return requested_cpu, requested_memory_gb


class TestCalculateRequestedResources(unittest.TestCase):
    def test_standard_deployment(self):
        actual = calculate_requested_resources(3, 0.5, 2)
        self.assertEqual(actual, (1.5, 6))

    def test_zero_replicas(self):
        actual = calculate_requested_resources(0, 0.5, 2)
        self.assertEqual(actual, (0.0, 0))

    def test_single_replica(self):
        actual = calculate_requested_resources(1, 1.0, 4)
        self.assertEqual(actual, (1.0, 4))

    def test_different_resource_profile(self):
        actual = calculate_requested_resources(4, 0.25, 1.5)
        self.assertEqual(actual, (1.0, 6.0))


if __name__ == "__main__":
    unittest.main()
```

The suite checks normal, boundary, and alternative-input cases. Running it
executes four tests and finishes with `OK`. If a future refactor changes the
calculation incorrectly, the expected and actual tuples identify the broken
behaviour immediately.

## Common Mistakes

- Testing only console output when the useful behaviour should be returned.
- Writing one happy-path test and assuming all inputs are covered.
- Changing several lines before re-running the failing test.
- Ignoring the expected and actual values in a failure report.
- Reading a traceback as undifferentiated text instead of locating the error
  type, file, line, and call path.
- Fixing the symptom shown by a test without understanding the cause.
- Leaving noisy temporary debug prints in completed code.
- Running only the focused test and forgetting the complete suite.
- Treating a passing suite as proof of cases that were never tested.

## Quick Self-Check

1. What makes a test a unit test?
2. Why are returned values usually easier to test than printed output?
3. What is the difference between a test failure and a test error?
4. Why should code be written and tested in small increments?
5. Which parts of a traceback should be inspected first?
6. Why should the full test suite run after the focused test passes?

## Reflection

Testing and debugging turn expectations into evidence. Unit tests provide
repeatable checks, while incremental development and tracebacks make failures
easier to isolate. These practices are essential for infrastructure tooling:
a small error in resource calculations, configuration generation, or rollout
logic can affect an entire environment, so behaviour should be verified before
automation reaches production.

## Completed

Chapter 05 completed on 2026-10-14.
