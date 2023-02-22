from .factory import NewsPortalFactory, AuthorFactory, ArticleFactory

# Generate some NewsPortal instances
news_portals = NewsPortalFactory.create_batch(5)

# Generate some Author instances
authors = AuthorFactory.create_batch(10)

# Generate some Article instances
articles = ArticleFactory.create_batch(15)