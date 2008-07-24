from pylons import config
from sqlalchemy import Column, MetaData, Table, types
from sqlalchemy.orm import mapper
from sqlalchemy.orm import scoped_session, sessionmaker

from img_gallery.model.photo import Photo

Session = scoped_session(sessionmaker(autoflush=True, transactional=True,
                                      bind=config['pylons.g'].sa_engine))

metadata = MetaData()

photos_table = Table('photos', metadata,
                     Column('id', types.String(100), primary_key=True),
                     Column('title', types.Unicode(255)),
                     Column('location', types.Text),
                     Column('license', types.Text),
                     )

mapper(Photo, photos_table)
