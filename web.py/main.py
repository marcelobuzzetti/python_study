import web

# Urls accept regex and will be passed as arguments to the GET method to index class
urls = (
    '/(.*)/(.*)', 'index' # /name/last_name
)
# define templates
render = web.template.render("resources/")

# Define app
app = web.application(urls, globals())

class index:
    def GET(self, name, last_name):
        # return f"Hello {name}!"
        return render.main(name, last_name)

if __name__ == "__main__":
    app.run()