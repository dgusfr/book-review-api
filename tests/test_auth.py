async def test_docs_are_available(client):
    response = await client.get("/api/v1/docs")

    assert response.status_code == 200
