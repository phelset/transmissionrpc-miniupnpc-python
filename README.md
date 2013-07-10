transmissionrpc-miniupnpc-python
================================
My transmission-daemon would not properly map peer port with UPnP IGD, this is my solution.
This code (and readme) is for personal use, and not intended for others.

In short therms my code does this:

1. Find current peer port via Transmission RPC
2. Check if current peer port is mapped
  * Exit if port is successfully mapped (nothing to do)
3. Try to map port if available
  * Find alternate port
4. Update (new) peer port via Transmission RPC

Libraries
---------

* transmissionrpc: http://pythonhosted.org/transmissionrpc/
* miniupnpc: https://github.com/miniupnp/

Install transmissionrpc python library in Ubuntu:

  $ sudo apt-get install python-transmissionrpc

Install miniupnpc python library in Ubuntu:

  $ sudo apt-get install git make python-dev
  $ git clone https://github.com/miniupnp/miniupnp.git
  $ cd miniupnp/miniupnpc
  $ make pythonmodule
  $ sudo make installpythonmodule
