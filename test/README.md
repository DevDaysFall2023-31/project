# Simple script to send some requests to service

Simple script to send requests to service with given rps during given number of seconds.

How to run script.py:
```
python3 script.py -a <action> -r <rps value> -s <duration in second> --ip <ip address> --port <port> 
```

List of actions is hard coded:
- "favourites" -- send resuests to /tracks/favourites
- "similar" -- send requests to /tracks/{track_id}/similar with random id got from yandex_music
- "peak" -- send requests to /peaks/{track_id} with random id got from yandex_music

There is parallel_runner.sh script that allows to sun several python scripts in background. Output will be stored in out.txt file.

How to run parallel_runner.sh:
```
./parallel_runner.sh <number of processes> -a <action> -r <rps value> -s <duration in second> --ip <ip address> --port <port> 
```
The inly difference between script.py and parallel_runner.sh arguments is that you have to pass number of processes in **first** argument.

Example:
```
./parallel_runner.sh 2 -a favourites -r 5 -s 1 --port 8080
```
