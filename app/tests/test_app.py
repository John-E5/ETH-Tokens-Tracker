"""
This file tests routes and responses

"""


class Testing:

    def test_get_home_route(self, client):
        res = client.get('/home')

        assert res.status_code == 200
        assert b'home-header' in res.data
        assert b'token-images' in res.data
        assert b'create-token' in res.data
        assert b'read-token' in res.data
        assert b'update-delete' in res.data
        assert b'home-footer' in res.data
        assert b'carousel' in res.data
        assert b'ScrollReveal()' in res.data

    def test_get_register_route(self, client):
        res = client.get('/register')

        assert res.status_code == 200
        assert b'username' in res.data
        assert b'email' in res.data
        assert b'password' in res.data
        assert b'password' != 'password'

    def test_get_login_route(self, client):
        res = client.get('/login')

        assert res.status_code == 200
        assert b'email' in res.data
        assert b'password' in res.data
        assert b'password' != 'password'

    def test_get_logout_route(self, client):
        res = client.get('/logout')

        assert res.status_code == 200
        assert b'logout' not in res.data
        assert b'login' in res.data
        assert b'register' in res.data

    def test_get_profile_route(self, client):
        res = client.get('/profile_page', follow_redirects=True)

        assert res.status_code == 200

    def test_get_stats_route(self, client):
        res = client.get('/portfolio_stats', follow_redirects=True)

        assert res.status_code == 200

    def test_get_dashboard_route(self, client):
        res = client.get('/dashboard', follow_redirects=True)

        assert res.status_code == 200

    def test_get_add_token_route(self, client):
        res = client.get('/token/new', follow_redirects=True)

        assert res.status_code == 200

    def test_get_token_route(self, client):
        res = client.get('/token/1', follow_redirects=True)

        assert res.status_code == 200

    def test_get_delete_token_route(self, client):
        res = client.get('/dashboard/1/delete_token', follow_redirects=True)

        assert res.status_code == 200