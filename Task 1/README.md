# Assignment 1: Task 1 <br>

### Problem Statement ###
To find the number of accidents occurring per hour that satisfy a set of conditions and display them in sorted fashion. <br>

### Mapper File ###
The mapper function does the following: <br>
 * Read the records from the JSON file - line by line. <br>
 * For every record, check the given 6 conditions. <br>
 * If the record satisfies all 6 conditions and does not contain "NaN" values in any required attributes, print <hour, 1>. <br>
 * Here, 'hour' is a character - ranging from 'a' to 'x' that corresponds to every hour 0 to 23. <br>
 * This makes the sorting the mapper output a lot easier. <br>

### Reducer File ###
The reducer function does the following: <br>
 * Read the mapper's sorted output - line by line. <br>
 * Convert the key (hour - which was a character) back to its corresponding integer. <br>
 * Aggregate all counts (of each hour). This is done dynamically as we read the inputs line by line. <br>
 * Print the aggregated total of every hour in the form <hour count>.
