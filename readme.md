## ngrook.py is a simple BugHunting/Pentesting tool (server html iframes or whatever you want)
<hr/>
*Only dependency is to have ngrok installed and configured!*
<br/>
<p>add to or modify the index.html in the static directory, and run the script, copy the long url and paste it (you know the drill!)</p>
<p>Very useful for csrf attacks or oauth code leaks etc...</p>
<br/>
<p>Btw don't hook this to any web interface as someone could inject code, for example: python3 ngrook.py 0.0.0.0 4444;ls</p>
