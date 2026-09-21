def test_index(client):
    response = client.get('/cloans/')
    assert response.status_code == 200


def test_add_loan(client, computer, user):
    response = client.post('/cloans/add', data={
        'computerId': computer.idComputer,
        'userId': user.idUser
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Dell" in response.data


def test_update_loan(client, computer_loan, computer, user):
    response = client.post(f'/cloans/update/{computer_loan.idLoan}', data={
        'computerId': computer.idComputer,
        'userId': user.idUser,
        'loanDate': '2026-09-21',
        'returnDate': '2026-10-01',
        'status': 'Returned'
    }, follow_redirects=True)
    assert response.status_code == 200


def test_delete_loan(client, computer_loan):
    response = client.post(f'/cloans/delete/{computer_loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200


def test_return_loan(client, computer_loan):
    response = client.post(f'/cloans/return/{computer_loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200