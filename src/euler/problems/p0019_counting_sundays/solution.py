'''
Problem 19: Counting Sundays
'''
from euler.utils.common import timeit

@timeit
def solve() -> int:
    """
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """
    # 0=Sunday, 1=Monday, ..., 6=Saturday
    # Given: 1 Jan 1900 was a Monday (1)
    
    # Calculate start day for 1 Jan 1901
    # 1900 is NOT a leap year (divisible by 100 but not 400) -> 365 days
    # 365 % 7 = 1
    # So 1 Jan 1901 is (1 + 1) % 7 = 2 (Tuesday)
    
    day_of_week = 2 
    sunday_count = 0
    
    # Months days mapping
    # Index 1-12, ignore index 0
    days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for year in range(1901, 2001): # 1901 to 2000 inclusive
        # Check leap year
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        
        for month in range(1, 13):
            # Check if current month 1st is Sunday
            if day_of_week == 0:
                sunday_count += 1
            
            # Calculate days in current month
            if month == 2:
                days = 29 if is_leap else 28
            else:
                days = days_in_months[month]
                
            # Update day_of_week for next month
            day_of_week = (day_of_week + days) % 7
            
    return sunday_count

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
