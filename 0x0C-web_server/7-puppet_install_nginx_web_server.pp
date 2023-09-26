# Puppet manifest to install Nginx, set up a Hello World page, and configure URL redirection

# Install Nginx package
package { 'nginx':
  ensure => 'present',
}

# Create a custom HTML file with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  mode    => '0644',
}

# Configure Nginx site with URL redirection
file { '/etc/nginx/sites-available/redirect.conf':
  ensure  => file,
  content => '
    server {
      listen 80;
      server_name localhost;

      location /redirect_me {
        return 302 https://youtube.com;
      }

      location / {
        root /var/www/html;
        index index.html;
      }
    }
  ',
  mode => '0644',
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/redirect.conf':
  ensure => link,
  target => '/etc/nginx/sites-available/redirect.conf',
  notify => Exec['nginx_reload'],
}

# Reload Nginx to apply the configuration
exec { 'nginx_reload':
  command     => 'sudo service nginx reload',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-enabled/redirect.conf'],
  require     => [Package['nginx'], File['/etc/nginx/sites-available/redirect.conf']],
}

# Start Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['nginx_reload'],
}

