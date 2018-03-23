import unittest

class TestBook(unittest.TestCase):
	"""
	This uncludes the tests for the books model
	"""

	def setUp(self):
		self.book = Book('User')

	def test_borrow_book(self):
		"""
		Test to borrow a book
		"""


	def test_return_book(self):
		"""
		Test to return a book
		"""
		