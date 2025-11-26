import pytest
import requests
import random
import re

BASE = "https://qa-internship.avito.com"


@pytest.fixture
def random_seller_id():
    return random.randint(111111, 999999)


@pytest.fixture
def item_data(random_seller_id):
    return {
        "sellerID": random_seller_id,
        "name": "Burger",
        "price": 300,
        "statistics": {"likes": 4, "viewCount": 200, "contacts": 2}
    }


@pytest.fixture
def created_item(item_data):

    r = requests.post(f"{BASE}/api/1/item", json=item_data)
    assert r.status_code == 200

    match = re.search(r"- ([\w-]+)$", r.json()["status"])
    assert match is not None, "Не удалось извлечь id из ответа"
    item_id = match.group(1)
    return item_id, item_data


def test_create_item(item_data):
    r = requests.post(f"{BASE}/api/1/item", json=item_data)
    assert r.status_code == 200
    assert "Сохранили объявление" in r.json()["status"]


def test_get_item_by_id(created_item):
    item_id, item_data = created_item
    r = requests.get(f"{BASE}/api/1/item/{item_id}")
    assert r.status_code == 200

    body = r.json()[0]
    assert body["id"] == item_id
    assert body["name"] == item_data["name"]
    assert body["price"] == item_data["price"]
    assert body["sellerId"] == item_data["sellerID"]


def test_get_items_by_seller(random_seller_id, item_data):
    item_data["sellerID"] = random_seller_id
    requests.post(f"{BASE}/api/1/item", json=item_data)

    r = requests.get(f"{BASE}/api/1/{random_seller_id}/item")
    assert r.status_code == 200

    arr = r.json()
    assert isinstance(arr, list)
    assert len(arr) > 0
    assert any(item["sellerId"] == random_seller_id for item in arr)


def test_get_statistics(created_item):
    item_id, item_data = created_item
    r = requests.get(f"{BASE}/api/1/statistic/{item_id}")
    assert r.status_code == 200

    stats = r.json()[0]
    assert stats["likes"] == item_data["statistics"]["likes"]
    assert stats["viewCount"] == item_data["statistics"]["viewCount"]
    assert stats["contacts"] == item_data["statistics"]["contacts"]
