### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_chat_channels',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_id', type='string',
          label=T('Id')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_chat_channels_archive',db.t_chat_channels,Field('current_record','reference t_chat_channels',readable=False,writable=False))

########################################
db.define_table('t_posts',
    Field('f_id_chanal', type='string',
          label=T('Id Chanal')),
    Field('f_id', type='string',
          label=T('Id')),
    Field('f_post_text', type='string',
          label=T('Post Text')),
    auth.signature,
    format='%(f_id_chanal)s',
    migrate=settings.migrate)

db.define_table('t_posts_archive',db.t_posts,Field('current_record','reference t_posts',readable=False,writable=False))
