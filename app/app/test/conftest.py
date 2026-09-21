from app import create_app, db
import pytest

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()  # Create tables within the context
        yield app
        db.session.remove()  # Cleanup session objects
        db.drop_all()
  

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def user(app):
    from app.models.users import User
    user = User(nameUser="test_user", passwordUser="test_password")
    db.session.add(user)
    db.session.commit()  # Commit changes within the context
    yield user    
  # Cleanup changes within the context


@pytest.fixture
def author(app):
    from app.models.authors import Author
    author = Author(nameAuthor="test_author", nationalityAuthor="Spain")
    db.session.add(author)
    db.session.commit()
    return author


@pytest.fixture
def book(app, author):
    from app.models.books import Book
    book = Book(titleBook="test_book", authorId=author.idAuthor)
    db.session.add(book)
    db.session.commit()
    return book


@pytest.fixture
def computer(app):
    from app.models.computers import Computer
    computer = Computer(
        brandComputer="Dell",
        modelComputer="Latitude",
        statusComputer="Active"
    )
    db.session.add(computer)
    db.session.commit()
    return computer


@pytest.fixture
def room(app):
    from app.models.rooms import Room
    room = Room(name="Room A", description="Test room")
    db.session.add(room)
    db.session.commit()
    return room


@pytest.fixture
def loan(app, book, user):
    from app.models.loans import Loan
    loan = Loan(bookId=book.idBook, userId=user.idUser)
    db.session.add(loan)
    db.session.commit()
    return loan


@pytest.fixture
def computer_loan(app, computer, user):
    from app.models.cloans import ComputerLoan
    loan = ComputerLoan(computerId=computer.idComputer, userId=user.idUser)
    db.session.add(loan)
    db.session.commit()
    return loan