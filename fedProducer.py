import fedmsg

# until this is in place, add name="relay_inbound": http://paste.fedoraproject.org/155599/74653371/

fedmsg.publish(topic='testing', active=True, msg={
        'test': "Hello World",
})