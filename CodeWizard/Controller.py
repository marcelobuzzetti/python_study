import web
import json

urls = (
    '/', 'Home',
    '/register', 'Register',
)

render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())

# Classes/Routes

class Home:
    def GET(self):
        return render.Home()
    
class Register:
    def GET(self):
        return render.Register()
    def POST(self):
        web.header('Content-Type', 'application/json')
        try:
            data = json.loads(web.data())
            response = {'username': data.get('username')}
            print(response)
            return json.dumps(response)
        except json.JSONDecodeError:
            return json.dumps({'error': 'Invalid JSON'})
    
if __name__ == "__main__":
    app.run()