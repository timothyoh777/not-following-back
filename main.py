import json

with open("followers.json") as read_file:
    followers = json.load(read_file)
with open("following.json") as read_file:
    following = json.load(read_file)

followers_set = set()
following_set = set()

for id in followers["relationships_followers"]:
    followers_set.add(id["string_list_data"][0]["value"])
for id in following["relationships_following"]:
    following_set.add(id["string_list_data"][0]["value"])

print(following_set - followers_set)

