# Distinct weight sampling heavy hitters implementation
from datasketch import HyperLogLog
import mmh3


def hash(subdomain, domain):
    return mmh3.hash128("%s_%s" % (subdomain, domain)) / float(2**128)

class DistinctHeavyHitters:

    def __init__(self, k, threshold=1):
        self.dCounters = {}
        self.seeds = {}
        self.tho = {}
        self.threshold = threshold
        self.k = k

    def update(self, subdomain, domain):
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

    def count(self):
        return [(domain, self.dCounters[domain].count(), self.tho[domain]) for domain in self.dCounters]

class HeavyHitters:
    def __init__(self, k):
        self.k = k
        self.counters = {}

    def update(self, subdomain):
        if subdomain in self.counters:
            self.counters[subdomain] += 1
        elif len(self.counters) < self.k:
            self.counters[subdomain] = 1
        else:
            keys_to_delete = []
            for key in self.counters:
                self.counters[key] -= 1
                if self.counters[key] == 0:
                    keys_to_delete.append(key)
            for key in keys_to_delete:
                del self.counters[key]

    def get(self):
        return [key for key in self.counters]