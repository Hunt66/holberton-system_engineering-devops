exec { 'modify_file':
  command => "/bin/sed -ie\'s/class-wp-locale.phpp/class-wp-local.php/\' /war/www/html/wp-settings.php"
}
