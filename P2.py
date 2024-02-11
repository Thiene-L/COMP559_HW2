from scipy.special import comb
from math import log2, ceil

# Given values
ell = 100
c = 5

# Function to calculate the number of possible multisets for a node with degree d
def calculate_multisets(ell, d):
    # We add 1 because the node itself is included in the multiset (degree + itself)
    r = d + 1
    # The number of multisets is calculated using the formula for combinations with repetition
    multisets = comb(ell + d, r, exact=True)
    return multisets

# Function to estimate the number of dimensions required to represent the multisets
# This is done by finding the minimum number of bits required to represent the number of multisets
# And since each dimension is represented by a 32-bit floating point number, we divide the total bits by 32
def estimate_dimensions(multisets):
    # Calculate the minimum number of bits to represent the number of multisets
    bits_needed = ceil(log2(multisets))
    # Calculate the number of dimensions, with each dimension being 32 bits
    dimensions_needed = ceil(bits_needed / 32)
    return dimensions_needed

# Estimating dimensions for three scenarios: half of the nodes, 99% of the nodes, and all nodes
# These are rough estimates. For more accurate calculations, one would need empirical data.

# A rough estimate for the median degree in a BA network
d_median = c
# A rough estimate for the 99th percentile degree
d_99th_percentile = 2 * c
# A rough estimate for the max degree (as we can't calculate for n -> infinity)
d_max = 10 * c

# Calculate the number of possible multisets for median, 99th percentile, and max degrees
multisets_median = calculate_multisets(ell, d_median)
multisets_99th_percentile = calculate_multisets(ell, d_99th_percentile)
multisets_max = calculate_multisets(ell, d_max)

# Estimate the number of dimensions needed for median, 99th percentile, and max degrees
dimensions_median = estimate_dimensions(multisets_median)
dimensions_99th_percentile = estimate_dimensions(multisets_99th_percentile)
dimensions_max = estimate_dimensions(multisets_max)

print(dimensions_median, dimensions_99th_percentile, dimensions_max)