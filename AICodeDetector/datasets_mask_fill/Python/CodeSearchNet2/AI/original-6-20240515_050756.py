
    print >> sys.stderr, "Caught SIGQUIT, exiting..."
    sys.exit(1)

def main():
    global debug
    debug = True
    signal.signal(signal.SIGINT, sigquit_handler)
    signal.signal(signal.SIGTERM, sigquit_handler)
    signal.signal(signal.SIGQUIT, sigquit_handler)
    signal.signal(signal.SIGHUP, sigquit_handler)
    signal.signal(signal.SIGUSR1, sigquit_handler)
    signal.signal(signal.SIGUSR2, sigquit_handler)
   