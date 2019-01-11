### Generate stats about the runtime directory

Use the playbook here to produce stats about where the playbook ran.

```
ANSIBLE_SHOW_CUSTOM_STATS=True ansible-playbook -i "localhost," -e ansible_python_interpreter=$(which python) sniffing/inspect_tower_directory.yml
```

This will produce information about the environment that includes

 - playbook_dir: directory where playbook exists
 - job_pwd: current working directory where it is invoked
 - job_env: environment variables and values
 - job_files: dictionary of relative filenames

