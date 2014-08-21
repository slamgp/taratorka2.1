from gluon.contrib.populate import populate
if db(db.auth_user).isempty():
     populate(db.auth_user,10)
     populate(db.t_chat_channels,10)
     populate(db.t_posts,10)
