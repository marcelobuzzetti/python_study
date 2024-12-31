import web

# Urls accept regex
urls = (
    '/(.*)', 'index'
)

# Define app
app = web.application(urls, globals())

class index:
    def GET(self, name):
        return f"Hello {name}!"

if __name__ == "__main__":
    app.run()