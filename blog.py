import markdown2
import os


def get_posts():
    posts = []
    for file in os.listdir('./blogposts'):
        if not file.endswith('.md'):
            raise ValueError("Non-Markdown files in blogposts directory")
        
        with open('./blogposts/'+file, 'r') as fd:
            title = fd.readline().strip()
            date = fd.readline().strip()
            description = fd.readline().strip()
            fd.readline()
            content=''.join(fd.readlines())
            filename = file.rsplit('.')[0]

        posts.append({
            'title': title,
            'date': date,
            'description': description,
            'content': markdown2.markdown(content),
            'url': filename,
            })

    return sorted(posts, key=lambda x: x['date'], reverse=True)
