#!/usr/bin/env python3
"""sampling_math.py — what does "I read 100 random rejects and found no misses" actually tell you?

Stdlib only. Every number the film says comes from this script's output.

Inputs are real counts from the Lectern runs (quality report 2026-09-26: 3,446 postings, 97 kept, 3,349 rejected,
a 100-row random reject sample; run 2026-10-18: 3,243 postings, 90 kept). The "5 relevant" figure is
Professor Bear's own count of postings that fit him, said in chat on 2026-10-18; it is an assumption here, not a
measurement, and the script takes it as a parameter.

    python3 sampling_math.py
"""
import math, random

N_ALL, N_REJ, SAMPLE = 3446, 3349, 100        # the 2026-09-26 run and its reject sample
RELEVANT = 5                                   # Professor Bear's count, 2026-10-18 (an assumption)


def p_zero_hypergeom(population, misses, n):
    """P(no miss in n draws without replacement, when `misses` of `population` rejects are misses)."""
    if misses == 0:
        return 1.0
    return math.comb(population - misses, n) / math.comb(population, n)


def n_needed(rate, confidence=0.95):
    """Draws needed so that zero misses seen bounds the miss rate below `rate` at `confidence`
    (equally: so that a miss, if the rate is `rate`, is seen with that probability)."""
    return math.ceil(math.log(1 - confidence) / math.log(1 - rate))


print(f"Population: {N_ALL:,} postings, {N_ALL - N_REJ} kept, {N_REJ:,} rejected. Sample: {SAMPLE} random rejects.\n")

rate = RELEVANT / N_ALL
print(f"1. The base rate. {RELEVANT} relevant postings in {N_ALL:,} is {rate:.4%}, about 1 in {1 / rate:,.0f}.")
print(f"   (1 in 500 would be 0.2000%, or {N_ALL / 500:.1f} postings in {N_ALL:,}.)")
for label, p in (("5 in 3,446", rate), ("1 in 500", 1 / 500)):
    print(f"   A blind random sample of {SAMPLE} postings at {label} expects {SAMPLE * p:.2f} relevant ones; "
          f"P(finding none) = {(1 - p) ** SAMPLE:.1%}, P(finding at least one) = {1 - (1 - p) ** SAMPLE:.1%}.")

print(f"\n2. Zero misses in {SAMPLE} reads, as the number of real misses among the {N_REJ:,} rejects changes.")
print("   misses  share of rejects   P(see none in 100)   P(see at least one)")
for m in (0, 1, 2, 5, 6, 10, 33, 100, 335):
    z = p_zero_hypergeom(N_REJ, m, SAMPLE)
    print(f"   {m:>6}  {m / N_REJ:>14.2%}   {z:>17.1%}   {1 - z:>18.1%}")

upper = 1 - 0.05 ** (1 / SAMPLE)
print(f"\n3. What zero in {SAMPLE} rules out. With 95% confidence the miss rate is below {upper:.2%} "
      f"(the 'rule of three' says 3/{SAMPLE} = {3 / SAMPLE:.0%}). That is up to about {upper * N_REJ:.0f} missed postings "
      f"among {N_REJ:,} rejects. It cannot tell zero from one in 600.")

print("\n4. How many random reads it would take to be able to say a miss rate is below X (95% confidence, zero found).")
for label, r in (("3%", 0.03), ("1%", 0.01), ("0.5%", 0.005), ("1 in 500", 1 / 500), ("1 in 600", 1 / 600)):
    n = n_needed(r)
    print(f"   below {label:>8}: {n:>5,} reads  ({n / N_REJ:.0%} of the rejects)")

random.seed(7)
trials, hits, M = 200_000, 0, 5
ids = range(N_REJ)
for _ in range(trials):
    if not any(i < M for i in random.sample(ids, SAMPLE)):
        hits += 1
print(f"\n5. Check by simulation: with {M} hidden misses, {trials:,} random samples of {SAMPLE} found none "
      f"in {hits / trials:.1%} of them (exact: {p_zero_hypergeom(N_REJ, M, SAMPLE):.1%}).")
