def test_index(client, computer):
    response = client.get('/computers/')
    assert response.status_code == 200
    assert b"Dell" in response.data


def test_add_computer(client):
    response = client.post('/computers/add', data={
        'brandComputer': 'Lenovo',
        'modelComputer': 'ThinkPad',
        'statusComputer': 'Active'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Lenovo" in response.data


def test_update_computer(client, computer):
    response = client.post(f'/computers/update/{computer.idComputer}', data={
        'brandComputer': 'HP',
        'modelComputer': 'EliteBook',
        'statusComputer': 'Inactive'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"HP" in response.data


def test_delete_computer(client, computer):
    response = client.post(f'/computers/delete/{computer.idComputer}', follow_redirects=True)
    assert response.status_code == 200
    assert b"Dell" not in response.data