# -*- coding: utf-8 -*-
"""Test the book api routes."""
from unittest.mock import MagicMock, patch

import pytest


@pytest.mark.usefixtures("db")
class TestBookRoutes:
    """Test suite for book routes."""

    @patch("backend.database.db.session")
    def test_get_all_books(self, mock_db_session, testapp):
        """Test retrieving all books."""
        mock_book = MagicMock()
        mock_book.id = 1
        mock_book.title = "Mock Book"
        mock_book.author_id = 1
        mock_book.genre = "Fiction"
        mock_book.published_year = "2022"

        mock_db_session.scalars().all.return_value = [mock_book]

        response = testapp.get("/books/")
        assert response.status_code == 200
        assert b"Mock Book" in response.body

    @patch("backend.database.db.session")
    def test_get_book(self, mock_db_session, testapp):
        """Test retrieving a single book by ID."""
        mock_book = MagicMock()
        mock_book.id = 1
        mock_book.title = "Mock Book"
        mock_book.author_id = 1
        mock_book.genre = "Fiction"
        mock_book.published_year = "2022"

        mock_db_session.scalars().all.return_value = [mock_book]

        response = testapp.get("/books/1")
        assert response.status_code == 200
        assert b"Mock Book" in response.body

    @patch("backend.database.db.session")
    def test_create_book(self, mock_db_session, testapp):
        """Test creating a new book."""
        mock_db_session.add.return_value = None
        mock_db_session.commit.return_value = None

        book_data = {
            "title": "New Book",
            "author_id": 1,
            "genre": "Science Fiction",
            "published_year": "2023",
        }
        response = testapp.post_json("/books/", book_data)
        assert response.status_code == 201

    @patch("backend.database.db.session")
    def test_update_book(self, mock_db_session, testapp):
        """Test updating an existing book."""
        mock_book = MagicMock()
        mock_book.id = 1
        mock_book.title = "Mock Book"

        mock_db_session.scalars().all.return_value = [mock_book]

        book_update_data = {"title": "Updated Book"}
        response = testapp.put_json("/books/1", book_update_data)
        assert response.status_code == 200

    @patch("backend.database.db.session")
    def test_delete_book(self, mock_db_session, testapp):
        """Test deleting a book by ID."""
        mock_book = MagicMock()
        mock_book.id = 1
        mock_book.title = "Mock Book"

        mock_db_session.scalars().all.return_value = [mock_book]

        response = testapp.delete("/books/1")
        assert response.status_code == 200
