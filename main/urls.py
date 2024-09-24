import home
from .settings import main_project

home.home_app.add_url_rule(rule= "/", view_func= home.render_home, methods= ["GET", "POST"])
main_project.register_blueprint(blueprint= home.home_app)