def test_api_de_listagem_de_produtos(client, db):
    resp = client.get('/api/produtos/list')
    assert resp.status_code == 200