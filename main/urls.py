import user
from .settings import main_project

user.user_app.add_url_rule(
    rule= "/user/",
    view_func= user.render_user,
    methods= ["GET", "POST"]
)
main_project.register_blueprint(user.user_app)