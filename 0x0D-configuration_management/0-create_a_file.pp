# this code generates a file with a phrase in it
file { "/tmp/holberton":
  ensure  => 'file',
  path    => "/tmp/holberton",
  mode    => "0744",
  owner   => "www-data",
  group   => "www-data",
  content => "I love Puppet"
}
