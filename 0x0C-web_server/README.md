<h1>Web Server Project</h1>
<h2>Tasks 📃</h2>
    <ol>
        <li>
            <strong>
                <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x0C-web_server/0-transfer_file">Transfer a file to your server</a>
            </strong>
            <p><code>0-transfer_file:</code> Bash script that transfers a file from client to a server.</p>
            <p>Accepts four arguments:</p>
            <ul>
                <li>The path of the file to be transferred.</li>
                <li>The IP of the server to transfer the file to.</li>
                <li>The username that scp connects with.</li>
                <li>The path of the SSH private key that scp uses.</li>
            </ul>
            <p>scp transfers the file to the user home directory ~/.</p>
        </li>
        <li>
            <strong>
                <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x0C-web_server/1-install_nginx_web_server">Install nginx web server</a>
            </strong>
            <p><code>1-install_nginx_web_server:</code> Bash script that configures a new Ubuntu machine with Nginx.</p>
            <ul>
                <li>Nginx listens on port 80.</li>
                <li>When querying Nginx at its root / with a curl GET request, it returns a page containing the string Hello World!.</li>
            </ul>
        </li>
        <li>
            <strong>
                <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x0C-web_server/2-setup_a_domain_name">Setup a domain name</a>
            </strong>
            <p><code>2-setup_a_domain_name:</code> A text file containing the domain name set up for the server through Gandi.</p>
        </li>
        <li>
            <strong>
                <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x0C-web_server/3-redirection">Redirection</a>
            </strong>
            <p><code>3-redirection:</code> Bash script that configures a new Ubuntu machine with Nginx.</p>
            <ul>
                <li>Setup is identical to <code>1-install_nginx_web_server</code> plus:</li>
                <li>The location /redirect_me returns a 301 Moved Permanently redirection to another page.</li>
            </ul>
        </li>
        <li>
            <strong>
                <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x0C-web_server/4-not_found_page_404">Not found page 404</a>
            </strong>
            <p><code>4-not_found_page_404:</code> Bash script that configures a new Ubuntu machine with Nginx.</p>
            <ul>
                <li>Setup is identical to <code>1-install_nginx_web_server</code> plus:</li>
                <li>Features a custom 404 page containing the string Ceci n'est pas une page.</li>
            </ul>
        </li>        
        <li>
            <strong>
                <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x0C-web_server/7-puppet_install_nginx_web_server.pp">Deploy fast, deploy well</a>
            </strong>
            <p><code>fabfile.py:</code>This Puppet manifest installs Nginx, creates a simple "Hello World" HTML page, and configures URL redirection using a custom Nginx site configurati</p>           
        </li>
    </ol>
