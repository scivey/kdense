from scipy import stats
import numpy as np
from . import util

class ApproximateKernelDensity(object):
    def __init__(self, data, kernel_stdev=1.0, std_cutoff=5.0):
        self.kernel_stdev = kernel_stdev
        self.data = np.array(data)
        self.data.sort()
        self.std_cutoff = std_cutoff
        self._dist_list = []
        for point in self.data:
            self._dist_list.append(
                [point, stats.norm(loc=point, scale=kernel_stdev)]
            )

    def pdf(self, x):
        cutoff = self.std_cutoff * self.kernel_stdev
        first_idx, _ = util.binsearch_closest(x - cutoff, self.data)
        in_range = False
        cum_pdf = 0.0
        sample_count = 0
        seen_indexes = []
        for idx in xrange(first_idx, len(self.data)):
            current_mean, current_dist = self._dist_list[idx]
            absdiff = abs(current_mean - x)
            if absdiff < cutoff:
                in_range = True
                sample_count += 1
                cum_pdf += current_dist.pdf(x)
                seen_indexes.append(idx)
            else:
                if in_range:
                    break
        return cum_pdf / float(len(self.data) or 1)
