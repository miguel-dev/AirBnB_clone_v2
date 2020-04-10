# Manifest that configures a server to deploy web static
exec { 'cmd_0':
  path    => '/usr/bin:/bin',
  command => 'sudo apt-get -y update',
  returns => [0,1]
}

exec { 'cmd_1':
  require => Exec['cmd_0'],
  path    => '/usr/bin:/bin',
  command => 'sudo apt-get -y install nginx',
  returns => [0,1]
}


exec { 'cmd_2':
  require => Exec['cmd_1'],
  path    => '/usr/bin:/bin',
  command => 'mkdir -p /data/web_static/releases/test',
  returns => [0,1]
}
exec { 'cmd_3':
  require => Exec['cmd_2'],
  path    => '/usr/bin:/bin',
  command => 'mkdir -p /data/web_static/shared/',
  returns => [0,1]
}

exec { 'cmd_4':
  require => Exec['cmd_2'],
  path    => '/usr/bin:/bin',
  command => 'echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html',
  returns => [0,1]
}

exec { 'cmd_5':
  require => Exec['cmd_2'],
  path    => '/usr/bin:/bin',
  command => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  returns => [0,1]
}

exec { 'cmd_6':
  require => Exec['cmd_5'],
  path    => '/usr/bin:/bin',
  command => 'chown -R ubuntu:ubuntu /data/',
  returns => [0,1]
}

exec { 'cmd_7':
  require => Exec['cmd_6'],
  path    => '/usr/bin:/bin',
  command => 'sed -i "43i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\t autoindex on;\n\t}\n" /etc/nginx/sites-enabled/default',
  returns => [0,1]
}

exec { 'cmd_8':
  require => Exec['cmd_7'],
  path    => '/usr/bin:/bin',
  command => 'sudo service nginx restart',
  returns => [0,1]
}
