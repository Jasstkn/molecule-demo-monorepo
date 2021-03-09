import pytest

@pytest.mark.parametrize('username', [
    'test_usr1',
    'test_usr2',
    'test_usr5',
])
def test_oh_my_tmux_install(host, username):
    tmux = host.file('/home/' + username + '/.tmux')
    tmux_conf = host.file('/home/' + username + '/.tmux.conf')
    tmux_local_conf = host.file('/home/' + username + '/.tmux.conf.local')
    assert tmux.exists
    assert tmux.is_directory
    assert tmux.user == username
    assert tmux.group in [username, 'users']
    assert tmux_conf.exists
    assert tmux_conf.is_symlink
    assert tmux_conf.linked_to == '/home/' + username + "/.tmux/.tmux.conf"
    assert tmux_local_conf.exists
    assert tmux_local_conf.is_file


@pytest.mark.parametrize('username', [
    'test_usr3',
    'test_usr4',
])
def test_oh_my_tmux_is_not_installed_for_excluded_users(host, username):
    tmux = host.file('/home/' + username + '/.tmux')
    assert not tmux.exists
