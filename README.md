# Progress metrics test

Aim is to track progress through a tutorial by running tests on participant's codebase when they commit.
This should make it easier to assist and prompt to check in on people who are stuck.

The participant should just have to copy paste a github action file into their repo when starting
so this should hopefully not confuse their learning.

- Participant commits
- Github action runs pytest and sends junit output to this app
   - (API endpoint url/token stored in organisation environment variables)
- This app saves the junit against GH user/repo and parses it to score each titorial stage
- Learner/group progress is displayed in dashboard, either in this app or separately