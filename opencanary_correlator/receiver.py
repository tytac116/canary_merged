import sys
import simplejson as json
from pkg_resources import resource_filename
import opencanary_correlator
from twisted.protocols.basic import LineReceiver
from twisted.python import usage
from twisted.internet import protocol
from twisted.internet import reactor
from opencanary_correlator.dispatcher import process_device_report

class CorrelatorOptions(usage.Options):
    optParameters = [['ip',   'i', '127.0.0.1', 'IP Address to listen on'],
                     ['config', 'c', None, 'Config file']]

    def postOptions(self):
        if self.opts['config'] is None:
            conf = resource_filename(__name__, 'opencanary_correlator.conf')
            self.opts['config'] = conf
            print("Warning: no config file specified. Using the template config (which does not have any alerting configured):\n%s\n" % conf, file=sys.stderr)

class CorrelatorReceiver(LineReceiver):
    delimiter = "\n".encode()
    MAX_LENGTH = 16384

    def lineReceived(self, line):
        try:
            event = json.loads(line)
        except Exception as e:
            print("Failed to decode line", file=sys.stderr)
            print(e)
            return

        process_device_report(event)

class CorrelatorFactory(protocol.Factory):
    protocol = CorrelatorReceiver

def main():
    from twisted.python import log
    from opencanary_correlator.common import config

    log.logfile=sys.stderr
    try:
        config = CorrelatorOptions()
        config.parseOptions()
    except usage.UsageError as ue:
        print('%s:' % sys.argv[0], ue, file=sys.stderr)
        print(config)
        sys.exit(1)

    opencanary_correlator.common.config.config = opencanary_correlator.common.config.Config(config.opts['config'])


    f = CorrelatorFactory()
    reactor.listenTCP(1514, f, interface=config.opts['ip'])
    reactor.run()

if __name__ == "__main__":
    main()