#!python

from twisted.internet import main
from twisted.spread import pb
from twisted.enterprise import adbapi
from twisted.web import widgets, server

from twisted.forum import gadgets, service

# Create Twisted application object
application = main.Application("forum")

# Connect to a database.
dbpool = adbapi.ConnectionPool("pyPgSQL.PgSQL", database="twisted")

# Create the service
forumService = service.ForumService("posting", application, dbpool)

# Create posting board object
gdgt = gadgets.ForumGadget(application, forumService)

# Accept incoming connections!
application.listenOn(8485, server.Site(gdgt))

# Done.
