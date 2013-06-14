from scipy import stats

N=stats.norm
print N.mean()      # 0
print N.var()       # 1

xi = N.isf(0.95)
print xi            # -1.64485
