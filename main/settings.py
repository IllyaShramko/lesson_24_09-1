import flask, flask_migrate, flask_sqlalchemy

main_project = flask.Flask(
    import_name = "main",
    template_folder = "templates"
)