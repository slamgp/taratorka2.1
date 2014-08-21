# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict(message = "You are welcomed taratorka")

def error():
    return dict()

@auth.requires_login()
def chat_channels_manage():
    if request.vars.btn_create:
        db.t_chat_channels.insert(f_name = request.vars.chanel_name)
    chaneles = db(db.t_chat_channels.id>0).select()
    return dict(chanales = chaneles,message = "Select a channel")

@auth.requires_login()
def posts_manage():
 #  form = SQLFORM.smartgrid(db.t_posts,onupdate=auth.archive)
 #  return locals()
    try:
        idChanels = request.raw_args[0]
        session.idChanales = request.raw_args[0]
    except:
         redirect(URL('default','chat_channels_manage'))
    if idChanels == '':
        redirect(URL('default','chat_channels_manage'))
 #   if request.vars.btn_send:
 #       db.t_posts.insert(f_post_text = request.vars.post_text, f_id_chanal	= idChanels)
    rows = db(db.t_posts.f_id_chanal == idChanels).select(orderby = ~db.t_posts.created_on)
    str = '';
    list_str = list()
    for row in rows:
        if row.created_by != None:
            rowsUser = db(db.auth_user.id == row.created_by).select()
            t_user = rowsUser[0].first_name
            for rowUser in rowsUser:
                t_user = rowUser.first_name
            str_post = '' + '[' + row.created_on.strftime("%Y-%m-%d %H:%M:%S") + ' : ' + t_user + ']   ' +  row.f_post_text  +  '\n'
            str = str + str_post
            list_str.append(str_post)
    request.ajax = True
    return dict(message = "all messages", text = str, list = list_str)

def read_post():
    list_str = list()
    rows = db((db.t_posts.f_id_chanal == session.idChanales) & (db.t_posts.f_post_text.like('' + request.vars.find_text    +'%') )).select(orderby = ~db.t_posts.created_on)
    str = '';
    for row in rows:
        if row.created_by != None:
            rowsUser = db(db.auth_user.id == row.created_by).select()
            t_user = rowsUser[0].first_name
                #for rowUser in rowsUser:
                    #t_user = rowUser.first_name
            str_post = '' + '[' + row.created_on.strftime("%Y-%m-%d %H:%M:%S") + ' : ' + t_user + ']   ' +  row.f_post_text  +  '\n'
            str = str + str_post
    return str

def input_post():
    db.t_posts.insert(f_post_text = request.vars.post_text, f_id_chanal = session.idChanales)
    str = read_post()
    return str

def find_post():
    list_str = list()
#    rows = db((db.t_posts.f_id_chanal == session.idChanales) & (db.t_posts.f_post_text.like('' + request.vars.find_text    #+'%'))).select(orderby = ~db.t_posts.created_on)
    rows = db((db.t_posts.f_id_chanal == session.idChanales) & (db.t_posts.f_post_text.like('' + request.vars.find_text    +'%'))).select(orderby = ~db.t_posts.created_on)
    str = '';
    for row in rows:
        if row.created_by != None:
            rowsUser = db(db.auth_user.id == row.created_by).select()
            t_user = rowsUser[0].first_name
                #for rowUser in rowsUser:
                    #t_user = rowUser.first_name
            str_post = '' + '[' + row.created_on.strftime("%Y-%m-%d %H:%M:%S") + ' : ' + t_user + ']   ' +  row.f_post_text  +  '\n'
            str = str + str_post
    return str
