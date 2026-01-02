# Counting Sundays

## Problem Statement

You are given the following information:
*   1 Jan 1900 was a Monday.
*   Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
*   A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

## Analysis

This problem asks us to simulate the calendar logic.

### Leap Year Rule
A year $Y$ is a leap year if:
1.  $Y$ is divisible by 4 AND ($Y$ is not divisible by 100 OR $Y$ is divisible by 400).

For example:
*   1900: Divisible by 4, divisible by 100, NOT divisible by 400 -> **Not Leap**.
*   1901-1999: Standard divisible by 4 rule works.
*   2000: Divisible by 400 -> **Leap**.

### Manual Simulation Strategy
We don't need `datetime` libraries. We can track the day of the week using modular arithmetic.

Let $0 = \text{Sunday}, 1 = \text{Monday}, \dots, 6 = \text{Saturday}$.

1.  **Initialization**:
    *   1 Jan 1900 was a Monday (1).
    *   1900 was not a leap year (365 days). $365 \pmod 7 = 1$.
    *   Therefore, 1 Jan 1901 was a Tuesday ($1+1=2$).
    *   Start simulation from `current_day = 2`.

2.  **Simulation**:
    *   Loop `year` from 1901 to 2000.
    *   Loop `month` from 1 to 12.
    *   If `current_day == 0`, increment `sunday_count`.
    *   Add the number of days in the current month to `current_day`.
    *   Take modulo 7.

This approach is $O(1)$ (constant number of months) and purely logical.