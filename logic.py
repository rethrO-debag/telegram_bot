import db

def auth_user(user_id):
	db.auth_user(user_id)
	db.close()
