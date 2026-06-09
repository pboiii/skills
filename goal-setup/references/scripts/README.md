# Goal Packet Scripts

These scripts are templates. Copy the useful ones into a generated goal folder and adapt them to the repo.

## goal-check.sh

Runs commands listed in `checks/commands.txt`, writes logs to `proof/logs/`, and exits nonzero if any required check fails.

Suggested setup from the installed skill bundle:

```bash
mkdir -p checks proof/logs
cp <skill-dir>/references/scripts/goal-check.sh ./goal-check.sh
cp <skill-dir>/references/scripts/commands.example.txt ./checks/commands.txt
chmod +x ./goal-check.sh
```

Run those commands from the generated goal folder and replace `<skill-dir>` with
the path to the installed `goal-setup` skill. Then edit `checks/commands.txt`
for the repo.

## validate-goal-pack.py

Checks whether a generated packet contains the expected files and sections. It does not prove completion.

```bash
python validate-goal-pack.py docs/goals/plans-to-implement/<slug> --standard
```

## update-goal-state.py

Updates the current resume capsule.

```bash
python update-goal-state.py docs/goals/plans-to-implement/<slug> \
  --verdict "M1 complete; final validation pending" \
  --next "Run ./goal-check.sh final" \
  --evidence "proof/logs/latest-summary.md"
```

## build-proof-index.py

Scans `proof/` and writes a reviewer-facing `proof/README.md`.

```bash
python build-proof-index.py docs/goals/plans-to-implement/<slug>
```
