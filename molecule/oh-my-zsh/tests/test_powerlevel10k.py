import pytest

# Test powerlevel10k installation
@pytest.mark.parametrize('username', [
    ('test_usr6')
])
def test_powerlevel10k_installed_by_default(host, username):
    powerlevel10k = host.file('/home/' + username + '/.oh-my-zsh/themes/powerlevel10k')
    powerlevel10k_config = host.file('/home/' + username + '/.p10k.zsh')
    assert powerlevel10k.exists
    assert powerlevel10k.is_directory
    assert powerlevel10k.user == username
    assert powerlevel10k.group in [username, 'users']

    assert powerlevel10k_config.exists
    assert powerlevel10k_config.is_file
    assert powerlevel10k_config.user == username
    assert powerlevel10k_config.group in [username, 'users']