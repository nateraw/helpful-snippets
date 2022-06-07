import streamlit as st

st.title("Helpful Snippets")
st.markdown("Below are some helpful interactive snippets that I've found useful. Will add to these as I think of them.")

st.markdown("### Pip install from GitHub repo")

repo_id = st.text_input("Repo", "huggingface/transformers")
repo_owner, repo_name = repo_id.split("/")[-2:]
branch_name = st.text_input("Branch Name")
nb = st.checkbox("Installing in notebook?")
st.markdown(f"""
Now you can copy this into your {'notebook' if nb else 'terminal'} and run:
```
{"! " if nb else ""}pip install git+https://github.com/{repo_owner}/{repo_name}{"@" + branch_name if branch_name.strip() != "" else ""}
```
""")
