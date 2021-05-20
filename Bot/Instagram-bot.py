from instapy import InstaPy

session = InstaPy(username = "r.i.c.h.i.k", password = "$Richik1234")
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)
session.set_do_follow(True, percentage=100)
session.like_by_tags(["fcbarcelona", "poetrycommunity", "fcbfemeni", "fcb"], amount = 3)
session.set_dont_like(["nsfw"])

session.end()
