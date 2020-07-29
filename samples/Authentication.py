destOrg = GIS("home")
print("Logged in as: " + destOrg.properties.user.username)

orig_userid = unS
new_userid  =  "YPotawsky@esri.com"

sourceUser = sourceOrg.users.get(orig_userid)
newUser = destOrg.users.get(new_userid)

source_user = sourceOrg.users.search(orig_userid)
dest_user = destOrg.users.search(new_userid)