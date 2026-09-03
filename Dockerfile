FROM python:3.12-slim

WORKDIR /workspace

# Only what the agent should see — NOT the verifier, hidden tests, or reference fix
COPY task.md /workspace/task.md
COPY stringcalc.py /workspace/stringcalc.py

CMD ["/bin/bash"]