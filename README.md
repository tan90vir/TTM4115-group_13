# TTM4115-group_13
RAT implementation instructions.
1) Move all files in your favourite path, let's say they will be located on "/home/ntnu/autoRATs".
2) Make a cronjob called every 15 minutes. This job should only call timestamp.sh in its path, like this "/bin/bash /home/ntnu/autoRATs/DataCollectorPY/timestamp.sh".
3) The script will download a .csv for each RAT in timestamp.txt and will upload statistics on Firebase database as well.
