from flask import Blueprint, jsonify, request

greet_bp = Blueprint('greet', __name__, url_prefix='/api')

@greet_bp.route('/greet', methods=['GET'])
def greet():
    """
    GETリクエストに対して挨拶を返すエンドポイント

    Returns
    -------
    JSON
        挨拶メッセージを含むJSONレスポンス
    """
    name = request.args.get('name', 'aaaa')
    # デフォルト値は'aaaa'に設定
    return jsonify({'message': f'こんにちは, {name}!'})  # JSONレスポンスを返す
