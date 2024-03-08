from Database import Database
from Page import Page
from PropertyTypes import PropertyTypes

pages = [Page("name", "title", "content", [PropertyTypes.URL, PropertyTypes.ID])]
database = Database("id", "title", pages, [PropertyTypes.URL, PropertyTypes.ID])
