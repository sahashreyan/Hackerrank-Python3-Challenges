from instapy import InstaPy

session = InstaPy(username = "your username", password = "your password")
#Replace your username with your actual username and the same with your password
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)
#You can set max followers to limit the search to those accounts within the limit
session.set_do_follow(True, percentage=100)

session.like_by_tags(["fcbarcelona", "poetrycommunity", "fcbfemeni", "fcb"], amount = 3)
#add as many tags as you want and remember the actual amount will be 9 more than what is given.
session.set_dont_like(["nsfw"])
#here is the list of tags you want to exclude from your search

session.end()
