
import json
from blog.models import Post

with open('posts.json') as f:
    posts = json.load(f)
    print(posts)
 
