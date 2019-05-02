## Runtime Analysis:

- Task0: O(1)
   - first_record_of_texts: O(1) as direct access to index of list
   - last_record_of_calls: O(1) as direct access to index of list

-----

- Task1: O(n * m) ~ O(n^2) worst case
  - loop through calls: O(n)
    - check if is in unique_number_list: O(m) 
  - loop through texts: O(n)
    - check if is in unique_number_list: O(m) 

-----
 
 - Task2: O(n * m) ~ O(n)
   - loop thought calls: O(n) 
   - splitting phone number: O(m) which is not significant
   - getting month_name : O(1) direct access by index from the list of months
   
-----

- Task 3:
   - PartA:  O(n * m) + O(nlogn) = O(nlogn),  m is not a big number becuase phone numbers length are limited compared to the length of all calls in dataset
     - find_code(): O(n * m) loops through all calls n, and m as length of phone number
       - is_fixed_line() : O(1) just checks for 1 characer by direct access
       - get_fixed_line_code(): O(m), m as length of phone number for splitting phone number by ) 
       - is_mobile(): O(1) just checks for 1 character in the middle by direct access
       - is_telemarketer(): O(1) if starts by 140 just character check by direct access
     - checking if code in in codes list: O(n) 
     - printing :
       - sort: O(nlong)
       - printing: O(n)
   - PartB: O(n * m), but m is not significant and it's the length of longest phone number so the time complexity is O(n)
     - loop through calls: O(n)
       - is_fixed_line() : O(1) just checks for 1 characer by direct access
       - get_fixed_line_code(): O(m), m as length of phone number for splitting phone number by ) 

