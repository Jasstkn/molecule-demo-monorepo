import pytest

# Test zsh, oh-my-zsh
@pytest.mark.parametrize('username', [
    'test_usr1',
    'test_usr2',
    'test_usr5',
])
def test_oh_my_zsh_install(host, username):
    oh_my_zsh = host.file('/home/' + username + '/.oh-my-zsh')
    assert oh_my_zsh.exists
    assert oh_my_zsh.is_directory
    assert oh_my_zsh.user == username
    assert oh_my_zsh.group in [username, 'users']


@pytest.mark.parametrize('username', [
    'test_usr3',
    'test_usr4',
])
def test_oh_my_zsh_is_not_installed_for_excluded_users(host, username):
    oh_my_zsh = host.file('/home/' + username + '/.oh-my-zsh')
    zshrc = host.file('/home/' + username + '/.zshrc')
    assert not oh_my_zsh.exists
    assert not zshrc.exists


@pytest.mark.parametrize('username,theme,plugins', [
    ('test_usr1', 'test_theme1', 'test_plugin1 test_plugin2'),
    ('test_usr2', 'test_theme2', 'test_plugin3 test_plugin4'),
])
def test_oh_my_zsh_config(host, username, theme, plugins):
    zshrc = host.file('/home/' + username + '/.zshrc')
    assert zshrc.exists
    assert zshrc.is_file
    assert zshrc.user == username
    assert zshrc.group in [username, 'users']
    assert zshrc.contains(theme)
    assert zshrc.contains(plugins)


# Test default installation
@pytest.mark.parametrize('username,theme,plugins,custom_plugins', [
    ('test_usr6',
    'powerlevel10k',
    'git',
    'zsh-syntax-highlighting zsh-autosuggestions' )
])
def test_antigen_installation(host, username, theme, plugins, custom_plugins):
    zshrc = host.file('/home/' + username + '/.zshrc')
    antigen = host.file('/home/' + username + '/antigen.zsh')
    assert zshrc.exists
    assert zshrc.is_file
    assert antigen.exists
    assert antigen.is_file
    assert zshrc.user == username
    assert zshrc.group in [username, 'users']
    assert zshrc.contains(theme)
    assert zshrc.contains(plugins)
    zshrc.contains
    # check installation via antigen for custom plugins
    for plugin in custom_plugins.split(" "):
        assert zshrc.contains("antigen bundle " + "zsh-users/" +plugin )