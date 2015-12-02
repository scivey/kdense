# kdense

Efficient approximate kernel density estimation for numpy/scipy.

In the naive approach to KDE, the kernel pdf is evaluated for every known data point. The `ApproximateKernelDensity` class in kdense improves on this by only evaluating the pdf against points that are close enough to make a meaningful contribution to the outcome.  Depending on data set and parameters, this can improve performance by orders of magnitude.

`ApproximateKernelDensity` uses a Gaussian kernel with (configurable) standard deviation 1.0.  Its `std_cutoff` parameter determines how many standard deviations away a point should be before being ignored, and defaults to 5.

## Install

```bash
sudo pip install kdense
```

## Example

```python
from kdense import ApproximateKernelDensity
import numpy as np
from numpy import random

data = np.array([
    random.normal(loc=50.0, scale=20.0) for _ in xrange(200)
])
model = ApproximateKernelDensity(data)
probability_of_30 = model.pdf(30.0)
```
