import PAM
from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(user, password):
    class AuthConv:
        def __init__(_, password):
            _.password = password
        def __call__(_, auth, query_list, userData):
            print "AuthConv called, pwd: %s" % _.password
            resp = []
            for query, qt in query_list:
                if qt == PAM.PAM_PROMPT_ECHO_ON:
                    resp.append((_.password, 0))
                elif qt == PAM.PAM_PROMPT_ECHO_OFF:
                    resp.append((_.password, 0))
                elif qt == PAM.PAM_PROMPT_ERROR_MSG or type ==PAM.PAM_PROMPT_TEXT_INFO:
                    print query
                    resp.append(('', 0))
                else:
                    return None            
            return resp
    auth = PAM.pam()
    auth.start("claros")
    auth.set_item(PAM.PAM_USER, user)
    auth.set_item(PAM.PAM_CONV, AuthConv(password))
    try:
        auth.authenticate()
        auth.acct_mgmt()
        print "Authentication successful"
        return User(1,user,password)
    except PAM.error, resp:
        return 


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

if __name__ == '__main__':
    app.run()




authenticate("cd", "cd")