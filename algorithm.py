# Distinct weight sampling heavy hitters implementation
from datasketch import HyperLogLog
import mmh3


def hash(subdomain, domain):
    return mmh3.hash128("%s_%s" % (subdomain, domain)) / float(2**128)

class DistinctHeavyHitter:

    def __init__(self, k, threshold=1):
        self.dCounters = {}
        self.seeds = {}
        self.tho = {}
        self.threshold = threshold
        self.k = k

    def ingest(self, subdomain, domain):
        hash_value = hash(subdomain, domain)
        if domain in self.dCounters:
            self.dCounters[domain].update(subdomain.encode('utf8'))
            self.seeds[domain] = min(self.seeds[domain], hash_value)
        else:
            if hash_value < self.threshold:
                self.dCounters[domain] = HyperLogLog()
                self.dCounters[domain].update(subdomain.encode('utf8'))
                self.seeds[domain] = hash_value
                self.tho[domain] = self.threshold
                if len(self.dCounters) > self.k:
                    max_seed_domain = -1
                    domain_key = None
                    for key in self.seeds:
                        if max_seed_domain < self.seeds[key]:
                            max_seed_domain = self.seeds[key]
                            domain_key = key
                    self.threshold = self.seeds[domain_key]
                    del self.dCounters[domain_key]
                    del self.seeds[domain_key]
                    del self.tho[domain_key]

    def get(self):
        return [(domain, self.dCounters[domain].count(), self.tho[domain]) for domain in self.dCounters]