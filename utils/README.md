# Pipeline and Workflow Script Migration

The script `pipeline_migration.py` provides mechanisms to migrate workflows and pipelines from one Lemonade instance to another (i.e., from one database to another). The tool allows you to specify the ID of the pipeline or workflow you want to copy, but it also supports multiple IDs (as a comma-separated list) or the option to specify all IDs. However, only one type of object can be specified at a time: either pipelines (and consequently their related workflows) or workflows (traditional workflows or SQL workflows, without any link to a pipeline).

## Parameters:

 * `--source-db`: Connection string for the source database (e.g., 'mysql://user:pass@host:port');
 * `--target-db`: Connection string for the target database (e.g., 'mysql://user:pass@host:port');
 * `--type`: Specification of the target, whether a `pipeline` or a `workflow`;
 * `--id`: ID of the pipeline or workflow to migrate. Supported options are: a specific ID (e.g., `1`), a list of IDs (e.g., `1,2,3`), or `all` to migrate all pipelines/workflows;
 * `--user-login`: (Optional) When set, it will change the current user owner of the workflow/pipeline.

### Usage Example

```bash
$ python pipeline_migration.py  --source-db mysql://root:PASSWORD@0.0.0.0:33062 \
    --target-db mysql://root:PASSWORD@0.0.0.0:33063 \
    --type pipeline \
    --user-login admin@lemonade.org.br \
    --id 1
```
