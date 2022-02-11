![Test Workflow](https://github.com/kjczarne/genevieve/actions/workflows/test-workflow.yaml/badge.svg)

[![codecov](https://codecov.io/gh/kjczarne/genevieve/branch/main/graph/badge.svg?token=2UY06SMWYC)](https://codecov.io/gh/kjczarne/genevieve)

# Genevieve

**GEN**erate **E**n**VI**ronm**E**nt **V**ariables **E**verywhere.

This is an extremely simple utility that produces:

- `env.ps1` PowerShell script
- `env.env` Bourne Shell script

The input is a `yaml` file in the form of:

```yaml
variables:
  SOME_KEY: 'some_value'
```

In POSIX shells the generated `env.env` can be used via: `source env.env` to set the environment variables set in the YAML file.
In PowerShell the `env.ps1` script should be run directly: `./env.ps1`.

## Troubleshooting

### Script execution permissions

#### PowerShell

Adjust your `ExecutionPolicy`.

#### Bourne shell

Run `chmod +x env.env`.
