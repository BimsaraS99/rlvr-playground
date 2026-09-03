# The sandbox the agent works in.
#
# CRITICAL design rule for THIS task: the agent must NOT be able to see the
# hidden tests, the verifier, or your reference fix — otherwise it can cheat
# (edit the tests, or hardcode answers for the exact test inputs).
#
# TODO: COPY in ONLY the files the agent should see. Think carefully about which
# ones those are. (Hint: it needs the prompt and the broken code — nothing else.)

FROM python:3.12-slim

WORKDIR /workspace

# TODO: COPY only the agent-visible files into /workspace.
#   COPY task.md /workspace/task.md
#   COPY stringcalc.py /workspace/stringcalc.py
# Do NOT copy: verifier.py, tests_hidden.py, reference_fix.py

CMD ["/bin/bash"]
