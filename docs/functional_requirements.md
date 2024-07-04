1. Store All Data into Database locally:
- convert all the current data and save it as backup
- periodically during checking also add all the new or edited pages to the database

2. Polling for changes or creation of a page, when this happens:
- add all the necessary attributes that are missing: category, goal, project, ... notes, notebooks through 
  recursion up the goal hierarchy

3. create scripts to transfer data from one database to another manually as this cannot be done in Notion, so for 
   example use this to seperate notebooks into seperage categories or do whatever you want
