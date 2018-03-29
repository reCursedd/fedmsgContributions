

import fedmsg

topic_filter = 'fedoratagger'   # This is much easier to test with

for name, endpoint, topic, msg in fedmsg.tail_messages():
    if topic_filter not in topic:
        # Bail out if the topic doesn't match
        continue

    pprint.pprint(msg)
