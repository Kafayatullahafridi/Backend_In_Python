import datetime


class Loan:
    def __init__(self, loan_id, book, member, loan_date=None, return_date=None):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.loan_date = loan_date or datetime.date.today()
        self.return_date = return_date

    def __str__(self):
        return f" {self.member} borrowed {self.book} on {self.loan_date}"
    def __repr__(self): 
        return f"Loan({self.loan_id}, {self.book}, {self.member}, {self.loan_date}, {self.return_date})"
    def mark_as_returned(self):
        self.return_date = datetime.date.today()
        self.book.is_available = True
    @property
    def is_active(self):
        return self.return_date is None