import signal
import sys

def installSignalHandler(f):
    def handleSignal(signum, frame):
        print 'Exiting server'
        f()
        sys.exit(0)
    signal.signal(signal.SIGINT, handleSignal)
    signal.signal(signal.SIGTSTP, handleSignal)
