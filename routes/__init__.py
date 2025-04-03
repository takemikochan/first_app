from .greet import greet_bp

def register_blueprints(app):
    """
    FlaskアプリにBlueprintを登録する関数

    Parameters
    ----------
    app : Flask
        Flaskアプリのインスタンス

    Returns
    -------
    None
    """
    app.register_blueprint(greet_bp)  # greet_bpをFlaskアプリに登録
    # 他のBlueprintもここで登録できる
    # app.register_blueprint(other_bp)