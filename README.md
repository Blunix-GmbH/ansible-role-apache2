# Apache2 Ansible Role (ansible-role-apache2) from Blunix GmbH

This role installs and configures Apache HTTP Server on Debian with the same layout we use in production.

The Ansible Role is written and actively maintained by <a href="https://www.blunix.com" target="_blank">Blunix GmbH</a>.
It is used in the Blunix <a href="https://www.blunix.com/linux-managed-hosting.html" target="_blank">Linux Managed Hosting</a> Stack.
Its usage is documented at our <a href="https://www.blunix.com/manual" target="_blank">Linux Managed Hosting Documentation</a>.

---

## Features

- Installs Apache2 plus helper packages such as `python3-passlib` and per-project module packages.
- Enables or disables Apache modules and cleans up unwanted vhosts.
- Templates the main Apache config and common include snippets (gzip, ssl).
- Manages HTTP basic authentication files with `htpasswd`.
- Renders and enables user-supplied virtual host templates under `/etc/apache2/sites-available`.

---

## Requirements

- Ansible: **>= 2.9.10**
- Managed operating systems: Debian **bullseye**

---


## Role variables, inventory and example playbook

An example play, example `inventory/group_vars` and `inventory/host_vars` as well as example template files for the role are located in the `example/ directory`.

- <a href="https://github.com/Blunix-GmbH/ansible-role-apache2/blob/main/example/inventory/group_vars/exa_www_prod_web.yml" target="_blank">`example/inventory/group_vars/exa_www_prod_web.yml`</a> — module defaults, log variables, and vhost list.
- <a href="https://github.com/Blunix-GmbH/ansible-role-apache2/blob/main/example/play.yml" target="_blank">`example/play.yml`</a> — calls the role with inventory-driven vhosts.
- <a href="https://github.com/Blunix-GmbH/ansible-role-apache2/blob/main/example/templates/etc/apache2/sites-available/www.example.com.conf.j2" target="_blank">`example/templates/etc/apache2/sites-available/www.example.com.conf.j2`</a> — vhost template rendered by the playbook.
- Templates expect `ansible_cake_managed`; pass it via inventory or `-e 'ansible_cake_managed=Managed by Ansible from {{ template_fullpath }}'` to include the source path automatically.

### Tests

The directory `test/` contains an example `play.yml` as well as `inventory/group_vars/`, if applicable to the role. the script `example/run-tests.sh` creates a IONOS cloud instance with terraform, uses the example inventory and playbook to run the role and then run pytest tests located in `example/tests/`. Destroy the terraform using `./run-tests.sh -d`.


---

## Managed files and templates

- <a href="https://github.com/Blunix-GmbH/ansible-role-apache2/blob/main/templates/etc/apache2/apache2.conf.j2" target="_blank"><code>/etc/apache2/apache2.conf</code></a>
- <a href="https://github.com/Blunix-GmbH/ansible-role-apache2/blob/main/templates/etc/apache2/includes/ssl.conf.j2" target="_blank"><code>/etc/apache2/includes/ssl.conf</code></a>
- <a href="https://github.com/Blunix-GmbH/ansible-role-apache2/blob/main/templates/etc/apache2/includes/gzip.conf.j2" target="_blank"><code>/etc/apache2/includes/gzip.conf</code></a>
- `/etc/apache2/sites-available/<name>.conf` rendered from the playbook-provided templates referenced in `apache2_vhosts_present` (see <a href="https://github.com/Blunix-GmbH/ansible-role-apache2/blob/main/example/templates/etc/apache2/sites-available/example-www.conf.j2" target="_blank"><code>example/templates/etc/apache2/sites-available/example-www.conf.j2</code></a>).

---

## Author Information

Blunix GmbH Berlin  

`root@Linux:~# Support | Consulting | Hosting | Training`

Blunix GmbH provides 24/7/365 Linux emergency support and consulting, Service Level Agreements for Debian Linux managed hosting using Ansible Configuration Management as well as Linux trainings and workshops.

Learn more at <a href="https://www.blunix.com" target="_blank">https://www.blunix.com</a>.

## Contact Information

For bug reports and feature requests, please open an issue in this repository’s GitHub issue tracker.

Otherwise please refer to the <a href="https://www.blunix.com/#contact" target="_blank">Blunix GmbH Contact Information</a>.

---

## License

Apache-2.0

Please refer to the `LICENSE` file in the root of this repository.
