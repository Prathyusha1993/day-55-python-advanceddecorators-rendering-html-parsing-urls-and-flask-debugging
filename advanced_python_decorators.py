

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def iss_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper

@iss_authenticated_decorator
def create_blog_post(user):
    print(f'this is {user.name}s new blog')

new_user = User('Pinky')
new_user.is_logged_in = True
create_blog_post(new_user)