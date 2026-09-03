# stringcalc-env — starter scaffold (YOU fill this in)

This is an empty scaffold for Build-It-Yourself Task 2. Every file has structure
and `TODO`s but no working logic — that's your job. See `task2-brief.md` for the
full brief and grading rubric.

## Build in THIS order (important)

Get correct things working first, break them second, grade them third, attack last:

1. **`reference_fix.py`** — write the CORRECT `add`. Run `python reference_fix.py`
   and eyeball the outputs (0,1,6,2,6).
2. **`tests_hidden.py`** — fill in `CASES` with strong cases, including HIDDEN
   inputs not shown in task.md. Sanity-check your reference fix passes them all
   (you can write 3 throwaway lines to loop CASES against reference_fix.add).
3. **`task.md`** — finalize the prompt so every rule your tests check is stated.
4. **`stringcalc.py`** — now write the BUGGY version the agent will start from.
5. **`verifier.py`** — implement the grader (the main deliverable). Fill in the
   three TODO functions: `load_agent_add`, `check_one`, `main`.
6. **Attack it** — create cheating `stringcalc.py` variants (see FAILURE_ANALYSIS.md)
   and confirm each FAILs. Record results.
7. **`Dockerfile`** — last. COPY in only `task.md` + `stringcalc.py`.

## How to test your verifier as you go

```bash
# Does your CORRECT fix pass? (copy reference into place, then grade)
cp reference_fix.py stringcalc.py
python verifier.py            # want: PASS, exit 0

# Does the BUGGY version fail? (restore your buggy one first)
#   ...put your buggy stringcalc.py back...
python verifier.py            # want: FAIL, exit 1
```

(Check the exit code with `echo $?` on Linux/Mac/WSL, or `echo %ERRORLEVEL%` on Windows cmd.)

## The checklist (from the brief)

- [ ] `reference_fix.py` passes your verifier
- [ ] the buggy `stringcalc.py` FAILS your verifier
- [ ] hidden tests are truly hidden from the agent's sandbox
- [ ] a hardcoded-for-visible-inputs fake FAILS on your hidden cases
- [ ] verifier fails cleanly on: missing file, wrong return type, exception, renamed fn
- [ ] exit codes correct: 0 = pass, 1 = fail

## When you're stuck or done

Paste your `verifier.py` to me. I'll review it like a Bespoke grader and actively
try to find cheats you didn't cover.
