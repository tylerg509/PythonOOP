
# from myappengine import webfunc, run_app

# class MainPage(webfunc.RequestHandler):
#     def get(self):
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.out.write('Welcome to the greatest website on the web')

    
# class FAQPage(webfunc.RequestHandler):
#     def get(self):
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.out.write('Welcome to the greatest FAQ on the web')

# application = webfunc.WSGIApplication(
#     [('/', MainPage),
#     ('/info', FAQPage)],debug=True
# )

# def main():
#     run_app(application)

# main()