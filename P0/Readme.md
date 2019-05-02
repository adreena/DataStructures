##Runtime Analysis:

- Task0: O(1)
   - first_record_of_texts: O(1) as direct access to index of list
   - last_record_of_calls: O(1) as direct access to index of list

###

- Task1: O(n * m), O(n^2) worst case
  - loop through calls: O(n)
    - check if is in unique_number_list: O(m) 
  - loop through texts: O(n)
    - check if is in unique_number_list: O(m) 

 