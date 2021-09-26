# UE19CS322 : Big Data - Assignment 1

## Aim of the assignment:
To read a data set and perform specific tasks using the ***Map-Reduce*** framework of the ***Hadoop Ecosystem***. <br><br>
_Language used:_ Python 3.8.x <br>
_Dataset:_ [5% and 15% Dataset](https://drive.google.com/drive/folders/1oxwATscIyOc4vG_HYaAz1QpEItHcsREp) <br>

## Steps to run tasks:
 To run the code locally on your system wihtout using hadoop, the following command can be used: <br>
 ```
 cat <path-to-json-file-dataset> | python3 mapper.py [command_line_arguments] | sort -k 1,1 | python3 reducer.py [command_line_arguments]
 ```
 <br>
 
To run the code on ***Hadoop HDFS*** on your local system: <br>
1. Turn on ***Hadoop*** on your local system. <br><br>
2. Create a directory within hdfs to store the dataset file. <br>
```
hdfs dfs -mkdir /<folder-name>
```
<br>

3. The command below is used to create a folder called **input** to store the dataset. <br>
```
hdfs dfs -mkdir /<folder-name>/input
```
<br>

4. Add the json dataset file into the directory **input** which was created in the previous step. <br>
```
hdfs dfs -put <path-to-json-file> /<folder-name>/input
```
<br>

5. To verify if the JSON files was successfully added:<br>
```
hdfs dfs -ls /<folder-name>/input
```
<br>

6. To run the code on the ***Hadoop HDFS***, run this command. Note that the output folder _must NOT exist_ when running this command. Hadoop creates it internally.<br>
```
hadoop jar <path-to-streaming-jar-file> -input /<folder-name>/input -output /<folder-name>/output -file <path-to-mapper-file> <path-to-reducer-file> -mapper "python3 mapper.py [command_line_arguments]" -reducer "python3 reducer.py"
```
<br>

7. Once executed, the output will be visible using the following command. <br>
```
hdfs dfs -cat /<folder-name>/output/part-00000
```

## Contributors:
[Hari Raagav T R](https://github.com/HariRaagavTR) <br>
[Manasa S M](https://github.com/manasa-sm) <br>
[Lakshmi Narayan P](https://github.com/LakshmiNarayanP) <br>

