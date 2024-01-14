<h1>HTTPS/SSL Project</h1>
<h2>Tasks</h2>
<ul>
  <li>
    <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x10-https_ssl/0-world_wide_web">
      <strong>0-world_wide_web</strong>
    </a>
    <p>
      The script is a tool for querying DNS information for specific subdomains of a given domain and displaying details such as the record type and associated IP address. The specific subdomains to be queried can either be specified as command-line arguments or taken from a predefined list if no specific subdomain is provided.
    </p>
  </li>
  <li>
    <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x10-https_ssl/1-haproxy_ssl_termination">
      <strong>1-haproxy_ssl_termination</strong>
    </a>
    <p>
      This configuration essentially sets up HAProxy as a load balancer with SSL termination, directing incoming HTTP and HTTPS traffic to the specified backend servers (web-01 and web-02). The backend servers are checked for availability, and traffic is distributed in a round-robin fashion. The configuration also includes various settings for logging, timeouts, and SSL/TLS options.
    </p>
  </li>
  <li>
    <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x10-https_ssl/100-redirect_http_to_https">
      <strong>100-redirect_http_to_https</strong>
    </a>
    <p>
      This configuration essentially sets up HAProxy to handle both HTTP and HTTPS traffic, redirecting HTTP to HTTPS, and load balancing the requests between the specified backend servers (web-01 and web-02). It also includes SSL/TLS settings, logging configurations, and timeout settings. The backend servers are checked for availability, and traffic is distributed in a round-robin fashion.
    </p>
  </li>
</ul>
