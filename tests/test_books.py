async def test_books_requires_authentication(client):
    response = await client.get("/api/v1/books/")

    assert response.status_code in {401, 403}
