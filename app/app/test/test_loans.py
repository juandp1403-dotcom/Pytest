def test_index(client):
    response = client.get('/Loan/')
    assert response.status_code == 200


def test_add_loan(client, book, user):
    response = client.post('/Loan/add', data={
        'bookId': book.idBook,
        'userId': user.idUser
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"test_book" in response.data


def test_edit_loan(client, loan):
    response = client.post(f'/Loan/edit/{loan.idLoan}', data={
        'returnDate': '2026-10-01',
        'fine': '2.5',
        'status': 'Returned'
    }, follow_redirects=True)
    assert response.status_code == 200


def test_delete_loan(client, loan):
    response = client.get(f'/Loan/delete/{loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200


def test_return_loan(client, loan):
    response = client.get(f'/Loan/return/{loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
