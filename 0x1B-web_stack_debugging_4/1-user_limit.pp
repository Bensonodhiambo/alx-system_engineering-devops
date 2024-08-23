# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message.

exec {'OS security config':
  command => 'sed -i "s/nofile [0-9]/nofile 5000/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
