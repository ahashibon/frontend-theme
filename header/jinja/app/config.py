# mcloud_base_url is used directly for the side menu
mcloud_base_url = "https://www.materialscloud.org"

# mcloud_base_url can be reused for the section links
# (but you can also define alternative ones)
urls = {
 "learn": "{}/learn".format(mcloud_base_url),
 "work": "{}/work".format(mcloud_base_url),
 "discover": "{}/discover".format(mcloud_base_url),
 "explore": "{}/explore".format(mcloud_base_url),
 "archive": "{}/archive".format(mcloud_base_url),
}

# set the css class of your section to "active"
css_classes = {
 "learn": "",
 "work": "",
 "discover": "",
 "explore": "",
 "archive": "active",
}
