def avgdist_peaks(seq):
    seq = list(seq)
    if len(seq) < 3:
        return 0.0
    if len(set(seq)) == 1:
        return 0.0
    else:
        peak_position = []
        for i in range(1, len(seq)):  # This iteration is to look for the position of peak value
            if seq[i] - seq[i - 1] < 0 and i == 1:  # This is the first value
                peak_position.append(i - 1)
            if seq[i] - seq[i - 1] > 0:
                if i == len(seq) - 1:  # This is the last value
                    peak_position.append(i)
                else:
                    if seq[i + 1] - seq[i] < 0:
                        peak_position.append(i)
        if len(peak_position) < 2:
            return 0.0
        else:
            l = []
            t = 0  # calculate the combination of possible peak pairs
            while len(
                    peak_position) > 0:  # This iteration is to compute the all situation of the distance of each pair peaks
                for x in range(0, len(peak_position)):
                    for i in range(0, len(peak_position) - 1):
                        m = peak_position[-1] - peak_position[
                            i]  # All situation of last value has in terms of pair peaks
                        l.append(m)
                        t = t + 1
                    peak_position.pop(-1)

            return sum(l) / t


assert abs(avgdist_peaks((0, 1, 0))) < 1e-6
assert abs(avgdist_peaks((0, 1, 1, 0))) < 1e-6

