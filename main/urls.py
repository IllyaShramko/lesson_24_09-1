import user
import home
from .settings import main_project

user.user_app.add_url_rule(
    rule= "/user/",
    view_func= user.render_user,
    methods= ["GET", "POST"]
)
main_project.register_blueprint(user.user_app)

home.home_app.add_url_rule(rule= "/", view_func= home.render_home, methods= ["GET", "POST"])
main_project.register_blueprint(blueprint= home.home_app)

