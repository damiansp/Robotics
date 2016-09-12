################################
#                              #
#  Better weighted resampling  #
#                              #
################################

#given a set of particles p, and a set of weight w, returns p resamplings
# of p according to weights w

p3 = []
index = int( random.uniform(0, len(p)) )
beta = 0
for j  in range(len(p)):
    beta += random.uniform(0, 2 * max(w))
    while w[index] < beta:
        beta -= w[index]
        index = (index + 1) % len(p)
    p3.append(p[index])

p = p3
