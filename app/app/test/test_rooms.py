def test_index(client, room):
    response = client.get('/room/')
    assert response.status_code == 200
    assert b"Room A" in response.data


def test_add_room(client):
    response = client.post('/room/add', data={
        'name': 'Room B',
        'description': 'New room'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Room B" in response.data


def test_edit_room(client, room):
    response = client.post(f'/room/edit/{room.id}', data={
        'name': 'Room C',
        'description': 'Updated room'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Room C" in response.data


def test_delete_room(client, room):
    response = client.get(f'/room/delete/{room.id}', follow_redirects=True)
    assert response.status_code == 200
    assert b"Room A" not in response.data