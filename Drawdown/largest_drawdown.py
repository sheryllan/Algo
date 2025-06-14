
def drawdowncalc(rets, N):
    if not rets or N <= 0:
        return 0

    # Calculate cumulative returns
    cumulative_returns = [1 + rets[0]]
    for ret in rets[1:]:
        cumulative_returns.append(cumulative_returns[-1] * (1 + ret))

    # Calculate drawdowns
    drawdowns = [0]
    peak = 1
    for value in cumulative_returns:
        if value > peak:
            peak = value
            if(drawdowns[-1] != 0):
                drawdowns.append(0)
        else:
            drawdown = (peak - value) / abs(peak)
            if(drawdown>drawdowns[-1]):
                    drawdowns[-1] = drawdown


    if(drawdowns[-1] == 0):
        drawdowns.pop()

    # Sort drawdowns in descending order
    drawdowns.sort(reverse=True)
    # print(drawdowns)

    # Return the Nth largest drawdown
    cnt = len(drawdowns)
    if N > cnt:
        return cnt
    else:
        return -round(drawdowns[N - 1], 4)

def get_peaks_troughs(rets):
    cum_ret = 1 + rets[0]
    cumulative_returns = [cum_ret]
    peaks_troughs = [0]  # 1 - peak, 2 - trough, 0 - none
    for i in range(1, len(rets) - 1):
        cum_ret = cumulative_returns[-1] * (1 + rets[i])
        cum_ret_next = cum_ret * (1 + rets[i + 1])
        cum_ret_prev = cumulative_returns[-1]
        if cum_ret_prev <= cum_ret and cum_ret >= cum_ret_next:
            peaks_troughs.append(1)
        elif cum_ret_prev >= cum_ret and cum_ret <= cum_ret_next:
            peaks_troughs.append(2)
        else:
            peaks_troughs.append(0)

        cumulative_returns.append(cum_ret)

    if len(rets) > 2:
        cumulative_returns.append(cumulative_returns[-1] * (1 + rets[-1]))
        peaks_troughs.append(0)
    if len(rets) > 1:
        peaks_troughs[0] = int(cumulative_returns[0] >= cumulative_returns[1])  # first peak
        peaks_troughs[-1] = 2 if cumulative_returns[-1] <= cumulative_returns[-2] else 0  # first trough

    return cumulative_returns, peaks_troughs



# #
# print(get_peaks_troughs([0.01, -0.04, 0.05, -0.01, -0.01, 0.01]))
# print(get_peaks_troughs([0.01, -0.01, 0.004, -0.02, 0.01]))
# print(get_peaks_troughs([-0.04, -0.03, -0.09]))


"""
There are 2 ways of finding a drawdown as you loop through the cumulative returns:
1) when a new peak is found, previous max peak and min trough must be a drawdown
2) when the current trough is lower than all troughs behind it - the lowest trough thereafter 
"""

def drawdown_calc(rets, N):
    if not rets or N <= 0:
        return 0

    cumulative_return = 1
    cumulative_returns = []
    min_trough_thereafter = float('inf')
    min_troughs_thereafter = [min_trough_thereafter] * len(rets)

    L = len(rets)
    for i in range(L):
        cumulative_return *= (1 + rets[i])
        cumulative_returns.append(cumulative_return)
    for i in range(L - 1, -1, -1):
        min_trough_thereafter = min(min_trough_thereafter, cumulative_returns[i])
        min_troughs_thereafter[i] = min_trough_thereafter

    max_peak = 1
    min_trough = float('inf')
    dropdowns = []
    for i in range(len(rets)):
        cum_ret = cumulative_returns[i]
        if cum_ret == max_peak:  # only need to check for max_peak because peak has to be set before trough for a drawdown
            continue

        if cum_ret > max_peak:
            if max_peak > min_trough:  # at a new potential peak, add the dropdown found from the last max_peak
                dropdowns.append(round((min_trough - max_peak) / abs(max_peak), 4))
                min_trough = float('inf')  # scenario 1 of min_trough value change
            max_peak = cum_ret  # scenario 1 of max_peak value change
        elif cum_ret < min_trough:  # at a potential trough
            # possibility of setting min_trough ahead of max_peak, which results in not a drawdown.
            # ruled out by previous 2 checks of cum_ret against max_peak, so that cum_ret must < max_peak
            min_trough = cum_ret  # scenario 3 of min_trough value change
            if min_trough <= min_troughs_thereafter[i]:
                dropdowns.append(round((min_trough - max_peak) / abs(max_peak), 4))
                min_trough = float('inf')  # scenario 2 of min_trough value change
                max_peak = cum_ret  # scenario 2 of max_peak value change

    if max_peak > min_trough:
        dropdowns.append(round((min_trough - max_peak) / abs(max_peak), 4))
    dropdowns = sorted(dropdowns, reverse=True)
    # print(dropdowns)
    return dropdowns[N - 1] if len(dropdowns) >= N else len(dropdowns)



print(drawdown_calc([0.01, -0.01, 0.004, -0.02, 0.01], 1))
print(drawdown_calc([0.01, -0.04, 0.05, -0.01, -0.01, 0.01], 3))
print(drawdown_calc([-0.02, -0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01], 1))
print(drawdown_calc([-0.01, 0, 0, 0, 0, 0, 0, 0, 0, -0.01], 1))
print(drawdown_calc([-0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0.01], 2))
print(drawdown_calc([0.01, -0.01, 0.01, 0.01, 0.01, -0.02, 0.01, -0.03, 0.02, -0.04, 0.005, -0.001], 3))
print(drawdown_calc([0.01, -0.01, 0.01, 0.01, 0.01, -0.02, 0.01, -0.03, 0.02, -0.04, 0.005, -0.001], 5))

print('\n')
print(drawdowncalc([0.01, -0.01, 0.004, -0.02, 0.01], 1))
print(drawdowncalc([0.01, -0.04, 0.05, -0.01, -0.01, 0.01], 3))
print(drawdowncalc([-0.02, -0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01], 1))
print(drawdowncalc([-0.01, 0, 0, 0, 0, 0, 0, 0, 0, -0.01], 1))
print(drawdowncalc([0.01, -0.01, 0.01, 0.01, 0.01, -0.02, 0.01, -0.03, 0.02, -0.04, 0.005, -0.001], 3))

