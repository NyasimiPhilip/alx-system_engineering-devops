<h1>SSH Project</h1>
<h2>Tasks 📃</h2>
    <ul>
        <li>
            <strong>
                <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x0B-ssh/0-use_a_private_key">Use a private key</a>
            </strong>
            <p><code>0-use_a_private_key:</code> Bash script that uses ssh to connect to my ALX-provided server.</p>
        </li>
        <li>
            <strong>
                <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x0B-ssh/1-create_ssh_key_pair">Create an SSH key pair</a>
            </strong>
            <p><code>1-create_ssh_key_pair:</code> Bash script that creates an RSA key pair.</p>
        </li>
        <li>
            <strong>
                <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x0B-ssh/2-ssh_config">Client configuration file</a>
            </strong>
            <p><code>2-ssh_config:</code> SSH configuration file configured to use the private key <code>~/.ssh/school</code> and to refuse authentication using a password.</p>
        </li>   
     <li>
            <strong>
                <a href="https://github.com/NyasimiPhilip/alx-system_engineering-devops/blob/master/0x0B-ssh/100-puppet_ssh_config.pp">Client configuration using puppet</a>
            </strong>     
            <p><code>100-puppet_ssh_config.pp</code></p>   
            <p>Ensures the line 'PasswordAuthentication no' is present in the specified file (/etc/ssh/ssh_config),
                effectively disabling password-based authentication for SSH.</p>
            <p>Ensures the line 'IdentityFile ~/.ssh/school' is present in the same file, specifying the path to an
                identity file (~/.ssh/school) for authentication when connecting via SSH.</p>
                </li>       
    </ul>
</body>

</html>
