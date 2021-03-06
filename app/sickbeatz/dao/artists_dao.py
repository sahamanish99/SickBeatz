from . import *

def get_artist_name(name):
  return Artist.query.filter(func.lower(Artist.name) == func.lower(name)).first()

def get_artist_id(idd):
  return Artist.query.filter_by(id = idd).first()

def artists_by_name(name):
  name = '%' + name + '%'
  return Artist.query.filter(Artist.name.ilike(name)).all()

def get_all_artists():
  return Artist.query.all()

def add_artist(artist):
  db.session.add(artist)
  db.session.commit()
  return artist

def delete_artist(artist):
  if artist:
    elt = get_artist_id(artist.id)
    db.session.delete(elt)
    db.session.commit()
    return True
  else: return False

def delete_artists():
  Artist.query.delete()
  db.session.commit()
  return True

def add_ifnotexists(session, model, **kwargs):
  obj = model.query.filter_by(**kwargs).first()
  if obj:
    return obj
  else:
      obj = model(**kwargs)
      session.add(obj)
      session.commit()
      return obj