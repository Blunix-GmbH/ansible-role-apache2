import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_module_package_present(host):
    assert host.package('libapache2-mod-security2')


def test_module_package_absent(host):
    assert not host.package('libapache2-mod-dnssd').is_installed
