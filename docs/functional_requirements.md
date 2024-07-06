1. Store All Data into Database locally:

- convert all the current data and save it as backup
- periodically during checking also add all the new or edited pages to the database

2. Polling for changes or creation of a page, when this happens:

- add all the necessary attributes that are missing: category, goal, project, ... notes, notebooks through
  recursion up the goal hierarchy

3. create scripts to transfer data from one database to another manually as this cannot be done in Notion, so for
   example use this to seperate notebooks into seperage categories or do whatever you want

- automated adding of tasks to track routines and habbits
- automated assignment of areas, goals and projects based on the upper hierarchy property attributes
- propagation of tags and other attributes from the sub-items inside the database meaning that the sub-items will have
  the same attributes + unique as their parents
- resources database → when you create video, book, article, link it will also be created inside resources database and
  made to mirror it for easier sorting and filtering and just one property assignemnt option in other databases
- write an automation using listener, by adding new connections such as Zapier and adding an automated Python Script
  such that whenever you add a new entry into Books, Videos,… it will also add this entry into the general database for
  aggregation and anaylysis and ease of access, the name will be the link to the details page and it will just copy the
  author tag, category, subcategory ,….
- clean API call wrapped inside methods so that I do not have to work with strings but classes instead
