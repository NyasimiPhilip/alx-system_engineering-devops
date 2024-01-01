 <h1>Shell, I/O Redirections and Filters Project</h1>
  <p>In this project, I learned about using the head, tail, find, wc, sort, uniq, grep, and tr commands to redirect standard input and output and combine commands in the Shell. Further, I learned about how special characters work and how to filter text from files.</p>
  <h2>Tasks</h2>
  <ul>
    <li>
      <p>0. Hello World</p>
      <code>0-hello_world:</code> Bash script that prints "Hello, World" followed by a new line to the standard output.
    </li>
    <li>
      <p>1. Confused smiley</p>
      <code>1-confused_smiley:</code> Bash script that displays a confused smiley "(Ôo)".
    </li>
    <li>
      <p>2. Let's display a file</p>
      <code>2-hellofile:</code> Bash script that displays the content of the /etc/passwd file.
    </li>
    <li>
      <p>3. What about 2?</p>
      <code>3-twofiles:</code> Bash script that displays the content of etc/passwd and /etc/hosts.
    </li>
    <li>
      <p>4. Last lines of a file</p>
      <code>4-lastlines:</code> Bash script that displays the last 10 lines of /etc/passwd.
    </li>
    <li>
      <p>5. I'd prefer the first ones actually</p>
      <code>5-firstlines:</code> Bash script that displays the first 10 lines of /etc/passwd.
    </li>
    <li>
      <p>6. Line #2</p>
      <code>6-third_line:</code> Bash script that displays the third line of the file iacta.
    </li>
    <li>
      <p>7. It is a good file that cuts iron without making a noise</p>
      <code>7-file:</code> Bash script that creates a file named exactly \*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:) containing the text Holberton School ending by a new line.
    </li>
    <li>
      <p>8. Save current state of directory</p>
      <code>8-cwd_state:</code> Bash script that writes into the file ls_cwd_content the result of the command ls -la.
    </li>
    <li>
      <p>9. Duplicate last line</p>
      <code>9-duplicate_last_line:</code> Bash script that duplicates the last line of the file iacta.
    </li>
    <li>
      <p>10. No more javascript</p>
      <code>10-no_more_js:</code> Bash script that deletes all the regular files (not directories) with a .js extension that are present in the current directory and all its subfolders.
    </li>
    <li>
      <p>11. Don't just count your directories, make your directories count</p>
      <code>11-directories:</code> Bash script that counts the number of directories and sub-directories in the current directory, not including the current and parent directories but counting hidden ones.
    </li>
    <li>
      <p>12. What’s new</p>
      <code>12-newest_file:</code> Bash script that displays the 10 newest files in the current directory, one file per line, sorted from newest to oldest.
    </li>
    <li>
      <p>13. Being unique is better than being perfect</p>
      <code>13-unique:</code> Bash script that takes a list of words as input and only prints words that appear exactly once, one word per line, sorted.
    </li>
    <li>
      <p>14. It must be in that file</p>
      <code>14-findthatword:</code> Bash script that displays lines containing the pattern "root" from the file /etc/passwd.
    </li>
    <li>
      <p>15. Count that word</p>
      <code>15-countthatword:</code> Bash script that displays the number of lines containing the pattern "bin" in the file /etc/passwd.
    </li>
    <li>
      <p>16. What's next?</p>
      <code>16-whatsnext:</code> Bash script that displays lines containing the pattern "root" and 3 lines after them in the file /etc/passwd.
    </li>
    <li>
      <p>17. I hate bins</p>
      <code>17-hidethisword:</code> Bash script that displays all lines in the file /etc/passwd that do not contain the pattern "bin".
    </li>
    <li>
      <p>18. Letters only please</p>
      <code>18-letteronly:</code> Bash script that displays all lines of the file /etc/ssh/sshd_config starting with a letter, including capital letters.
    </li>
    <li>
      <p>19. A to Z</p>
      <code>19-AZ:</code> Bash script that replaces all characters A and c from input to Z and e respectively.
    </li>
    <li>
      <p>20. Without C, you would live in hiago</p>
      <code>20-hiago:</code> Bash script that removes all letters c and C from input.
    </li>
    <li>
      <p>21. esreveR</p>
      <code>21-reverse:</code> Bash script that reverses its input.
    </li>
    <li>
      <p>22. DJ Cut Killer</p>
      <code>22-users_and_homes:</code> Bash script that displays all users and their home directories, sorted by users, based on the /etc/passwd file.
    </li>
  </ul>

 <h2>Additional Tasks</h2>

  <ul>
    <li>
      <p>23. Empty casks make the most noise</p>
      <code>100-empty_casks:</code> Bash script that finds all empty files and directories in the current directory and all sub-directories as follows:
      <ul>
        <li>Only the names of the files and directories are displayed.</li>
        <li>Hidden files included.</li>
        <li>One file name per line.</li>
      </ul>
    </li>
    <li>
      <p>24. A gif is worth ten thousand words</p>
      <code>101-gifs:</code> Bash script that lists all the files with a .gif extension in the current directory and all its sub-directories as follows:
      <ul>
        <li>Hidden files included.</li>
        <li>Only regular files (not directories) listed.</li>
        <li>File names displayed without extensions.</li>
        <li>Files sorted by byte values, but case insensitive.</li>
        <li>One file name per line.</li>
      </ul>
    </li>
    <li>
      <p>25. Acrostic</p>
      <code>102-acrostic:</code> Bash script that decodes acrostics that use the first letter of each line.
    </li>
    <li>
      <p>26. The biggest fan</p>
      <code>103-the_biggest_fan:</code> Bash script that parses web server logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
      <ul>
        <li>Ordered by number of requests, with most active hosts or IP's at the top.</li>
      </ul>
    </li>
  </ul>
