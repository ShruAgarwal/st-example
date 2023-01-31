# Deploy Streamlit Apps with one click! 🎉

This is a demo of the Github Bot that comments with a deploy link on new PRs.


## How to Use? 👀
Copy the below workflow code & make these changes as per your needs:
- Under `jobs` section, you can replace the branch name `develop/**` to whatever that is mentioned to make PRs on that branch.
- For the `&mainModule` param, under `message` section, replace with the name of your Streamlit app.

```yaml
name: Streamlit deploy link
on:
  pull_request:    # A new PR is opened
    types: opened
    
# Avoid duplicate workflows on same branch
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
  
# To trigger the bot to comment with a Streamlit Cloud deploy link
jobs:
 comment:
   runs-on: ubuntu-latest
   steps:
     - name: Check branch  # scans for new PRs on 'develop' related branch
       if: startsWith(github.event.pull_request.head.ref, 'develop/**')
       run: echo "Pull request is from the correct branch"
 
     - name: Post comment
       uses: thollander/actions-comment-pull-request@v2
       with:
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         message: |     # repo & branch paths are input query params for deploy dialog
           Thanks for the pull request! 
           You can now deploy this app using Streamlit here 👉 [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=${{ github.repository }}&branch=${{ github.event.pull_request.head.ref }}&mainModule=streamlit_app.py)
           
```
⚡ Save this workflow file with `.yml` under `.github/workflows/` folder in the root of your repo.

After this, whenever you or contributors make any new changes in the app and open a PR, this bot will send a **deploy link** to test those new changes made.

>An example you can see that I've tried to make a PR 👉 https://github.com/ShruAgarwal/st-example/pull/8#issuecomment-1383148682
 
