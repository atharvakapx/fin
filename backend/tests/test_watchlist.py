"""Tests for watchlist API: GET, POST add, POST duplicate, DELETE."""

import pytest


@pytest.mark.asyncio
async def test_get_watchlist_default_ten(client):
    resp = await client.get("/api/watchlist")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 10
    tickers = [item["ticker"] for item in data]
    assert "AAPL" in tickers
    assert "GOOGL" in tickers


@pytest.mark.asyncio
async def test_post_add_ticker(client):
    resp = await client.post("/api/watchlist", json={"ticker": "AMD"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["ticker"] == "AMD"

    resp = await client.get("/api/watchlist")
    tickers = [item["ticker"] for item in resp.json()]
    assert "AMD" in tickers
    assert len(tickers) == 11


@pytest.mark.asyncio
async def test_post_duplicate_returns_409(client):
    await client.post("/api/watchlist", json={"ticker": "AMD"})
    resp = await client.post("/api/watchlist", json={"ticker": "AMD"})
    assert resp.status_code == 409


@pytest.mark.asyncio
async def test_delete_removes_ticker(client):
    resp = await client.delete("/api/watchlist/AAPL")
    assert resp.status_code == 200
    assert resp.json()["ok"] is True

    resp = await client.get("/api/watchlist")
    tickers = [item["ticker"] for item in resp.json()]
    assert "AAPL" not in tickers
    assert len(tickers) == 9


@pytest.mark.asyncio
async def test_delete_nonexistent_returns_404(client):
    resp = await client.delete("/api/watchlist/ZZZZ")
    assert resp.status_code == 404
