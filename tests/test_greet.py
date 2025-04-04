import pytest
from app import app  # Flaskアプリのインスタンスをインポート

@pytest.fixture
def client():
    """
    Flaskアプリのテストクライアントを作成するフィクスチャ

    Returns
    -------
    FlaskClient
        Flaskアプリのテストクライアント
    """
    with app.test_client() as client:
        yield client

def test_greet_with_name(client):
    """
    /api/greetエンドポイントに対するGETリクエストのテスト

    Parameters
    ----------
    client : FlaskClient
        Flaskアプリのテストクライアント

    Returns
    -------
    None
    """
    response = client.get('/api/greet?name=みこと')  # GETリクエストを送信
    assert response.status_code == 200  # ステータスコードが200であることを確認
    assert response.json == {'message': 'こんにちは, みこと!'}  # レスポンスの内容を確認

def test_greet_without_name(client):
    """
    /api/greetエンドポイントに対するGETリクエストのテスト（名前なし）

    Parameters
    ----------
    client : FlaskClient
        Flaskアプリのテストクライアント

    Returns
    -------
    None
    """
    response = client.get('/api/greet')  # GETリクエストを送信（名前なし）
    assert response.status_code == 200  # ステータスコードが200であることを確認
    assert response.json == {'message': 'こんにちは, aaaa!'}  # レスポンスの内容を確認
