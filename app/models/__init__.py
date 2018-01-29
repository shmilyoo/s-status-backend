from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def socket_session_commit():
    try:
        db.session.commit()
        return {'success': True}
    except Exception as e:
        db.session.rollback()
        return {'success': False, 'message': str(e)}
    finally:
        db.session.remove()
