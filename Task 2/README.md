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
 
 ### Run the program ###
 To run the code locally on your system wihtout using hadoop, the following command can be used: <br>
 ```
 cat <path-to-json-file-dataset> | python3 mapper.py <co-ordinate1> <co-ordinate2> <distance> | sort -k 1,1 | python3 reducer.py
 ```
 _co-ordinate1, co-ordinate2_ and _distance_ are the command line arguments for the mapper file. <br><br>
 To run the code on ***Hadoop HDFS*** on your local system: <br>
1. Turn on ***Hadoop*** on your local system. <br>
2. Create a directory within hdfs to store the dataset file. <br>
```
hdfs dfs -mkdir /<folder-name>
```
3. The command below is used to create a folder called **input** to store the dataset <br>
```
hdfs dfs -mkdir /<folder-name>/input
```
4. Add the json dataset file into the directory **input** which was created in the previous step.<br>
```
hdfs dfs -put <path-to-json-file> /<folder-name>/input
```
5. To verify if the JSON files was successfully added<br>
```
hdfs dfs -ls /<folder-name>/input
```
6. To run the code on the ***Hadoop HDFS***<br>
```
hadoop jar <path-to-streaming-jar-file> -input /<folder-name>/input -output /<folder-name>/output -file <path-to-mapper-file> <path-to-reducer-file> -mapper "python3 mapper.py <co-ordinate1> <co-ordinate2> <distance>" -reducer "python3 reducer.py"
```
7. Once executed, the output will be visible using the following command.<br>
```
hdfs dfs -cat /<folder-name>/output/part-00000
```
>_co-ordinate1, co-ordinate2_ and _distance_ are the command line arguments for the mapper file. <br>
