from invoke import task

@task
def install(ctx):
    ctx.run("dotbot -c install.conf.yaml")
