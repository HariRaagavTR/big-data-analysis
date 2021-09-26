# Assignment 1: Task 2 <br>

### Problem Statement ###
To find the number of accidents occurring per city and state where the distance between the start coordinates of the accident and a given pair of coordinates - (LATITUDE, LONGITUDE) is within D. LATITUDE, LONGITUDE and D are passed into the mapper as command line arguments. <br>

### Mapper File ###
_Note:_ A function called **euclidian_dist()** was created to calculate the distance between the 2 co-ordinates :round_pushpin: passed as parameter. <br>
The mapper function does the following: <br>
 * Read the records from the JSON file line by line. <br>
 * Obtain the latitude and longitude of each record. <br>
 * Calculate the distance between the co-ordinates :round_pushpin: entered in the command line and the co-ordinates obtained from each record. <br>
 * If this distance is less than the distance entered in the command line, then it satisfies the condition. <br>
 * For those satisfied records, use the latitude and longitude as json parameters to make a **POST** API request call to the given URL. <br>
 * Obtain the state and city name from the response. <br>
 * Print them. <br>

### Reducer File ###
The reducer function does the following: <br>
 * Obtain all the records from the mapper's output line by line. <br>
 * Aggregate the counts of all states and cities. <br>
 * Print all states and cities along with their counts in a specific order. <br> 
 * Keys (Ex: AB, AC) that are derived from another key (Ex: A) must be printed first. <br>
 * This logic holds true for any level of derivation. (Example order: ABC, ABD, AB, AC, A) <br>
 * A key is considered derived only if the child key is separated from its parent value by a space. (Ex: "Marina Beach" is derived from "Marina" while "Marina-Beach" is not) <br>
 * This order is obtained dynamically. <br>
