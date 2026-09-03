# RL Environments — practice projects in verifiable-reward task design

Two small but complete **reinforcement-learning environments** for LLM agents,
built to explore the core engineering problem behind training modern AI agents:
designing tasks whose success can be **automatically verified** and whose graders
**cannot be gamed**.

Each environment follows the same real-world lifecycle used to train coding
agents (e.g. SWE-bench-style setups):

> **prompt → sandboxed environment → grader → run an agent → failure analysis → iterate**

The tasks themselves are deliberately simple. The real content is everything
around them: deterministic inputs, independent grading, sandboxing, and — most
importantly — active defense against the many ways an agent can "pass" a grader
without actually doing the work.

---

## Why this matters

Frontier models improve by practicing against environments that score their
attempts and feed back a reward (RLVR — Reinforcement Learning with Verifiable
Rewards). The reward signal is only as good as the **verifier** that produces it.
A verifier that can be tricked doesn't just fail to help — it actively teaches the
model to cheat, because the training loop reinforces *whatever* scored well.

So the central skill isn't "write a checker." It's **adversarial verifier
design**: assume a motivated model is trying to fool your grader, and close every
loophole. Both projects here are built around that mindset.

---

## The two environments

### 1. `log-analyzer/` — verification by output comparison

The agent reads a web-server log and outputs statistics as JSON. The grader
computes the correct answer independently and compares.

**Anti-cheat mechanism: a secret grading seed.** The input log is generated
deterministically from a seed. The agent sees the log made with a public seed,
but the grader regenerates the log with a *secret* seed the agent never saw and
grades against that. Any answer that was hardcoded/memorized is instantly wrong —
the only way to pass is to genuinely read and process the input.

### 2. `stringcalc-env/` — verification by running hidden tests

The agent fixes a small buggy Python function. The grader runs the fixed function
against a suite of test cases and decides pass/fail.

**Anti-cheat mechanism: hidden test inputs.** The agent only sees a few examples
in the task prompt; the grader tests against many additional inputs it never saw.
Hardcoding the visible examples fails the moment a hidden input is tested. The
grader also defends against wrong return types, the `True == 1` bool trick,
renamed/missing functions, and deleted files — each attack was tried and caught
(see `stringcalc-env/FAILURE_ANALYSIS.md`).

**Same underlying principle, two different forms:** grade against something the
agent could not have memorized — a secret seed in one, hidden tests in the other.

---

## Key ideas demonstrated

- **Deterministic, seedable inputs** so the "correct answer" is fixed and the
  grader is trustworthy.
- **Independent grading** — the verifier computes truth itself and never trusts
  the agent's output.
- **Layered, defensive validation** — structural checks (keys, types) before value
  checks; ordering that matters for security (e.g. rejecting `bool` before the
  `int` check, since `True == 1` in Python).
- **Clean failure semantics** — every failure reports exactly what was wrong and
  exits with a proper code (`0` pass / `1` fail) so it can drive an automated
  training pipeline.
- **Sandboxing** via Docker — the agent's world contains only the task and the
  input, never the grader, hidden tests, or answer key.
- **Adversarial testing** — each grader is attacked on purpose to prove it holds,
  and remaining limitations are documented honestly.

---

## Repo structure

```
.
├── log-analyzer/          # Environment 1: output-comparison + secret seed
│   ├── task.md            # the prompt the agent reads
│   ├── generate_log.py    # deterministic, seedable input generator
│   ├── reference_solution.py
│   ├── verifier.py        # the grader (secret-seed anti-cheat)
│   ├── Dockerfile         # sandbox
│   ├── FAILURE_ANALYSIS.md
│   └── README.md
│
└── stringcalc-env/        # Environment 2: hidden-test verification
    ├── task.md            # spec the agent reads
    ├── stringcalc.py      # buggy starting code the agent must fix
    ├── reference_fix.py   # correct solution (proves solvability; not in sandbox)
    ├── tests_hidden.py    # hidden test cases (the anti-cheat)
    ├── verifier.py        # the grader (defensive, cheat-resistant)
    ├── Dockerfile         # sandbox: agent sees only task.md + stringcalc.py
    └── FAILURE_ANALYSIS.md
```

---

## Running it

Requires Python 3.10+ (and Docker if you want to run the sandbox).

### log-analyzer

```bash
cd log-analyzer
python generate_log.py --seed 42     # build the input the agent sees
python reference_solution.py         # produce a correct result.json
python verifier.py                   # grade it -> PASS

# anti-cheat demo:
python verifier.py --grade-seed 91237                                        # honest solution still PASSES
python verifier.py --result attacks/cases/hardcoded.json --grade-seed 91237  # hardcoded answer FAILS
```

### stringcalc-env

```bash
cd stringcalc-env
python verifier.py                   # grades stringcalc.py against hidden tests

# the buggy starting code FAILS; a correct fix PASSES:
copy reference_fix.py stringcalc.py  # (Linux/Mac: cp)  simulate a correct agent fix
python verifier.py                   # -> PASS
```

### Sandbox (either environment)

```bash
docker build -t <env-name> .
docker run -it --rm <env-name>
# inside: `ls` shows only the agent-visible files — grader and answer key are absent
```

---

## What a stronger, production version would add

These are learning projects, and the write-ups are honest about their limits.
A production environment would add: running the agent's code inside a
resource-limited, network-isolated container with a timeout (not on the host);
bridging the grader and the sandbox so the two are never accessible at the same
time (e.g. extract the agent's output with `docker cp`, or inject the grader only
after the agent is frozen); and generating many task variants so an agent cannot
overfit to a single instance. See each environment's `FAILURE_ANALYSIS.md` for
details.

---

## Note

These are original practice projects built to learn RL-environment and verifier
design. They are not affiliated with, nor solutions to, any company's assessment.