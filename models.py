import sqlalchemy as sq
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Contact(Base):

    __tablename__ = 'contacts'

    contact_id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String(50))
    last_name = sq.Column(sq.String(50))
    email = sq.Column(sq.String(100))
    address =sq.Column(sq.String(256))
