# TTM4115-group_13
RAT implementation instructions.
1) Move all files in your favourite path.
2) Make a cronjob called every 15 minutes. This job should only call rat_downloader.sh in its path.
3) The script will download a .csv with RAT's answers.
Notes:
- The csv file will be named after the RAT number
- The RAT number will be computed on rat_links.txt rows.
- The first row of form-links.txt is intended to host the title of the file.
- RAT-1.csv gives you an example of the expected result.
