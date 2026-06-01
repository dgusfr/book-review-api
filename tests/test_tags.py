async def test_tags_requires_authentication_or_permission(client):
    response = await client.get("/api/v1/tags/")

    assert response.status_code in {401, 403}
