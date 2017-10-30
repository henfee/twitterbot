from newsapi.articles import Articles
from newsapi.sources import Sources
import secrets


a = Articles(API_KEY=secrets.newapi_api)
s = Sources(API_KEY=secrets.newapi_api)

print(s.informaion())
