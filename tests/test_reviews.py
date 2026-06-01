async def test_reviews_requires_authentication_or_permission(client):
    response = await client.get("/api/v1/reviews/")

    assert response.status_code in {401, 403}
