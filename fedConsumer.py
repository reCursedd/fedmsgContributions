import fedmsg
import fedmsg.config
import logging.config
import fedmsg.meta

import pprint
# First, load the fedmsg config from fedmsg.d/
config = fedmsg.config.load_config()

# Then, configure the python stdlib logging to use fedmsg's logging config
logging.config.dictConfig(config.get('logging'))
active = True
fedmsg.meta.make_processors(**config)

#topic_filter = 'fedbadges'     # We really want this, but its rare
topic_filter = 'github'   # This is much easier to test with

for name, endpoint, topic, msg in fedmsg.tail_messages():
    if topic is 'testing' :
        pprint.pprint(msg)
    if topic in 'fedoraproject':
        print("Hiiii")
