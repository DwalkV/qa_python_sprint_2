from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    # Нельзя добавить одну и ту же книгу дважды
    def test_add_new_book_forbidden_add_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1

    # Нельзя выставить рейтинг книге, которой нет в списке
    def test_set_book_rating_no_rating_for_book_not_in_list(self):
        collector = BooksCollector()
        collector.set_book_rating('Щегол', 8)
        assert len(collector.get_books_rating()) == 0

    # Нельзя выставить рейтинг меньше 1.
    def test_set_book_rating_null_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Сто лет одиночества')
        collector.set_book_rating('Сто лет одиночества', 0)
        assert collector.books_rating['Сто лет одиночества'] != 0

    # Нельзя выставить рейтинг больше 10
    def test_set_book_rating_more_than_ten_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Автостопом по Галактике')
        collector.set_book_rating('Автостопом по Галактике', 100)
        assert collector.books_rating['Автостопом по Галактике'] == 1

    # У не добавленной книги нет рейтинга.
    def test_get_book_rating_book_not_in_list_without_rating(self):
        collector = BooksCollector()
        collector.get_book_rating('Щегол')
        assert collector.get_book_rating('Щегол') is None

    # Получить список книг только с одинаковым рейтингом
    def test_get_books_with_specific_rating_two_same_rating_books(self):
        collector = BooksCollector()
        collector.add_new_book('Автостопом по Галактике')
        collector.add_new_book('Щегол')
        collector.set_book_rating('Автостопом по Галактике', 10)
        collector.set_book_rating('Щегол', 8)
        assert collector.get_books_with_specific_rating(10) == ['Автостопом по Галактике']

    # Добавление книги в избранное.
    def test_add_book_in_favorites_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Автостопом по Галактике')
        collector.add_book_in_favorites('Автостопом по Галактике')
        assert 'Автостопом по Галактике' in collector.get_list_of_favorites_books()

    # Нельзя добавить книгу в избранное, если её нет в словаре books_rating
    def test_add_book_in_favorites_add_book_not_from_books_rating(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Автостопом по Галактике')
        assert 'Автостопом по Галактике' not in collector.get_list_of_favorites_books()

    # Проверка удаления книги из избранного
    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Автостопом по Галактике')
        collector.add_book_in_favorites('Автостопом по Галактике')
        collector.delete_book_from_favorites('Автостопом по Галактике')
        assert len(collector.get_list_of_favorites_books()) == 0

