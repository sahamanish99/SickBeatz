from . import *

def get_users():
  return User.query.all()

def get_user_id(idd):
  return User.query.filter_by(id = idd).first()

def get_user_name(name):
  return User.query.filter(func.lower(User.name) == func.lower(name)).first()

def add_user(usr):
  db.session.add(usr)
  db.session.commit()
  return usr

def delete_user(usr):
  if usr:
    elt = get_user_id(usr.id)
    db.session.delete(elt)
    db.session.commit()
    return True
  else: return False

def delete_users():
  User.query.delete()
  db.session.commit()
  return True