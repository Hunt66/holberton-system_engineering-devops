# This kills the process killmenow

exec { 'kill_process':
  command  => 'pkill killmenow',
  provider => 'shell'
}
