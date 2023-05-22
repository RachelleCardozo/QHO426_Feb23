

blog_posts = [{"Photos":3, "Likes":2}, {"Likes":13, "Comments":4, "Shares":1}, {"Photos":6, "Likes":130, "Comments":20, "Shares":3}]

total_photos = 0
for post in blog_posts:
    try:
        total_photos = total_photos + post["Photos"]
    except KeyError:
        print("Exception occured")
        pass

print(total_photos)
